from DataStructures.node import Node
from Other import globals

class Trie:
    def __init__(self):
        self.head = Node()

    def add(self, page, wordForAdd):
        word = wordForAdd.lower()
        # globals.words.append(word)
        curr_node = self.head
        j = 0
        for char in word:
            if char not in curr_node.children:
                curr_node.addChild(char)
            curr_node = curr_node.children[char]

        if page not in curr_node.wordShowing.keys():
            j = 0
        else:
            j = curr_node.wordShowing[page]

        curr_node.data = word
        curr_node.count += 1
        curr_node.wordShowing[page] = j + 1

    def isWord(self, wordForSearch):
        word = wordForSearch.lower()

        if word == '':
            return False, None
        if word is None:
            # should add error message
            print ("Error")
            return False, None

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

        return exists, curr_node
