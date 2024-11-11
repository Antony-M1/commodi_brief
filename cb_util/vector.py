import hashlib
import os
from streamlit.runtime.uploaded_file_manager import UploadedFile
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import OpenSearchVectorSearch
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter


def get_hash(uploaded_file: UploadedFile) -> str:
    """
    convert the pdf file into a hash value
    """
    file_content = uploaded_file.read()
    hash_sha256 = hashlib.sha256(file_content).hexdigest()

    return hash_sha256


class VectorDB():

    def __init__(self, uploaded_file: UploadedFile):
        self.uploaded_file = uploaded_file
        self.opensearch_username = os.environ.get('OPENSEARCH_USERNAME')
        self.opensearch_password = os.environ.get('OPENSEARCH_PASSWORD')
        self.embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.output_file = os.path.join(os.getcwd(), "output.pdf")

    def save_pdf(self) -> str:
        """
        save pdf
        """
        with open(self.output_file, "wb") as file:
            file.write(self.uploaded_file.getbuffer())

    def chunk(self) -> list:
        self.save_pdf()
        loader = PyPDFLoader(self.output_file)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=50)
        docs = text_splitter.split_documents(documents)
        return docs

    def get_knn(self, query: str = "", k: int = 10):
        docs = self.chunk()
        docsearch = OpenSearchVectorSearch.from_documents(
                        docs,
                        self.embeddings_model,
                        opensearch_url="https://localhost:9200",
                        http_auth=(self.opensearch_username, self.opensearch_password),
                        use_ssl=False,
                        verify_certs=False,
                        ssl_assert_hostname=False,
                        ssl_show_warn=False
                    )
        docs = docsearch.similarity_search(query, k=k)
        return "\n".join([doc.page_content for doc in docs])
