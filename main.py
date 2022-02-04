import os
from mapaEstado import MapaEstado
from leitores.leitorTxt import LeitorTxt

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
    print()
    print("Caminho da busca em largura")
    print(mapaEstado.mapaGrafo.busca_em_largura("Campina Grande", "Montadas"))
    print()
    print("Caminho da busca em estrela")
    print(mapaEstado.mapaGrafo.busca_a_estrela("Campina Grande", "Montadas", "Campina Grande"))

arquivo.close()
