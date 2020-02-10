import globals

def parseQueryOrdinary(query):

    query = query.lower()

    if query.find("and") != -1 and query.find("or") == -1 and query.find("not") == -1:
        times = query.count("and")
        if times > 1:
            return False

        searching = query.split()
        wordsForSearch = []
        for i in range(0, len(searching)):
            if searching[i] != "and":
                wordsForSearch.append(searching[i])

        print(wordsForSearch)
        # call intersection search


    elif query.find("and") == -1 and query.find("or") != -1 and query.find("not") == -1:
        times = query.count("or")
        if times > 1:
            return False

        searching = query.split()
        wordsForSearch = []
        for i in range(0, len(searching)):
            if searching[i] != "or":
                wordsForSearch.append(searching[i])

        print(wordsForSearch)

    elif query.find("and") == 1 and query.find("or") == -1 and query.find("not") != -1:
        times = query.count("not")
        if times > 1:
            return False

        searching = query.split()
        wordsForSearch = []
        for i in range(0, len(searching)):
            if searching[i] != "not":
                wordsForSearch.append(searching[i])

        print(wordsForSearch)

    elif query.find("and") == 1 and query.find("or") == -1 and query.find("not") == -1:

        searching = query.split()

        if len(searching) > 2:
            return False

        wordsForSearch = []
        for i in range(0, len(searching)):
            wordsForSearch.append(searching[i])

        print(wordsForSearch)
