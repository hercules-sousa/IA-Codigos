import os
from mapaEstado import MapaEstado
from leitores.leitorTxt import LeitorTxt
from leitores.leitorJson import LeitorJson

mapaEstado = MapaEstado("Paraíba")

print("Trabalhando com arquivo TXT")
nomePasta = os.path.dirname(__file__)
caminhoTxt = os.path.join(nomePasta, 'arquivos/paraiba.txt')
with open(caminhoTxt) as arquivoTxt:
    leitorTxt = LeitorTxt()
    mapaEstado.setLeitor(leitorTxt)
    mapaEstado.construir_grafo_estado(arquivoTxt)

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
    print()

arquivoTxt.close()

print("Trabalhando com arquivo JSON")
caminho_json = os.path.join(nomePasta, 'arquivos/paraiba.json')
with open(caminho_json) as arquivoJson:
    leitorJson = LeitorJson()
    mapaEstado.setLeitor(leitorJson)
    mapaEstado.construir_grafo_estado(arquivoJson)

    print("Caminho da busca em profundidade")
    print(mapaEstado.mapaGrafo.busca_em_profundidade("Campina Grande", "Montadas"))
    print()
    print("Caminho da busca em largura")
    print(mapaEstado.mapaGrafo.busca_em_largura("Campina Grande", "Montadas"))
    print()
    print("Caminho da busca em estrela")
    print(mapaEstado.mapaGrafo.busca_a_estrela("Campina Grande", "Montadas", "Campina Grande"))
    print()

arquivoJson.close()