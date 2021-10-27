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
        payload = dict(self.payload)
        payload.update({"action": "query", "list": "search"})
        payload["srsearch"] = s
        for line in fetchApi(endpoint=endPoint, payload=payload, headers=self.headers):
            yield line

    def getExtract(self, page="", headers=None):
        if headers is None:
            headers = {}
        self.headers.update(headers)
        payload = dict(self.payload)
        payload.update({"action": "query"})
        payload["titles"] = page
        for line in fetchApi(endpoint=endPoint, payload=payload, headers=self.headers):
            yield line

    def getPage(self, page="", headers=None):
        if headers is None:
            headers = {}
        payload = dict(self.payload)
        payload.update({"action": "parse"})
        self.headers.update(headers)
        payload["page"] = page
        for line in fetchApi(endpoint=endPoint, payload=payload, headers=self.headers):
            yield line
