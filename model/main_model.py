from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._listaAlbum = []
        self._nodes = []
        self._edges = []
        self._grafo = nx.Graph()

        self.mappaAlbumId = {}
        self.mappaNodiId = {}

        # self.loadAlbum()

    # def loadAlbum(self):
    #     self._listaAlbum = DAO.getAllAlbums()
    #     for album in self._listaAlbum:
    #         self.mappaAlbumId[album.AlbumId] = album


    def buildGraph(self, durataMin):
        self._grafo.clear()

        self._nodes = []
        self._edges = []
        self.mappaNodiId = {}

        self._nodes = DAO.getAllNodes(durataMin)
        self._grafo.add_nodes_from(self._nodes)
        for nodo in self._nodes:
            self.mappaNodiId[nodo.AlbumId] = nodo
        self._edges = DAO.getAllEdges(self.mappaNodiId)
        self._grafo.add_edges_from(self._edges)

    def get_nodes(self):
        return list(self._grafo.nodes())

    def get_edges(self):
        return list(self._grafo.edges())   #data = True

    def get_num_of_nodes(self):
        return self._grafo.number_of_nodes()

    def get_num_of_edges(self):
        return self._grafo.number_of_edges()

    def infoComponenteConnessa(self, nodo):
        componenteConnessa = nx.node_connected_component(self._grafo, nodo)
        return len(componenteConnessa), self.durataTotCC(componenteConnessa)

    def durataTotCC(self, insiemeCC):
        # durata = 0
        # for cc in insiemeCC:
        #     durata += cc.durataTotale
        # return durata
        return sum([cc.durataTotale for cc in insiemeCC])



if __name__ == "__main__":
    model = Model()
    # for album in model._listaAlbum:
    #     print(album)

    model.buildGraph(60)
    mappa = {}
    for nodo in model.get_nodes():
        print(nodo)
        mappa[nodo.AlbumId] = nodo

    print(model.get_num_of_nodes())
    print(model.get_num_of_edges())
    dimensioneCC = model.infoDimensioneComponenteConnessa(mappa[259])
    print(dimensioneCC)

    # cc = nx.node_connected_component(model._grafo,mappa[259])
    # print(cc)