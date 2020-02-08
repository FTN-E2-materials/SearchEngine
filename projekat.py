# -*- coding: utf-8 -*-
import re
import os
import time
import random
import sys

from HTMLParser import HTMLParser


class Parser(HTMLParser):
    """
    Parser HTML dokumenata

    Upotreba:
        parser = Parser()
        parser.parse(FILE_PATH)
    """

    def handle_starttag(self, tag, attrs):
        """
        Metoda beleži sadržaj href atributa

        Poziv metode vrši se implicitno prilikom nailaska na tag
        unutar HTML fajla. Ukoliko je u pitanju anchor tag, beleži
        se vrednost href atributa.

        Argumenti:
        - `tag`: naziv taga
        - `attrs`: lista atributa
        """
        if tag == 'a':
            # typecast da izbegnem looping
            attrs = dict(attrs)
            link = attrs['href']

            # ignoriši spoljnje linkove i uzmi u obzir samo html fajlove
            if not link.startswith('http'):
                # ukloni sekciju iz linka
                hash_index = link.rfind('#')
                if hash_index > -1:
                    link = link[:hash_index]

                if link.endswith('html') or link.endswith('htm'):
                    relative_path = os.path.join(self.path_root, link)
                    link_path = os.path.abspath(relative_path)
                    self.links.append(link_path)

    def handle_data(self, data):
        """
        Metoda beleži pronađene reči

        Poziv metode vrši se implicitno prilikom nailaska na sadržaj
        HTML elemenata. Sadržaj elementa se deli u reči koje se beleže
        u odgovarajuću listu.

        Argument:
        - `data`: dobijeni sadržaj elementa
        """
        stripped_text = re.sub('[\W]', ' ', data).split()
        if stripped_text:
            self.words.extend(stripped_text)

    def parse(self, path):
        """
        Metoda učitava sadržaj fajla i prosleđuje ga parseru

        Argument:
        - `path`: putanja do fajla
        """
        self.links = []
        self.words = []

        try:
            with open(path, 'r') as document:
                self.path_root = os.path.abspath(os.path.dirname(path))
                content = document.read()
                self.feed(content)

                # očisti duplikate
                self.links = list(set(self.links))

        except IOError as e:
            print(e)
        finally:
            return self.links, self.words


allFiles = {}
givenWord = ""
listEl = []
root = "" # my test root
words = []
start = ""
givenDir = "" # users wanted root

class Node:
    def __init__(self, letter = None, data = None, count = 0):
        self.letter = letter
        self.data = data
        self.children = dict()
        self.count = count

    def addChild(self, key, data = None):
        self.children[key] = Node(key, data)


class Trie:
    def __init__(self):
        self.head = Node()

    def add(self, wordForAdd):
        word = wordForAdd.lower()
        words.append(word)

        curr_node = self.head
        word_finish = True

        for i in range(len(word)):
            if word[i] in curr_node.children:
                curr_node = curr_node.children[word[i]]
            else:
                word_finish = False
                break

        if not word_finish:
            while i < len(word):
                curr_node.addChild(word[i])
                curr_node = curr_node.children[word[i]]
                i += 1

        curr_node.data = word
        curr_node.count += 1

    def isWord(self, wordForSearch):
        word = wordForSearch.lower()

        if word == '':
            return False
        if word is None:
            # should add error message
            print "Error"

        # starting from zero
        curr_node = self.head
        exists = True

        for letter in word:
            if letter in curr_node.children:
                curr_node = curr_node.children[letter]
            else:
                exists = False
                break
        if exists:
            if curr_node.data is None:
                exists = False

        return exists, current_node

class Vertex:
    # TODO: implement the rest of the vertex of the graph
    def __init__(self, name, words):
        self.wordTrie = self.getWords(words)

    def getWords(self, words):
        trie = Trie()
        for i in range(len(words)):
            trie.add(words[i])
        return trie


class Graph:

    def __init__(self):
        self.graph = {}

    def addTo(self, name, links, words):
        allFiles[name] = Vertex(name, words)
        # TODO: implement rest

def getAllHtmlFiles(path):
    paths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html'):
                p = root + "//" + file
                paths.append(p)
    parse(paths)

def parse(paths):
    global start
    parser = Parser()

    for i in range(len(paths)):
        parsed = parser.parse(paths[i])
        graph.addTo(paths[i], parsed[0], parsed[1])

    start = paths[0]

def startingSearch():
    # TODO:
    # function for starting
    # it will call all needed functions

    print "Starting search"


if __name__ == '__main__':
    start_time = time.time()
    root = "//home//jelena//Desktop//PythonProjekat//test-skup//files"
    # random path just for the start
    # givenDir = raw_input("Unesite zeljeni korenski direktorijum: ")

    graph = Graph()

    getAllHtmlFiles(root)
    print time.time() - start_time

    test = raw_input("Unesite upit: ")

    # check if user wants to exit (put some random key for exiting)

    givenWord = test

    startingSearch()
