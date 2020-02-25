import re
import os
import time
import random
import glob
import sys

from Other import globals
from DataStructures.parser import Parser
from DataStructures.graph import Graph
from DataStructures.node import Node
from SearchParse.parseQuery import *
from SearchParse.parseComplexQuery import *
from DataStructures.trie import Trie
from Other.printPages import *
from Other.colors import colors

def getAllHtmlFiles(path):
    start_time = time.time()
    print("This may take a while... ")
    parser = Parser()

    # files = glob.glob(path + '/**/*.html', recursive = True)
    # i = 0

    '''
    for file in files:
        parsed = parser.parse(file)
        for word in parsed[1]:
            globals.trie.add(word, file)
        i += 1
        progress(i, len(files), status = '')
        #globals.listEl.append(file)
    progress(len(files), len(files), status = '')
    '''

# zbog uporedjivanja brzine
# na linuxu radi brze os.walk
# zato je i ostavljen

    if not os.path.isabs(path):
        path = os.path.abspath(path)
    else:
        pass
        
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html') or file.endswith('.htm'):
                p = os.path.join(root, file)
                #print(p)
                #p = os.path.abspath(p)
                #print(p)
                globals.listEl.append(p)
                parsed = parser.parse(p)
                globals.graph.addPage(p, parsed[0])
                addToTrie(parsed[1], p)

    print (colors.GREEN + "Time elapsed: ", str(time.time() - start_time) + colors.END)
    if not globals.listEl:
        print("There are no html files in the directory!")
        return False
    else:
        return True

def addToTrie(words, path):
    for i in range(len(words)):
        globals.trie.add(path, words[i])

def startingSearch(givenWord, flag):
    startSearch = time.time()
    if flag == 1:
        returnValue = parseQueryOrdinary(givenWord)
    else:
        returnValue = parseComplexQuery(givenWord)

    if not returnValue[0]:
        if flag == 1:
            print(colors.RED + "Incorrect ordinary query!" + colors.END)
            print(colors.RED + "Try ['word'] 'operator' ['word']" + colors.END)
        else:
            print(colors.RED + "Incorrect complex query" + colors.END)
            print(colors.RED + "Try ['operator']['lparen']['words' ... ]['rparen']..." + colors.END)
    elif len(returnValue[1]) == 0:
        print(colors.RED + "No html page found." + colors.END)
    else:
        print(colors.GREEN + "Time elapsed with search: " + str(time.time() - startSearch) + colors.END)
        printPages(returnValue[1])


if __name__ == '__main__':
    done = True
    print("If you want to exit at any time type x or X.")

    while done:
        globals.root = input("Enter path for loading: ")
        if globals.root == "x" or globals.root == "X":
            exit()

        found = getAllHtmlFiles(globals.root)
        if found:
            done = False
        else:
            done = True

    while True:
        print("1. Regular search (maximum one operator and, or, not).")
        print("2. Advanced search.")
        print("'X' or 'x' for exiting.")

        srch = input("Your input: ")

        if srch == "x" or srch == "X":
            print(colors.BLUE + "See ya soon!" + colors.END)
            exit()
        if srch == "1" or srch == "2":
            upit = input("Enter your query: ")
            startingSearch(upit, int(srch))
        else:
            print("Invalid number!")
