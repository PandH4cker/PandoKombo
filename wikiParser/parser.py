import json
from utils import removeHTMLTag, removeBrackets, removeHTMLComments, removePunctuations, removeBlacklistedLetters


class Parser:
    def __init__(self, pageGenerator):
        self.pageGenerator = pageGenerator
        jsonOutput = json.loads("".join(s.decode() for s in self.pageGenerator))["parse"]
        s = removeBrackets(removeHTMLTag(jsonOutput["text"]["*"]))
        s = removePunctuations(removeHTMLComments(s))
        s = removeBlacklistedLetters(s)
        print(s)

