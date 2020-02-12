import globals
from mySet import mySet

def findLists(graph, word1, word2):
    tempList1 = mySet()
    tempList2 = mySet()

    for keys in graph.graph.keys():
        contains1 = globals.allFiles[keys].wordTrie.isWord(word1)
        contains2 = globals.allFiles[keys].wordTrie.isWord(word2)

        if contains1[0]:
            if keys not in tempList1:
                tempList1.add(keys)

        if contains2[0]:
            if keys not in tempList2:
                tempList2.add(keys)

        if keys.find(word1) != -1:
            if keys not in tempList1:
                tempList1.add(keys)

        if keys.find(word2) != -1:
            if keys not in tempList2:
                tempList2.add(keys)


    return tempList1, tempList2
