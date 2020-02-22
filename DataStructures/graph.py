
from Other import globals

class Graph:
    def __init__(self):
        self._incoming = {}
        self._outgoing = {}

    def addVertex(self, vertex):
        self._outgoing[vertex] = []
        if vertex not in self._incoming.keys():
            self._incoming[vertex] = []
            
    def addEdge(self, vertex, vertexToAppend):
        self._outgoing[vertex].append(vertexToAppend)
        if vertexToAppend not in self._incoming.keys():
            self._incoming[vertexToAppend] = []

        self._incoming[vertexToAppend].append(vertex)
    def addPage(self, vertex, links):

        self.addVertex(vertex)
        for link in links:
            self.addEdge(vertex, link)

    def get_incoming(self, vertex):
        return list(self._incoming[vertex])

    def get_outgoing(self, vertex):
        return list(self._outgoing[vertex])

    def vertices(self):
        return list(self._outgoing.keys())
