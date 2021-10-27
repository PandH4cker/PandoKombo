import urllib.request
import urllib.parse
from .config import url


def fetchApi(endpoint: str, payload: dict = None, method: str = 'GET', headers: dict = None) -> str:
    """

    :param endpoint: str
    :param payload: dict
    :param method: str
    :param headers: dict
    :rtype: str
    """
    #Commissariat_à_l%27énergie_atomique_et_aux_énergies_alternatives
    if headers is None:
        headers = {}
    if payload is None:
        payload = {}

    if "page" in payload:
        payload["page"] = urllib.parse.unquote(payload["page"])
        payload = urllib.parse.urlencode(payload)
    elif "titles" in payload:
        payload["titles"] = urllib.parse.unquote(payload["titles"])
        payload = urllib.parse.urlencode(payload) + "&prop=extracts&explaintext"
    elif "srsearch" in payload:
        payload["srsearch"] = urllib.parse.unquote(payload["srsearch"])
        payload = urllib.parse.urlencode(payload)

    req = urllib.request.Request(f"{url}{endpoint}?{payload}",
                                 headers=headers,
                                 method=method.upper())
    with urllib.request.urlopen(req) as response:
        for line in response:
            yield line
