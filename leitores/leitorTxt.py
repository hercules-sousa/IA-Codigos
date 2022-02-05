from interfaces.leitor import LeitorInterface


class LeitorTxt(LeitorInterface):
    def __init__(self):
        pass

    '''
        Obtém os dados de um determinado arquivo txt e retorna eles no formato adequado para ser usado pelo Grafo
    '''
    def obter_dados(self, arquivo):
        conteudo_arquivo = arquivo.readlines()
        dados = list()
        for linha in conteudo_arquivo:
            linha_lista = linha.split(",")
            cidade1 = linha_lista[0].strip()
            cidade2 = linha_lista[-1].strip()
            peso = float(linha_lista[1])
            dados.append([f"{cidade1}-{cidade2}", peso])
        return dados