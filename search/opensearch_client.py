from opensearchpy import OpenSearch
from config.settings import settings

client = OpenSearch(
    hosts = [{"host" : "localhost", "port": 9200}],
    http_compress = True,
    http_auth = ("admin", "admin"), # We can change it to prod whenever needed
    use_ssl = False,
    verify_certs = False
)