import re

CLEANR = re.compile("<.*?>")
CSS_STYLE = re.compile("<style.*?>.*?</style>")
BRACKETS = re.compile("\\[.*?]")
HTML_COMMENTS = re.compile("<!--.*?-->", re.DOTALL)
PUNCTUATIONS = re.compile("(&#\\d+;)|([,();″↑«»\":]+)|(\s([.\-·:]+|\\d)\s)|(\\d\.\\d)")
BLACKLIST_LETTERS = re.compile("([a-zA-Z]\s*?et\s*?[a-zA-Z])|(n o)|(a   b   c)|(v  ·   m)")
RELATED_ARTICLES = re.compile(r"id=\"Articles_connexes\">.*?<ul>(.*?)<\/ul>", re.MULTILINE | re.DOTALL)
RELATED_ARTICLES_LINKS = re.compile(r"href=\"(.*?)\"")
NEW_RELATED_ARTICLES = re.compile(r"Articles connexes[\n ]*(.*)...Liens externes",
                                  re.IGNORECASE | re.MULTILINE | re.DOTALL)


def removeHTMLTag(html):
    return re.sub(CLEANR, " ", re.sub(CSS_STYLE, " ", html))


def removeBrackets(html):
    return re.sub(BRACKETS, "", html)


def removeHTMLComments(html):
    return re.sub(HTML_COMMENTS, "", html)


def removePunctuations(html):
    return re.sub(PUNCTUATIONS, "", html)


def removeBlacklistedLetters(string):
    return re.sub(BLACKLIST_LETTERS, "", string)


def getRelatedArticles(html):
    return re.search(NEW_RELATED_ARTICLES, html)


def reconstructWikiLinks(names):
    return list(map(lambda s: "_".join(s.split()), names))


def getRelatedArticlesLinks(relatedArticlesName):
    names = filter(None, relatedArticlesName.split("\n"))
    return reconstructWikiLinks(names)
