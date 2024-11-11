
def get_summary(model, knn):
    prompt = """You are a summarizer. I have provided the details about the commodity,
    and I will perform a similarity search to retrieve relevant results. Based on the
    similarity results, please provide a clear and concise summary for each commodity class,
    highlighting key insights, projections, and trends. The summary should be organized by
    commodity and should only focus on the most relevant information retrieved through the similarity search.

    Here are the similarity search results:
    {results}

    Please process the information and give a refined summary for each commodity,
    ensuring that unnecessary details are excluded, and the summary is easy to understand.
    """.format(results=knn)
    response = model.generate_content(prompt)
    return response.text
