import urllib.request
import urllib.parse
from config import url


def fetchApi(endpoint, payload=None, method='get', headers=None):
    if headers is None:
        headers = {}
    if payload is None:
        payload = {}
    payload = urllib.parse.urlencode(payload)
    req = urllib.request.Request(f"{url}{endpoint}?{payload}", data=payload.encode('ascii'), headers=headers,
                                 method=method)
    with urllib.request.urlopen(req) as response:
        for line in response:
            yield line
