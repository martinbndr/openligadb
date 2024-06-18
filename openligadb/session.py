from requests import Session
from urllib.parse import urljoin

class RequestsSession(Session):
    def __init__(self):
        super().__init__()
        self.base_url = "https://api.openligadb.de"
        self.headers = {
            "accept": "application/json"
        }

    def request(self, method, url, *args, **kwargs):
        joined_url = self.base_url + url
        return super().request(method, joined_url, *args, headers=self.headers, **kwargs)