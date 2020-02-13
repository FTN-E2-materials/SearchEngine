# -*- coding: utf-8 -*-

import re
import os
import time
import random
import sys
import globals

from parser import Parser
from graph import Graph
from node import Node
from vertex import Vertex
from parseQuery import *
from trie import Trie
from printPages import *
from colors import colors

def getAllHtmlFiles(path):

    print("This may take a while... ")
    parser = Parser()
    i = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html'):
                i += 1
                p = root + "/" + file
                globals.listEl.append(p)
                parsed = parser.parse(p)
                addToTrie(parsed[1], p)

    if not globals.listEl:
        print("There are no html files in the directory!")

def addToTrie(words, path):
    for i in range(len(words)):
        globals.trie.add(path, words[i])

def startingSearch(givenWord):
    returnValue = parseQueryOrdinary(globals.givenWord)

    if not returnValue[0]:
        print(colors.RED + "Incorrect query!" + colors.END)
        print(colors.RED + "Try ['word'] 'operator' ['word']" + colors.END)
    elif len(returnValue[1]) == 0:
        print(colors.RED + "No html page found." + colors.END)
    else:
        printPages(returnValue[1])

if __name__ == '__main__':
    start_time = time.time()

    globals.root = input("Enter path for loading: ")
    # graph = Graph()
    getAllHtmlFiles(globals.root)

    print()
    print (colors.GREEN + "Time elapsed: ", str(time.time() - start_time) + colors.END)

    print("For exiting insert 'x' or 'X'")

    while True:

        upit = input("Enter your query: ")

        if upit == "x" or upit == "X":
            print(colors.BLUE + "See ya soon!" + colors.END)
            exit()

        globals.givenWord = upit
        startingSearch(globals.givenWord)

    # check if user wants to exit (put some random key for exiting
