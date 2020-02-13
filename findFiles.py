import globals
from mySet import mySet

def findLists(word1, word2):
    tempList1 = mySet()
    tempList2 = mySet()

    if word1 == word2:
        contains1 = globals.trie.isWord(word1)

        if contains1[0]:
            for paths in contains1[1].wordShowing.keys():
                tempList1.add(paths)

        return tempList1, tempList1

    else:
        contains1 = globals.trie.isWord(word1)
        contains2 = globals.trie.isWord(word2)
        if contains1[0]:
            for paths in contains1[1].wordShowing.keys():
                tempList1.add(paths)

        if contains2[0]:
            for paths in contains2[1].wordShowing.keys():
                tempList2.add(paths)
        return tempList1, tempList2
