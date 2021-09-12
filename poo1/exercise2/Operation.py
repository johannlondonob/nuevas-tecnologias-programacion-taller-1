class Operation:
    __num_1: float = None
    __num_2: float = None
    __result: float = None
    __operation: str = ""

    def __init__(self, num_1, num_2, operation):
        self.__num_1 = num_1
        self.__num_2 = num_2
        self.__operation = operation

    def print_result(self):
        self.__operate()
        return self.__result

    def __operate(self):
        if self.__operation == "+":
            self.__result = self.__num_1 + self.__num_2
        elif self.__operation == "-":
            self.__result = self.__num_1 - self.__num_2
        elif self.__operation == "*":
            self.__result = self.__num_1 * self.__num_2
        else:
            self.__result = self.__num_1 / self.__num_2
