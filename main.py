import os
from mapa.mapa import Mapa
from leitores.leitorTxt import LeitorTxt
from leitores.leitorJson import LeitorJson

# Obtendo diretório onde o programa está sendo executado
dir_atual = os.path.dirname(__file__)

# Obtendo caminho do arquivo
caminho_arquivo = os.path.join(dir_atual, 'arquivos/Cidades - Brasil.txt')

# Criando mapa
mapa = Mapa("Capitais")

# Criando leitores para arquivos TXT e JSON
leitor_txt = LeitorTxt()
leitor_json = LeitorJson()

# Verificando tipo de arquivo para determinar leitor
if caminho_arquivo.endswith('.txt'):
    print('Trabalhando com arquivo TXT...\n')

    mapa.set_leitor(leitor_txt)
elif caminho_arquivo.endswith('.json'):
    print('Trabalhando com arquivo JSON...\n')

    mapa.set_leitor(leitor_json)

# Abrindo arquivo para obter dados e construir grafo
with open(caminho_arquivo, encoding='utf-8') as arquivo:
    mapa.construir_grafo_mapa(arquivo)

arquivo.close()

print(mapa.mapa_grafo)

# Obtendo entrada do usuário
cidade_origem = input('Digite o nome da cidade origem: ')
cidade_destino = input('Digite o nome da cidade destino: ')

print('\nEscolha um tipo de algoritmo de busca:\n')
print('1 - Busca em profundidade')
print('2 - Busca em largura')
print('3 - Busca A*')

op = int(input())

if op == 1:
    print("Caminho da busca em profundidade:")
    print(mapa.busca_em_profundidade(cidade_origem, cidade_destino))

if op == 2:
    print("Caminho da busca em largura:")
    print(mapa.busca_em_largura(cidade_origem, cidade_destino))

if op == 3:
    print('\nInforme os valores heurísticos:\n')

    # Criando dicionário enquanto obtém entrada do usuário
    h = {cidade: float(input(f'{cidade}: ')) for cidade in mapa.mapa_grafo.vertices}

    print("\nCaminho da busca em estrela:")
    print(mapa.busca_a_estrela(cidade_origem, cidade_destino, h))
