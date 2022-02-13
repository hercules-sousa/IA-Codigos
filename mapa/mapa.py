from typing import Type
from mapa.grafo import Grafo
from interfaces.leitor import LeitorInterface


class Mapa:
    def __init__(self, nome_mapa, leitor: Type[LeitorInterface] = None):
        self.nome_mapa = nome_mapa
        self.leitor = leitor
        self.mapa_grafo = Grafo()

    def set_leitor(self, leitor: Type[LeitorInterface]):
        self.leitor = leitor

    def construir_grafo_mapa(self, arquivo) -> None:
        dados = self.leitor.obter_dados(arquivo)
        for aresta in dados:
            self.mapa_grafo.adicionar_aresta(aresta)

    def busca_em_profundidade(self, cidade_origem, cidade_destino):
        return self.mapa_grafo.busca_em_profundidade(cidade_origem, cidade_destino)

    def busca_em_largura(self, cidade_origem, cidade_destino):
        return self.mapa_grafo.busca_em_largura(cidade_origem, cidade_destino)

    def busca_a_estrela(self, cidade_origem, cidade_destino, heuristica):
        return self.mapa_grafo.busca_a_estrela(cidade_origem, cidade_destino, heuristica)