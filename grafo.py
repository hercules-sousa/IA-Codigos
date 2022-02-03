class Grafo:
    def __init__(self, vertices=None, arestas=None):
        self.vertices = vertices
        self.arestas = arestas

    def __str__(self):
        grafo_str = str()

        for i in range(len(self.vertices)):
            if i < len(self.vertices) - 1:
                grafo_str += f'{self.vertices[i]}, '
            else:
                grafo_str += f'{self.vertices[i]}\n'

        for valor in self.arestas:
            grafo_str += f'Vértices: {valor[0]} -> Valor {valor[1]}\n'

        return grafo_str

    def obter_vizinhos_e_pesos(self, vertice):
        resultado = list()

        for i in self.arestas:
            aresta = i[0].split('-')

            if aresta[0] == vertice:
                resultado.append([i[1], aresta[1]])
            elif aresta[1] == vertice:
                resultado.append([i[1], aresta[0]])

        return resultado

    def busca_em_largura(self, vertice_inicial, vertice_final):
        fila = list()

        fila.append([vertice_inicial])

        while fila:
            caminho = fila.pop(0)

            vertice = caminho[-1]

            if vertice == vertice_final:
                return caminho

            for vizinho_e_peso in self.obter_vizinhos_e_pesos(vertice):
                new_path = list(caminho)

                new_path += vizinho_e_peso
                fila.append(new_path)

        return

    def busca_em_profundidade(self, vertice_inicial, vertice_final, visitados=None):
        if visitados is None:
            visitados = list()

        if vertice_inicial not in visitados:
            visitados.append(vertice_inicial)

        if vertice_inicial == vertice_final:
            return [vertice_final]

        for i in self.arestas:
            aresta = i[0]
            vertice1 = i[0][0]
            vertice2 = i[0][-1]
            peso = str(i[1])
            if vertice1 not in visitados and vertice1 != vertice_inicial and vertice_inicial in aresta:
                caminho = self.busca_em_profundidade(vertice1, vertice_final, visitados)
                if caminho is not None:
                    return [vertice2, peso] + caminho
            elif vertice2 not in visitados and vertice2 != vertice_inicial and vertice_inicial in aresta:
                caminho = self.busca_em_profundidade(vertice2, vertice_final, visitados)
                if caminho is not None:
                    return [vertice1, peso] + caminho
        return None
