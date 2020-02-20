from Other import globals
from DataStructures.mySet import mySet

def findLists(words):
    listOfSets = []
    '''
    if len(words) == 1:
        tempList1 = mySet()

        contains1 = globals.trie.isWord(words[0])

        if contains1[0]:
            for paths in contains1[1].wordShowing.keys():
                tempList1.add(paths)

        listOfSets.append(tempList1)

        return listOfSets

    elif len(words) == 2:
        tempList1 = mySet()
        tempList2 = mySet()
        contains1 = globals.trie.isWord(words[0])
        contains2 = globals.trie.isWord(words[1])
        if contains1[0]:
            for paths in contains1[1].wordShowing.keys():
                tempList1.add(paths)

        if contains2[0]:
            for paths in contains2[1].wordShowing.keys():
                tempList2.add(paths)

        listOfSets.append(tempList1)
        listOfSets.append(tempList2)
        return tempList1, tempList2
    '''
     #eliflen(words) > 2:
    for i in range(0, len(words)):
        tempList = mySet()
        contains = globals.trie.isWord(words[i])
        if contains[0]:
            for paths in contains[1].wordShowing:
                tempList.add(paths)

        listOfSets.append(tempList)
    return listOfSets
