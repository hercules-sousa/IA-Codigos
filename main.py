from grafo import Grafo
from leitores.leitorTxt import LeitorTxt
from mapaEstado import MapaEstado
import os

'''
grafo1 = Grafo(list("ABCD"), [
    ["A-B", 12],
    ["B-C", 15],
    ["A-C", 1],
    ["C-D", 2]
])

print(grafo1.busca_em_profundidade("A", "C"))
print(grafo1.busca_em_largura("A", "C"))

grafo2 = Grafo(list("ABCD"), [
    ["A-B", 4],
    ["A-C", 1],
    ["C-D", 2],
])

print(grafo2.busca_em_profundidade("A", "D"))
print(grafo2.busca_em_largura("A", "D"))

grafo3 = Grafo(list("ABC"), [
    ["A-A", 12],
    ["A-B", 4],
    ["B-C", 5],
])

print(grafo3.busca_em_profundidade("A", "C"))
print(grafo3.busca_em_largura("A", "C"))
print(grafo3.busca_em_profundidade("C", "A"))
print(grafo3.busca_em_largura("C", "A"))

grafo4 = Grafo(list("ABCDEFG"), [
    ["A-A", 10],
    ["A-B", 4],
    ["B-B", 7],
    ["B-C", 1],
    ["B-D", 8],
    ["D-E", 9],
    ["E-F", 5],
    ["E-G", 4],
])
print(grafo4.busca_em_largura("C", "G"))

print(grafo4.busca_em_profundidade("C", "G"))
'''

nome_pasta = os.path.dirname(__file__)
caminho_txt = os.path.join(nome_pasta, 'arquivos/paraiba.txt')
with open(caminho_txt) as arquivo:
    leitorTxt = LeitorTxt()
    mapaEstado = MapaEstado("Paraíba", leitorTxt)
    mapaEstado.construir_grafo_estado(arquivo)
    print("Exibindo mapa:")
    print(mapaEstado.mapaGrafo)

    print("Caminho da busca em profundidade")
    print(mapaEstado.mapaGrafo.busca_em_profundidade("Campina Grande", "Montadas"))
    print(mapaEstado.mapaGrafo.busca_em_largura("Campina Grande", "Montadas"))
    print(mapaEstado.mapaGrafo.busca_a_estrela("Campina Grande", "Montadas", "Campina Grande"))

arquivo.close()
