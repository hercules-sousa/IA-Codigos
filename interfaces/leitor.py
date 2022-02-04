from abc import ABC, abstractmethod


class LeitorInterface(ABC):

    @abstractmethod
    def obter_dados(self, arquivo) -> []:
        raise NotImplementedError
