import json
from interfaces.leitor import LeitorInterface


class LeitorJson(LeitorInterface):
    def __init__(self):
        pass

    '''
        Obtém os dados de um determinado arquivo json e retorna eles no formato adequado para ser usado pelo Grafo
    '''
    def obter_dados(self, arquivo):
        conteudo_arquivo = json.load(arquivo)
        rotas = conteudo_arquivo["rotas"]
        dados = list()

        for rotaObj in rotas:
            cidade1 = rotaObj["cidadeOrigem"]
            cidade2 = rotaObj["cidadeDestino"]
            peso = rotaObj["distancia"]
            dados.append([f"{cidade1}-{cidade2}", peso])

        return dados
