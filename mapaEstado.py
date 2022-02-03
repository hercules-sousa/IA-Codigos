from typing import Type
from grafo import Grafo
from interfaces.leitor import LeitorInterface


class MapaEstado:
    def __init__(self, nomeEstado):
        self.nomeEstado = nomeEstado
        self.estado = Grafo()

    def construir_grafo_estado(self, leitor: Type[LeitorInterface], arquivo):
        print(arquivo)
        leitor.obter_dados()
