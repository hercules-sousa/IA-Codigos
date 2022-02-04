from interfaces.leitor import LeitorInterface


class LeitorTxt(LeitorInterface):
    def __init__(self):
        pass

    def obter_dados(self):
        return ["Buscando dados..."]