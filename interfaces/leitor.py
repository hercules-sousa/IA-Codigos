from abc import ABC, abstractmethod


class LeitorInterface(ABC):

    @abstractmethod
    def obter_dados(self) -> []:
        raise NotImplementedError
