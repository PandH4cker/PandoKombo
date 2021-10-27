from services import url, fetchApi

endPoint = "/w/api.php"


class WikiAPI:
    def __init__(self, headers=None):
        if headers is None:
            headers = {}
        self.url = f"{url}{endPoint}"
        self.headers = headers
        self.payload = {"format": "json", "errorformat": "none"}

    def search(self, s="", headers=None):
        if headers is None:
            headers = {}
        self.headers.update(headers)
        self.payload.update({"action": "query", "list": "search"})
        self.payload["srsearch"] = s
        for line in fetchApi(endpoint=endPoint, payload=self.payload, headers=self.headers):
            yield line

    def getExtract(self, page="", headers=None):
        if headers is None:
            headers = {}
        self.headers.update(headers)
        self.payload.update({"action": "query"})
        self.payload["titles"] = page
        for line in fetchApi(endpoint=endPoint, payload=self.payload, headers=self.headers):
            yield line

    def getPage(self, page="", headers=None):
        if headers is None:
            headers = {}
        self.payload.update({"action": "parse"})
        self.headers.update(headers)
        self.payload["page"] = page
        for line in fetchApi(endpoint=endPoint, payload=self.payload, headers=self.headers):
            yield line
