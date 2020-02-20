from DataStructures.vertex import Vertex
from Other import globals

class Graph:
    def __init__(self):
        self.graph = {}

    def addTo(self, name, links, words):
        globals.allFiles[name] = Vertex(name, words)

        self.graph[name] = links


        # TODO: implement rest
