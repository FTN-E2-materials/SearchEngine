import globals
from mySet import mySet

def findLists(graph, word1, word2):
    tempList1 = mySet()
    tempList2 = mySet()

    if word1 == word2:
        contains1 = globals.trie.isWord(word1)

        if contains1[0]:
            for paths in contains1[1].wordShowing.keys():
                tempList1.add(paths)

        return tempList1, None

    else:

        contains1 = globals.trie.isWord(word1)
        contains2 = globals.trie.isWord(word2)
        print(contains1, contains2)
        if contains1[0]:
            for paths in contains1[1].wordShowing.keys():
                tempList1.add(paths)
                print(contains1[1].wordShowing[paths])

        if contains2[0]:
            for paths in contains2[1].wordShowing.keys():
                tempList2.add(paths)
                print (contains2[1].wordShowing[paths])



        print (tempList1.__len__(), tempList2.__len__())
        return tempList1, tempList2
