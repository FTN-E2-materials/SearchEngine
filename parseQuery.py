import globals
from findFiles import *
from operations import *
from mySet import mySet

def parseQueryOrdinary(graph, query):

    query = query.lower()
    wordsForSearch = []
    operation = ""

    if query.find("and") != -1 and query.find("or") == -1 and query.find("not") == -1:
        times = query.count("and")
        if times > 1:
            return False, None

        searching = query.split()
        operation = "and"

        for i in range(0, len(searching)):
            if searching[i] != "and":
                wordsForSearch.append(searching[i])

    elif query.find("and") == -1 and query.find("or") != -1 and query.find("not") == -1:
        times = query.count("or")
        if times > 1:
            return False, None

        searching = query.split()
        operation = "or"

        for i in range(0, len(searching)):
            if searching[i] != "or":
                wordsForSearch.append(searching[i])

    elif query.find("and") == -1 and query.find("or") == -1 and query.find("not") != -1:
        times = query.count("not")
        if times > 1:
            return False, None

        searching = query.split()
        operation = "not"
        for i in range(0, len(searching)):
            if searching[i] != "not":
                wordsForSearch.append(searching[i])

    elif query.find("and") == -1 and query.find("or") == -1 and query.find("not") == -1:

        searching = query.split()

        if len(searching) > 2:
            return False, None


        for i in range(0, len(searching)):
            wordsForSearch.append(searching[i])
    else:
        return False, None

    if len(wordsForSearch) > 2:
        return False, None

    if len(wordsForSearch) == 1:
        list1 = mySet()

        if operation == "not":
            for keys in globals.allFiles.keys():
                list1.add(keys)

            list2, list3 = findLists(graph, wordsForSearch[0], wordsForSearch[1])
            value = callOp(list1, list2, operation)

        elif operation == "or":
            list1, list2 = findLists(graph, wordsForSearch[0], wordsForSearch[1])
            return True, list1

        elif operation == "and":
            list1, list2 = findLists(graph, wordsForSearch[0], wordsForSearch[1])
            return True, list1

    else:
        print (wordsForSearch)
        list1, list2 = findLists(graph, wordsForSearch[0], wordsForSearch[1])
        value = callOp(list1, list2, operation)
        print(value[1].__len__())

    return value
