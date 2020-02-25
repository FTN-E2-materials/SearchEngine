from Other import globals
from Other.colors import colors
from SearchParse.findFiles import *
from SearchParse.operations import *
from DataStructures.mySet import mySet
from DataStructures.stack import Stack
from DataStructures.parseTree import *
from Rang.countCost import *

# COMPLEX QUERY PARSER

def isOperator(char):
    if char == "&" or char == "|" or char == "!":
        return True
    else:
        return False

def parseComplexQuery(givenWord):
    wordsForSearch = []
    givenWord = givenWord.replace(" ", "")
    givenWord = givenWord.lower()
    wordList = []

    if givenWord.count("(") != givenWord.count(")"):
        print(colors.RED + "Must have equal number of left and right parentheses." + colors.END)
        return False, None

    if givenWord[0] == "&" or givenWord[0] == "|":
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
            if givenWord[i+1] == "&" or givenWord[i+1] == "|":
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
            if isOperator(givenWord[i+1]):
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
            elif givenWord[i+1] == "&" or givenWord[i+1] == "|" or givenWord[i+1] == ")" or givenWord[i+1] == "(":
                pass
            else:
                wordList.append("||")

        elif givenWord[i] != "&" and givenWord[i] != "|":
            word += givenWord[i]

            if i == len(givenWord) - 1:
                wordList.append(word)
                wordsForSearch.append(word)

            elif givenWord[i+1] == "&" or givenWord[i+1] == "|" or givenWord[i+1] == "(" or givenWord[i+1] == ")" or givenWord[i+1] == "!":
                wordList.append(word)
                wordsForSearch.append(word)
                word = ""

                if givenWord[i+1] == "(":
                    wordList.append("||")

    print("Infix to postfix: ")
    postfix = toPostfix(" ".join(wordList))
    print(postfix)
    tree = createParseTree(postfix)
    
    resultSet = evaluateTree(tree)
    finalResultSet = countCost(resultSet, wordsForSearch)

    return True, finalResultSet

# prevodjenje u postfiksnu notaciju

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
