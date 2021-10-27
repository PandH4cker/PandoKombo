from utils.regex import removeHTMLTag, removeBrackets, removeHTMLComments, \
    removePunctuations, removeBlacklistedLetters, getRelatedArticlesLinks, getRelatedArticles
from utils.colors import Color


def printBanner():
    print(chr(27) + "[2J")
    print(f"{Color.YELLOW.value}.------..------..------..------..------..------.\
    \b\b\b\b.------..------..------..------.\n|{Color.BLUE.value}P{Color.YELLOW.value}.--. \
    \b\b\b\b||{Color.BLUE.value}A{Color.YELLOW.value}.--. ||{Color.BLUE.value}N{Color.YELLOW.value}\
    \b\b\b\b.--. ||{Color.BLUE.value}D{Color.YELLOW.value}.--. ||{Color.BLUE.value}O{Color.YELLOW.value}\
    \b\b\b\b.--. ||{Color.BLUE.value}K{Color.YELLOW.value}.--. ||{Color.BLUE.value}O{Color.YELLOW.value}\
    \b\b\b\b.--. ||{Color.BLUE.value}M{Color.YELLOW.value}.--. ||{Color.BLUE.value}B{Color.YELLOW.value}\
    \b\b\b\b.--. ||{Color.BLUE.value}O{Color.YELLOW.value}.--. |\n| :/\: || (\/) || :(): || :/\: || :/\: \
    \b\b\b\b|| :/\: || :/\: || (\/) || :(): || :/\: |\n| (__) || :\/: || ()() || (__) || :\/: || :\/: || \
    \b\b\b\b:\/: || :\/: || ()() || :\/: |\n| '--'{Color.BLUE.value}P{Color.YELLOW.value}|| '--'{Color.BLUE.value}A\
    \b\b\b\b{Color.YELLOW.value}|| '--'{Color.BLUE.value}N{Color.YELLOW.value}|| '--'{Color.BLUE.value}D\
    \b\b\b\b{Color.YELLOW.value}|| '--'{Color.BLUE.value}O{Color.YELLOW.value}|| '--'{Color.BLUE.value}K\
    \b\b\b\b{Color.YELLOW.value}|| '--'{Color.BLUE.value}O{Color.YELLOW.value}|| '--'{Color.BLUE.value}M\
    \b\b\b\b{Color.YELLOW.value}|| '--'{Color.BLUE.value}B{Color.YELLOW.value}|| '--'{Color.BLUE.value}O\
    \b\b\b\b{Color.YELLOW.value}|\n`------'`------'`------'`------'`------'`------'`------'`------'`------'\
    \b\b\b\b`------'{Color.RESET.value}")
