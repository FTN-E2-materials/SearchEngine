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

def getAllHtmlFiles(path):
    paths = []
    print("Files found: ")
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html'):
                p = root + "/" + file
                paths.append(p)
                print(p)
    if not paths:
        print("There are no html files in the directory!")
    else:
        parse(paths)

def parse(paths):

    parser = Parser()

    for i in range(len(paths)):
        parsed = parser.parse(paths[i])
        graph.addTo(paths[i], parsed[0], parsed[1])

    globals.start = paths[0]

def startingSearch(givenWord):
    # TODO:
    # function for starting
    # it will call all needed functions

    returnValue = parseQueryOrdinary(graph, globals.givenWord)

    if not returnValue[0]:
        print("Incorrect query!")
        print("Try ['word'] 'operator' ['word']")
    else:
        printPages(returnValue[1])
        
if __name__ == '__main__':
    start_time = time.time()
    globals.root = "test-skup"

    # random path just for the start
    # globals.givenDir = raw_input("Unesite zeljeni direktorijum: ")

    graph = Graph()
    getAllHtmlFiles(globals.root)
    print (time.time() - start_time)

    globals.givenWord = input("Enter your query: ")

    startingSearch(globals.givenWord)


    # check if user wants to exit (put some random key for exiting
