from trie import Trie
import globals

class Vertex:
    # TODO: implement the rest of the vertex of the graph
    def __init__(self, name, words):
        self.name = name
        self.words = words
        self.wordTrie = self.getWords(words)
        self.me = 0 # koliko puta ja sadrzim rec
        self.myLinks = 0 # koliko puta moji linkovi sadrze rec
        self.links = 0  # koliko ukupno linkova sadrzi rec
        self.rank = 0
        self.num = 0

    def getWords(self, words):
        trie = Trie()
        for i in range(len(words)):
            trie.add(words[i])
        return trie
        
    def countRank(self):
        # TODO: implement self rank
        pass
