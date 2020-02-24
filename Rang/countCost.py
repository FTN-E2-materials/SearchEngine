from Other import globals
from Other.mergeSort import *

class classForShowing:
    def __init__(self, page, rang):
        self.page = page
        self.rang = rang

    def getPage(self):
        return self.page
    def getRang(self):
        return self.rang

    def setPage(self, page):
        self.page = page
    def setRang(self, rang):
        self.rang = rang


def countCost(resultSet, words):
    sortedList = []

    showingByWord = costByWord(words, resultSet)
    costByLinks(resultSet, showingByWord)

    for page in showingByWord:
        for node in globals.graph.get_incoming(page):
            if globals.trie.isWord(node):
                showingByWord[page] += 1
            else:
                showingByWord[page] += 0.5

    for page in showingByWord:
        sortedList.append(classForShowing(page, showingByWord[page]))

    mergeSort(sortedList)
    return sortedList

def costByWord(words, resultSet):
    showPages = {}

    for page in resultSet:
        showPages[page] = 0

    for word in words:
        value = globals.trie.isWord(word)
        
        if value[0]:
            for page in value[1].wordShowing:
                if page in showPages.keys():
                    showPages[page] += value[1].wordShowing[page]

    for page in resultSet:
        showPages[page] = showPages[page] * 0.5

    return showPages

def costByLinks(resultSet, showingByWord):
    for page in resultSet:
        adding = 0
        for node in globals.graph.get_incoming(page):
            if node in showingByWord.keys():
                adding += showingByWord[node]
                showingByWord[page] = adding * 0.3
