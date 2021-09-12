from poo2.exercise2.Vehicle import Vehicle


class TwoWheel(Vehicle):
    __cilinder = None

    def __init__(self, color, weight, cilinder):
        Vehicle.__init__(self, color, weight)
        self.__cilinder = cilinder

    def __str__(self):
        Vehicle.__str__(self)
        print(f"Centímetros cúbicos del vehículo: {self.__cilinder}")

    def transit(self):
        print('Two wheel transitando...')

    def fill_gasoline(self, liters):
        print(f'Tanqueando {liters} litros de gasolina')
