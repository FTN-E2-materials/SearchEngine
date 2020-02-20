from Other import globals

class Node:
    def __init__(self, letter = None, data = None, count = 0):
        self.letter = letter
        self.data = data
        self.children = dict()
        self.count = count
        self.wordShowing = dict()

    def addChild(self, key, data = None):
        self.children[key] = Node(key, data)
