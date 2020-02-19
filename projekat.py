# -*- coding: utf-8 -*-

import re
import os
import time
import random
import sys
import globals
import glob

from parser import Parser
from graph import Graph
from node import Node
from vertex import Vertex
from parseQuery import *
from trie import Trie
from printPages import *
from colors import colors
from progressbar import *

def getAllHtmlFiles(path):

    print("This may take a while... ")
    parser = Parser()

    # files = glob.glob(path + '/**/*.html', recursive = True)
    i = 0

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

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html'):
                i += 1
                p = os.path.join(root, file)
                globals.listEl.append(p)
                parsed = parser.parse(p)
                addToTrie(parsed[1], p)
            # ovde dodavanje u graf ide

    if not globals.listEl:
        print("There are no html files in the directory!")

def addToTrie(words, path):
    for i in range(len(words)):
        globals.trie.add(path, words[i])

def startingSearch(givenWord, flag):
    if flag == 1:
        returnValue = parseQueryOrdinary(givenWord)
    else:
        returnValue = parseComplexQuery(givenWord)

    if not returnValue[0]:
        print(colors.RED + "Incorrect query!" + colors.END)
        print(colors.RED + "Try ['word'] 'operator' ['word']" + colors.END)
    elif len(returnValue[1]) == 0:
        print(colors.RED + "No html page found." + colors.END)
    else:
        # ovde ce se pre printovnja pozivati funkcija za rangiranje rezultata
        # i sortiranje takvih stranica

        printPages(returnValue[1])

if __name__ == '__main__':
    start_time = time.time()

    globals.root = input("Enter path for loading: ")
    # graph = Graph()
    getAllHtmlFiles(globals.root)

    print()
    print (colors.GREEN + "Time elapsed: ", str(time.time() - start_time) + colors.END)


    while True:
        print("1. Regular search (maximum one operator and, or, not).")
        print("2. Advanced search.")
        print("'X' or 'x' for exiting.")

        srch = input()

        if srch == "x" or srch == "X":
            print(colors.BLUE + "See ya soon!" + colors.END)
            exit()
        if srch == "1" or srch == "2":
            upit = input("Enter your query: ")
            startingSearch(upit, int(srch))
        else:
            print("Invalid number!")
