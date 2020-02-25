from Other import globals
from Other.colors import colors
from SearchParse.findFiles import *
from SearchParse.operations import *
from DataStructures.mySet import mySet
from DataStructures.stack import Stack
from DataStructures.parseTree import *
from Rang.countCost import *

# ORDINARY QUERY

def parseQueryOrdinary(query):

    query = query.lower()
    wordsForSearch = []
    operation = ""

    # validation

    if query.find("and") != -1 and query.find("or") == -1 and query.find("not") == -1:
        times = query.count("and")
        if times > 1:
            print(colors.RED + "Only one operator is allowed." + colors.END)
            return False, None

        searching = query.split()
        operation = "and"

        if searching[0] == "and" or searching[-1] == "and":
            print(colors.RED + "Expression can not start or end with an operator." + colors.END)
            return False, None

        for i in range(0, len(searching)):
            if searching[i] != "and":
                wordsForSearch.append(searching[i])

    elif query.find("and") == -1 and query.find("or") != -1 and query.find("not") == -1:
        times = query.count("or")
        if times > 1:
            print(colors.RED + "Only one operator is allowed." + colors.END)
            return False, None

        searching = query.split()
        operation = "or"

        if searching[0] == "or" or searching[-1] == "or":
            print(colors.RED + "Expression can not start or end with an operator." + colors.END)
            return False, None

        for i in range(0, len(searching)):
            if searching[i] != "or":
                wordsForSearch.append(searching[i])

    elif query.find("and") == -1 and query.find("or") == -1 and query.find("not") != -1:
        times = query.count("not")
        if times > 1:
            print(colors.RED + "Only one operator is allowed." + colors.END)
            return False, None

        searching = query.split()
        operation = "not"

        if searching[-1] == "not":
            print(colors.RED + "Expression can not start or end with an operator." + colors.END)
            return False, None

        for i in range(0, len(searching)):
            if searching[i] != "not":
                wordsForSearch.append(searching[i])

        if len(wordsForSearch) > 1:
            if searching[0] == "not":
                print(colors.RED + "More than one operator!" + colors.END)
                return False, None

    elif query.find("and") == -1 and query.find("or") == -1 and query.find("not") == -1:
        searching = query.split()

        for i in range(0, len(searching)):
            wordsForSearch.append(searching[i])
    else:
        return False, None

    if not wordsForSearch:
        print(colors.RED + "No words for search." + colors.END)
        return False, None

    # STARTING SEARCH

    if len(wordsForSearch) == 1:
        list1 = mySet()

        if operation == "not":
            for keys in globals.listEl:
                list1.add(keys)

            list = findLists(wordsForSearch)
            value = callOp(list1, list[0], operation)

            if value[0]:
                resultSet = countCost(value[1], wordsForSearch)
                return value[0], resultSet
            else:
                return value

        elif operation == "or":
            return False, None

        elif operation == "and":
            return False, None

        elif operation == "":
            list = findLists(wordsForSearch)
            resultSet = countCost(list[0], wordsForSearch)
            return True, resultSet

    else:
        list = findLists(wordsForSearch)
        if len(list) == 2:
            list1 = list[0]
            list2 = list[1]
            value = callOp(list1, list2, operation)

            if value[0]:
                resultSet = countCost(value[1], wordsForSearch)
                return value[0], resultSet
            else:
                return value

        elif len(list) > 2:
            if operation == "":
                first = callOp(list[0], list[1], operation)
                for i in range(2, len(list), 1):
                    value = callOp(first[1], list[i], operation)
                    first = value

                if first[0]:
                    resultSet = countCost(first[1], wordsForSearch)
                    return first[0], resultSet
                else:
                    return first
            else:
                return False, None
