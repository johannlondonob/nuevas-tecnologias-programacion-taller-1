from poo2.exercise2.FourWheel import FourWheel


class Truck(FourWheel):
    __lenght = None

    def __init__(self, color, weight, number_doors, lenght):
        FourWheel.__init__(self, color, weight, number_doors)
        self.__lenght = lenght

    def __str__(self):
        FourWheel.__str__(self)
        print(f"Longitud del camión: {self.__lenght}")

    def transit(self):
        print('Camión transitando...')

    def install_trailer(self, trailer_lenght):
        self.__lenght = self.__lenght + trailer_lenght
        print(f'Instalando nuevo remolque de {trailer_lenght} metros de largo')
