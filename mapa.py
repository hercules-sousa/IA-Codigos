from typing import Type
from grafo import Grafo
from interfaces.leitor import LeitorInterface


class Mapa:
    def __init__(self, nome_mapa, leitor: Type[LeitorInterface] = None):
        self.nome_mapa = nome_mapa
        self.leitor = leitor
        self.mapaGrafo = Grafo()

    def setLeitor(self, leitor: Type[LeitorInterface]):
        self.leitor = leitor

    def construir_grafo_mapa(self, arquivo) -> None:
        dados = self.leitor.obter_dados(arquivo)
        for aresta in dados:
            self.mapaGrafo.adicionarAresta(aresta)
