class VerticeInvalidoException(Exception):
    pass

class Grafo:
    def __init__(self, vertices=None, arestas=None):
        if arestas is None:
            arestas = []
        if vertices is None:
            vertices = []
        self.vertices = vertices
        self.arestas = arestas

    def __str__(self):
        grafo_str = str()

        for i in range(len(self.vertices)):
            if i < len(self.vertices) - 1:
                grafo_str += f'{self.vertices[i]}, '
            else:
                grafo_str += f'{self.vertices[i]}\n\n'

        for valor in self.arestas:
            grafo_str += f'Cidades: {valor[0]} -> distância {valor[1]}\n'

        return grafo_str

    def verticeValido(self, vertice):
        if vertice in self.vertices:
            return True
        return False

    def adicionarAresta(self, aresta):
        self.arestas.append(aresta)
        for cidade in aresta[0].split("-"):
            if cidade not in self.vertices:
                self.vertices.append(cidade)

    def busca_a_estrela(self, vertice_inicial, vertice_final, heuristica):
        if not self.verticeValido(vertice_inicial):
            raise VerticeInvalidoException(vertice_inicial)
        if not self.verticeValido(vertice_final):
            raise VerticeInvalidoException(vertice_final)

        vertices_abertos = [vertice_inicial]
        vertices_fechados = list()

        distancia_atual = {
            vertice_inicial: 0
        }

        parents = {
            vertice_inicial: [vertice_inicial, 0]
        }

        while len(vertices_abertos) > 0:
            node = None

            for v in vertices_abertos:
                if node is None or distancia_atual[v] + heuristica[v] < distancia_atual[node] + heuristica[node]:
                    node = v

            if node is None:
                return

            if node == vertice_final:
                caminho = list()

                while parents[node][0] != node:
                    caminho += [node, parents[node][1]]
                    node = parents[node][0]

                caminho.append(vertice_inicial)

                caminho.reverse()

                return caminho

            for item in self.obter_vizinhos_e_pesos(node):
                peso, vertice = item

                if vertice not in vertices_abertos and vertice not in vertices_fechados:
                    vertices_abertos.append(vertice)
                    parents[vertice] = [node, peso]
                    distancia_atual[vertice] = distancia_atual[node] + peso
                else:
                    if distancia_atual[vertice] > distancia_atual[node] + peso:
                        distancia_atual[vertice] = distancia_atual[node] + peso
                        parents[vertice] = [node, peso]

                        if vertice in vertices_fechados:
                            vertices_fechados.remove(vertice)
                            vertices_abertos.append(vertice)

            vertices_abertos.remove(node)
            vertices_fechados.append(node)

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
        if not self.verticeValido(vertice_inicial):
            raise VerticeInvalidoException(vertice_inicial)
        if not self.verticeValido(vertice_final):
            raise VerticeInvalidoException(vertice_final)

        fila = list()

        fila.append([vertice_inicial])

        while fila:
            caminho = fila.pop(0)

            vertice = caminho[-1]

            if vertice == vertice_final:
                return caminho

            for vizinho_e_peso in self.obter_vizinhos_e_pesos(vertice):
                novo_caminho = list(caminho)

                novo_caminho += vizinho_e_peso
                fila.append(novo_caminho)

        return

    def busca_em_profundidade(self, vertice_inicial, vertice_final, visitados=None):
        if visitados is None:
            if not self.verticeValido(vertice_inicial):
                raise VerticeInvalidoException(vertice_inicial)
            if not self.verticeValido(vertice_final):
                raise VerticeInvalidoException(vertice_final)

            visitados = list()

        if vertice_inicial not in visitados:
            visitados.append(vertice_inicial)

        if vertice_inicial == vertice_final:
            return [vertice_final]

        for i in self.arestas:
            aresta = i[0]
            vertice1 = aresta.split("-")[0]
            vertice2 = aresta.split("-")[-1]
            peso = i[1]
            if vertice1 not in visitados and vertice1 != vertice_inicial and vertice_inicial in aresta:
                caminho = self.busca_em_profundidade(vertice1, vertice_final, visitados)
                if caminho is not None:
                    return [vertice2, peso] + caminho
            elif vertice2 not in visitados and vertice2 != vertice_inicial and vertice_inicial in aresta:
                caminho = self.busca_em_profundidade(vertice2, vertice_final, visitados)
                if caminho is not None:
                    return [vertice1, peso] + caminho
        return None
