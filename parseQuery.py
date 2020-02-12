import globals
from findFiles import *
from operations import *

def parseQueryOrdinary(graph, query):

    query = query.lower()
    wordsForSearch = []
    operation = ""

    if query.find("and") != -1 and query.find("or") == -1 and query.find("not") == -1:
        times = query.count("and")
        if times > 1:
            return False

        searching = query.split()
        operation = "and"

        for i in range(0, len(searching)):
            if searching[i] != "and":
                wordsForSearch.append(searching[i])

    elif query.find("and") == -1 and query.find("or") != -1 and query.find("not") == -1:
        times = query.count("or")
        if times > 1:
            return False

        searching = query.split()
        operation = "or"

        for i in range(0, len(searching)):
            if searching[i] != "or":
                wordsForSearch.append(searching[i])

    elif query.find("and") == -1 and query.find("or") == -1 and query.find("not") != -1:
        times = query.count("not")
        if times > 1:
            return False

        searching = query.split()
        operation = "not"
        for i in range(0, len(searching)):
            if searching[i] != "not":
                wordsForSearch.append(searching[i])

    elif query.find("and") == -1 and query.find("or") == -1 and query.find("not") == -1:

        searching = query.split()

        if len(searching) > 2:
            return False


        for i in range(0, len(searching)):
            wordsForSearch.append(searching[i])
    else:
        return False

    if len(wordsForSearch) < 2 and len(wordsForSearch) > 2:
        return False


    list1, list2 = findLists(graph, wordsForSearch[0], wordsForSearch[1])
    print(list1.__len__(), list2.__len__(), operation)
    value = callOp(list1, list2, operation)
    return value
