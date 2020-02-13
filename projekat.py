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
    paths = []
    print("This may take a while... ")
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html'):
                p = root + "/" + file
                paths.append(p)
                #print(p)
    if not paths:
        print("There are no html files in the directory!")
    else:
        parse(paths)

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('\r[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

def parse(paths):

    parser = Parser()

    for i in range(len(paths)):
        parsed = parser.parse(paths[i])
        progress(i, len(paths), status='')
        globals.listEl.append(paths[i])
        addToTrie(parsed[1], paths[i])

    progress(len(paths), len(paths), status='') # da bi stiglo do 100%
    globals.start = paths[0]

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
    print (colors.GREEN + "Time elapsed:", str(time.time() - start_time) + colors.END)

    print("For exiting insert 'x'")

    while True:

        upit = input("Enter your query: ")

        if upit == "x" or upit == "X":
            print(colors.RED + "See ya soon!" + colors.END)
            exit()

        globals.givenWord = upit
        startingSearch(globals.givenWord)

    # check if user wants to exit (put some random key for exiting
