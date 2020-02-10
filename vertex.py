from trie import Trie
import globals

class Vertex:
    # TODO: implement the rest of the vertex of the graph
    def __init__(self, name, words):
        self.wordTrie = self.getWords(words)

    def getWords(self, words):
        trie = Trie()
        for i in range(len(words)):
            trie.add(words[i])
        return trie
