from API import WikiAPI
from wikiParser import Parser


class PandoKombo:
    def __init__(self, search, outputFile, depth=4):
        self.search = search
        wikiAPI = WikiAPI()
        parser = Parser(wikiAPI.getPage(self.search))
        for i in range(depth):
            for page in list(parser.relatedArticles):
                if page not in parser.redArticles:
                    parser.parseFromGenerator(wikiAPI.getPage(page), i + 1 < depth)
                parser.relatedArticles.remove(page)
                parser.redArticles.append(page)
        parser.writeFile(outputFile)


if __name__ == '__main__':
    PandoKombo("Commissariat_à_l%27énergie_atomique_et_aux_énergies_alternatives", outputFile="test.txt")
