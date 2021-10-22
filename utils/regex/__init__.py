import re

CLEANR = re.compile("<.*?>")
CSS_STYLE = re.compile("<style.*?>.*?</style>")
BRACKETS = re.compile("\\[.*?]")
HTML_COMMENTS = re.compile("<!--.*?-->", re.DOTALL)
PUNCTUATIONS = re.compile("(&#\\d+;)|([,();″↑«»\":]+)|(\s([.\-·:]+|\\d)\s)|(\\d\.\\d)")
BLACKLIST_LETTERS = re.compile("([a-zA-Z]\s*?et\s*?[a-zA-Z])|(n o)|(a   b   c)|(v  ·   m)")


def removeHTMLTag(html):
    return re.sub(CLEANR, " ", re.sub(CSS_STYLE, " ", html))


def removeBrackets(html):
    return re.sub(BRACKETS, "", html)


def removeHTMLComments(html):
    return re.sub(HTML_COMMENTS, "", html)


def removePunctuations(html):
    return re.sub(PUNCTUATIONS, "", html)


def removeBlacklistedLetters(str):
    return re.sub(BLACKLIST_LETTERS, "", str)
