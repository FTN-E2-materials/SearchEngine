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

def getAllHtmlFiles(path):
    paths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html'):
                p = root + "/" + file
                paths.append(p)
                print(p)
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

    print ("Starting search")


if __name__ == '__main__':
    start_time = time.time()
    globals.root = "test-skup"
    # random path just for the start
    # globals.givenDir = raw_input("Unesite zeljeni direktorijum: ")

    graph = Graph()

    getAllHtmlFiles(globals.root)
    print (time.time() - start_time)

    test = input("Unesite upit: ")

    # check if user wants to exit (put some random key for exiting

    globals.givenWord = test
    startingSearch(globals.givenWord)
