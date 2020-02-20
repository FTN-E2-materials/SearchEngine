from Other import globals
from Other.colors import colors
from SearchParse.findFiles import *
from SearchParse.operations import *
from DataStructures.mySet import mySet
from DataStructures.stack import Stack
from DataStructures.parseTree import *

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
def isOperatorParen(char):
    if char == "&" or char == "|" or char == "!":
        return True
    else:
        return False
def parseComplexQuery(givenWord):
    originalGivenWord = givenWord
    givenWord = givenWord.replace(" ", "")
    givenWord = givenWord.lower()
    wordList = []

    if givenWord.count("(") != givenWord.count(")"):
        print(colors.RED + "Must have equal number of left and right parentheses." + colors.END)
        return False, None

    if givenWord[0] == "&&" or givenWord[0] == "||":
        print(colors.RED + "Query can not start with AND/OR operator." + colors.END)
        return False, None

    if givenWord[-1] == "!" or givenWord[-1] == "&" or givenWord[-1] == "|":
        print(colors.RED + "Query can not end with an operator." + colors.END)
        return False, None

    timesAnd = givenWord.count("&")
    timesOr = givenWord.count("|")
    rem1 = timesAnd % 2
    rem2 = timesOr % 2

    if rem1 != 0 or rem2 != 0:
        print(colors.RED + "Invalid operator (only && and || are allowed)." + colors.END)
        return False, None

    word = ""
    flag = False

    for i in range(0, len(givenWord), 1):
        num = 0


        if givenWord[i] == "(":
            if givenWord[i+1] == "&&" or givenWord[i+1] == "||":
                print(colors.RED + "Word before an operator is needed." + colors.END)
                return False, None
            else:
                wordList.append("(")
                flag = True
        elif givenWord[i] == "&" and givenWord[i+1] == "&":
            num += 1
            if givenWord[i+2] == "|" or givenWord[i+2] == "&":
                print(colors.RED + "Invalid operator." + colors.END)
                return False, None
            else:
                wordList.append("&&")
                flag = True
        elif givenWord[i] == "|" and givenWord[i+1] == "|":
            num += 1
            if givenWord[i+2] == "&" or givenWord[i+2] == "|":
                print(colors.RED + "Invalid operator." + colors.END)
                return False, None
            else:
                wordList.append("||")
                flag = True
        elif givenWord[i] == "!":
            if isOperatorParen(givenWord[i+1]):
                print(colors.RED + "Invalid operator." + colors.END)
                return False, None
            else:
                wordList.append("!")
                flag = True
        elif givenWord[i] == ")":
            wordList.append(")")
            flag = True
            if i == len(givenWord) - 1:
                pass
            elif givenWord[i+1] == "&" or givenWord[i+1] == "|" or givenWord[i+1] == ")" or givenWord[i+1] == "(" or givenWord[i+1] == "!":
                pass
            else:
                wordList.append("||")
        elif givenWord[i] != "&" and givenWord[i] != "|":
            word += givenWord[i]
            print(givenWord[i])
            if i == len(givenWord) - 1:
                wordList.append(word)
            elif givenWord[i+1] == "&" or givenWord[i+1] == "|" or givenWord[i+1] == ")" or givenWord[i+1] == "(" or givenWord[i+1] == "!":
                wordList.append(word)
                flag = False
                word = ""

    postfix = toPostfix(" ".join(wordList))
    print(postfix)
    print(postfix)
    tree = createParseTree(postfix)
    resultSet = evaluateTree(tree)
    return True, resultSet

def toPostfix(query):

    precedence = {}
    precedence['!'] = 4
    precedence['&&'] = 3
    precedence['||'] = 2
    precedence['('] = 1

    opstack = Stack()
    postfix = []
    tokens = query.split()
    print(tokens)
    wordsInARow = 0

    for token in tokens:
        if token == "(":
            opstack.push(token)
            wordsInARow = 0
        elif token == ")":
            while True:
                temp = opstack.pop()
                if temp is None or temp == "(":
                    break
                else:
                    postfix.append(temp)
            wordsInARow = 0
        elif token == "&&" or token == "||" or token == "!":
            print(token)
            while (not opstack.isEmpty() and precedence[opstack.peek()] >= precedence[token]):
                postfix.append(opstack.pop())
            opstack.push(token)
            wordsInARow = 0
        else: # rec za pretragu
            postfix.append(token)
            if wordsInARow >= 1:
                postfix.append("||")
            wordsInARow += 1

    while not opstack.isEmpty():
        postfix.append(opstack.pop())

    return " ".join(postfix)
