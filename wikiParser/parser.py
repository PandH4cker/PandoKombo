import json
from collections import Counter

from utils import removeHTMLTag, removeBrackets, \
    removeHTMLComments, removePunctuations, \
    removeBlacklistedLetters, getRelatedArticlesLinks, getRelatedArticles


class Parser:
    def __init__(self, pageGenerator):
        self.redArticles = []
        self.counter = Counter()
        self.relatedArticles = []
        self.parseFromGenerator(pageGenerator)

    def parseFromGenerator(self, gen, extend=True):
        jsonOutput = json.loads("".join(s.decode() for s in gen))
        if "errors" not in jsonOutput:
            jsonOutput = jsonOutput["parse"]
        else:
            print("[!] Page provided does not exist..")
            return
        if extend:
            if relatedArticles := getRelatedArticles(jsonOutput["text"]["*"]):
                links = getRelatedArticlesLinks(relatedArticles.group(1))
                links = list(filter(lambda item: "href=" not in item, links))
                self.relatedArticles.extend(links)
        text = removeBrackets(removeHTMLTag(jsonOutput["text"]["*"]))
        text = removePunctuations(removeHTMLComments(text))
        text = removeBlacklistedLetters(text)
        self.occurs(text)

    def occurs(self, text):
        self.counter.update(Counter(w for w in text.split() if len(w) > 3 or w.isupper()))

    def writeFile(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for k, _ in self.counter.most_common():
                f.write(k + "\n")
