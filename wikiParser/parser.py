import json
from collections import Counter

from utils import removeHTMLTag, removeBrackets, \
    removeHTMLComments, removePunctuations, removeBlacklistedLetters


class Parser:
    def __init__(self, pageGenerator):
        self.counter = Counter()
        self.pageGenerator = pageGenerator
        jsonOutput = json.loads("".join(s.decode() for s in self.pageGenerator))["parse"]
        print(jsonOutput["text"]["*"])
        self.text = removeBrackets(removeHTMLTag(jsonOutput["text"]["*"]))
        self.text = removePunctuations(removeHTMLComments(self.text))
        self.text = removeBlacklistedLetters(self.text)
        self.occurs()

    def occurs(self):
        self.counter.update(Counter(w for w in self.text.split() if len(w) > 3 or w.isupper()))

    def writeFile(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for k, v in self.counter.most_common():
                f.write(k + "\n")
