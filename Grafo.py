class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A=[]):
        self.N = N
        self.A = A

    def __str__(self):
        grafo_str = str()

        for i in range(len(self.N)):
            if(i < len(self.N) - 1):
                grafo_str += f'{self.N[i]}, '
            else:
                grafo_str += f'{self.N[i]}\n'

        for valor in self.A:
            grafo_str += f'Vértices: {valor[0]} -> Valor {valor[1]}\n'

        return grafo_str

    def busca_em_profundidade(self, vertice_inicial, vertice_final, visitados=None):
        if visitados is None:
            visitados = []
            resultado = str()

        if vertice_inicial in visitados:
            return
        else:
            visitados.append(vertice_inicial)

        if vertice_inicial == vertice_final:
            return vertice_final

        for item_aresta in self.A:
            aresta = item_aresta[0]
            peso = item_aresta[-1]
            if aresta[0] == vertice_inicial and aresta[-1] not in visitados:
                return f'{vertice_inicial} - {peso} - {self.busca_em_profundidade(aresta[-1], vertice_final, visitados)}'

            if aresta[-1] == vertice_inicial and aresta[0] not in visitados:
                return f'{vertice_inicial} - {peso} - {self.busca_em_profundidade(aresta[0], vertice_final, visitados)}'

        return resultado
