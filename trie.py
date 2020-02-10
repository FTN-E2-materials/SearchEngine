from node import Node
import globals

class Trie:
    def __init__(self):
        self.head = Node()

    def add(self, wordForAdd):
        word = wordForAdd.lower()
        globals.words.append(word)

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
            print ("Error")

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
