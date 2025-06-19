from search.opensearch_client import client

def search_logs(query: str, size: 50):
    index_name = "siem-logs"
    body = {
        "query" : {
            "query_string": {
                "query": query
            }
        },
        "size" : size
    }
    
    resp = client.search(index = index_name, body = body)
    return resp["hits"]["hits"]
    