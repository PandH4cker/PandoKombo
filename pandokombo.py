import json
import urllib.parse

from API import WikiAPI
from wikiParser import Parser
from utils import printBanner, reconstructWikiLinks


class PandoKombo:
    def __init__(self):
        printBanner()
        wikiAPI = WikiAPI()
        cont = True
        parser = Parser()
        while cont:
            self.search = input("PandoKombo > Search >> ")
            jsonOutput = json.loads("".join(s.decode() for s in wikiAPI.search(self.search)))
            searchList = jsonOutput["query"]["search"]
            if searchList:
                choice = -1
                while not 0 <= choice < len(searchList):
                    for index, result in enumerate(searchList):
                        print("\t", index, "-", result["title"])
                    choice = int(input("PandoKombo > Choice >> "))
                depth = int(input("PandaKombo > Depth (Default 1) >> ") or "1")
                p = Parser(wikiAPI.getExtract(searchList[choice]["title"]))
                p.redArticles.extend(reconstructWikiLinks([searchList[choice]["title"].lower()]))
                for i in range(depth):
                    for page in list(p.relatedArticles):
                        if urllib.parse.unquote(page.lower()) not in p.redArticles:
                            p.parseFromGenerator(wikiAPI.getExtract(page), i + 1 < depth)
                        p.relatedArticles.remove(page)
                        p.redArticles.append(urllib.parse.unquote(page.lower()))
                parser += p
                cont = True if input("PandoKombo > Continue (y/n) ? (Default False) >> ") in ["Y", "y"] else False
                if not cont:
                    outputFile = input("PandaKombo > Output Filename >> ")
                    parser.writeFile(outputFile)


if __name__ == '__main__':
    PandoKombo()
