import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = []
        self._edges = []
        self._idMap = {}

    def getAnni(self):
        return DAO.getAnni()

    def buildGraph(self, anno1, anno2):
        self._graph.clear()
        self._nodes = DAO.getAllCircuits()
        self._graph.add_nodes_from(self._nodes)

        self._idMap = {}
        for node in self._nodes:
            self._idMap[node.circuitId] = node

        self._edges = DAO.getArchi(anno1, anno2, self._idMap)
        for a in self._edges:
            self._graph.add_edge(a[0], a[1])

    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()

    def getGraphDetails(self):
        connComps = list(nx.connected_components(self._graph))
        connessa = connComps[0]
        res = []
        for c in connessa:
            res.append((c, self._getMaxEdge(c)))

        res.sort(key=lambda x: x[1], reverse=True)
        return res

    def _getMaxEdge(self, nodo):
        # val = 0
        # for i in self._graph.neighbors(nodo):
        #     if self._graph[nodo][i]["weight"]>val:
        #         val = self._graph[nodo][i]["weight"]
        #
        # return val
        #
        return max(self._graph.get_edge_data(nodo, i)['weight'] for i in self._graph.neighbors(nodo))

