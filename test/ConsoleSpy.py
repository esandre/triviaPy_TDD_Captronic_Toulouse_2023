from io import StringIO

from ConsoleInterface import ConsoleInterface


class ConsoleSpy(ConsoleInterface):
    __output = StringIO()

    def print(self, message: str):
        self.__output.write(message)
        self.__output.write("\n")

    def get_output(self):
        return self.__output.getvalue()