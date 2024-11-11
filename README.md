# Commodity Brief

**"commodi_brief"** combines "Commodity" and "Brief," capturing the tool's purpose of providing concise summaries for each agricultural commodity class. The name suggests a quick, distilled overview of complex commodity data, making it easier for users to gain insights at a glance.

**Reference**
- [Get sample PDF](https://www.usda.gov/oce/commodity/wasde)

**Prerequisites**
- [Python 3.10+](https://www.python.org/downloads/#:~:text=Python%203.10.15,Release%20Notes)
- [Opensearch](https://github.com/Antony-M1/opensearch_docker) - get the opensearch from that link its a docker compose file.
- [Flake 8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8) for the PEP 8 Standard Edition

# .env
```py
GOOGLE_API_KEY=<YOUR_API_KEY>

OPENSEARCH_USERNAME=admin
OPENSEARCH_PASSWORD=Dragon@75845567
```
if you run the `opensearch` from the docker compose what I given, then thats the `username` & `password`

# Quick Start
### Step 1: Clone the repo
```
git clone https://github.com/Antony-M1/commodi_brief.git
```
### Step 2: Create & Activate environment
```
python -m venv venv
```
```
source venv/bin/activate
```

### Step 3: Install dependencies
```
pip install -r requirements.txt
```

### Step 4: Run the project
```
streamlit run main.py
```