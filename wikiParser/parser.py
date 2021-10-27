import json
import string
from collections import Counter

from utils import getRelatedArticlesLinks, getRelatedArticles, Color


class Parser:
    def __init__(self, pageGenerator=None):
        self.redArticles = set()
        self.counter = Counter()
        self.relatedArticles = set()
        if pageGenerator is not None:
            self.parseFromGenerator(pageGenerator)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            p = Parser()
            p.counter = Counter({**self.counter, **other.counter})
            return p
        else:
            raise NotImplemented

    def parseFromGenerator(self, gen, extend=True):
        jsonOutput = json.loads("".join(s.decode() for s in gen))
        if "-1" not in jsonOutput["query"]["pages"]:
            jsonOutput = jsonOutput["query"]
            pages = next(iter(jsonOutput["pages"].values()))
            Color.success(f"Fetching {pages['title']}...")
            extract = pages["extract"]
            punctuation = string.punctuation.replace("-", "") \
                .replace("`", "") \
                .replace("'", "")
            extract = extract.translate(str.maketrans(punctuation, ' ' * len(punctuation)))
        else:
            pages = next(iter(jsonOutput["query"]["pages"].values()))
            Color.error(f"Can't fetch {pages['title']}...")
            return
        if extend:
            extractWithParentheses = next(iter(jsonOutput["pages"].values()))["extract"].replace("=", "")
            if relatedArticles := getRelatedArticles(extractWithParentheses):
                self.relatedArticles.update(getRelatedArticlesLinks(relatedArticles.group(1)))
        self.occurs(extract)

    def occurs(self, text):
        self.counter.update(Counter(w.lower() for w in text.split() if (len(w) > 3 or w.isupper()) and w.isalpha()))

    def writeFile(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for k, _ in self.counter.most_common():
                f.write(k + "\n")
