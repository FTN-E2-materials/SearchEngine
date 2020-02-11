import globals


def findLists(graph, word1, word2):
    tempList1 = []
    tempList2 = []

    for keys in graph.graph.keys():
        contains1 = globals.allFiles[keys].wordTrie.isWord(word1)
        contains2 = globals.allFiles[keys].wordTrie.isWord(word2)

        if contains1[0]:
            if keys not in tempList1:
                tempList1.append(keys)

        if contains2[0]:
            if keys not in tempList2:
                tempList2.append(keys)

        if keys.find(word1) != -1:
            if keys not in tempList1:
                tempList1.append(keys)

        if keys.find(word2) != -1:
            if keys not in tempList2:
                tempList2.append(keys)


    return tempList1, tempList2
