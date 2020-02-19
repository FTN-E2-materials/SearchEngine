import globals
from findFiles import *
from operations import *
from mySet import mySet

def parseQueryOrdinary(query):

    query = query.lower()
    wordsForSearch = []
    operation = ""

    if query.find("and") != -1 and query.find("or") == -1 and query.find("not") == -1:
        times = query.count("and")
        if times > 1:
            return False, None

        searching = query.split()
        operation = "and"

        if searching[0] == "and" or searching[-1] == "and":
            return False, None

        for i in range(0, len(searching)):
            if searching[i] != "and":
                wordsForSearch.append(searching[i])

    elif query.find("and") == -1 and query.find("or") != -1 and query.find("not") == -1:
        times = query.count("or")
        if times > 1:
            return False, None

        searching = query.split()
        operation = "or"

        if searching[0] == "or" or searching[-1] == "or":
            return False, None

        for i in range(0, len(searching)):
            if searching[i] != "or":
                wordsForSearch.append(searching[i])

    elif query.find("and") == -1 and query.find("or") == -1 and query.find("not") != -1:
        times = query.count("not")
        if times > 1:
            return False, None

        searching = query.split()
        operation = "not"

        if searching[-1] == "not":
            return False, None

        for i in range(0, len(searching)):
            if searching[i] != "not":
                wordsForSearch.append(searching[i])

    elif query.find("and") == -1 and query.find("or") == -1 and query.find("not") == -1:
        searching = query.split()

        for i in range(0, len(searching)):
            wordsForSearch.append(searching[i])
    else:
        return False, None

    if not wordsForSearch:
        return False, None

    if len(wordsForSearch) == 1:
        list1 = mySet()

        if operation == "not":
            for keys in globals.listEl:
                list1.add(keys)

            list = findLists(wordsForSearch)
            value = callOp(list1, list[0], operation)
            print(value[1].__len__())
            return value

        elif operation == "or":
            return False, None

        elif operation == "and":
            return False, None

        elif operation == "":
            list = findLists(wordsForSearch)
            return True, list[0]

    else:
        list = findLists(wordsForSearch)
        if len(list) == 2:
            list1 = list[0]
            list2 = list[1]
            value = callOp(list1, list2, operation)
            return value

        elif len(list) > 2:
            if operation == "":
                rem = len(list) % 2
                flag = False
                if rem == 1:
                    flag = True
                first = callOp(list[0], list[1], operation)
                for i in range(2, len(list), 1):
                    value = callOp(first[1], list[i], operation)
                    first = value

                return first
            else:
                return False, None
