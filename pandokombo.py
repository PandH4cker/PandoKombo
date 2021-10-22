from API import WikiAPI
from wikiParser import Parser


class PandoKombo:
    def __init__(self, search):
        self.search = search
        wikiAPI = WikiAPI()
        parser = Parser(wikiAPI.getPage(self.search))


if __name__ == '__main__':
    PandoKombo("Commissariat_à_l%27énergie_atomique_et_aux_énergies_alternatives")
