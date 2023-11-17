import abc


class ConsoleInterface(abc.ABC):
    @abc.abstractmethod
    def print(self, message: str):
        pass
