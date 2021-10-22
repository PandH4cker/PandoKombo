from services import url, fetchApi

endPoint = "/w/api.php"


class WikiAPI:
    def __init__(self, headers=None):
        if headers is None:
            headers = {}
        self.url = f"{url}{endPoint}"
        self.headers = headers
        self.payload = {"action": "parse", "format": "json", "errorformat": "none"}

    def getPage(self, page="", headers=None):
        print(f"[+] Getting {page}...")
        if headers is None:
            headers = {}
        self.headers.update(headers)
        self.payload["page"] = page
        for line in fetchApi(endpoint=endPoint, payload=self.payload, headers=self.headers):
            yield line
