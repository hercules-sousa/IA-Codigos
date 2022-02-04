from typing import Type
from grafo import Grafo
from interfaces.leitor import LeitorInterface


class MapaEstado:
    def __init__(self, nomeEstado, leitor: Type[LeitorInterface]):
        self.nomeEstado = nomeEstado
        self.leitor = leitor
        self.estado = Grafo()

    def construir_grafo_estado(self,  arquivo) -> None:
        print(arquivo)
        dados = self.leitor.obter_dados()
        print(dados)
