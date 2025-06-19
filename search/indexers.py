from search.opensearch_client import client

async def index_log(log : dict):
    index_name = "siem-logs"
    client.index(index = index_name)
    