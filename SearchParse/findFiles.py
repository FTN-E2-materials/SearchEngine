from Other import globals
from DataStructures.mySet import mySet

def findLists(words):
    listOfSets = []

    for i in range(0, len(words)):
        tempList = mySet()
        contains = globals.trie.isWord(words[i])
        if contains[0]:
            for paths in contains[1].wordShowing:
                tempList.add(paths)

        listOfSets.append(tempList)
    return listOfSets
