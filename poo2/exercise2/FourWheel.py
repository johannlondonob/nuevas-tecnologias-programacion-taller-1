from poo2.exercise2.Vehicle import Vehicle


class FourWheel(Vehicle):
    __number_doors = None

    def __init__(self, color, weight, number_doors):
        Vehicle.__init__(self, color, weight)
        self.__number_doors = number_doors

    def __str__(self):
        Vehicle.__str__(self)
        print(f"Número de puertas: {self.__number_doors}")

    def transit(self):
        print('Four wheel transitando...')

    def repaint(self, color):
        self.__color = color
        print(f'Repintando vehículo de {self.__color}')
