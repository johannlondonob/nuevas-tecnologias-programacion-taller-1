class Vehicle:
    __color = ""
    __weight = 0.0

    def __init__(self, color, weight):
        self.__color = color
        self.__weight = weight

    def __str__(self):
        print(f"Color del vehículo: {self.__color}")
        print(f"Peso del vehículo: {self.__weight}")

    def transit(self):
        print('Vehículo transitando...')

    def allow_person(self, person_weight):
        self.__weight = self.__weight + person_weight
        print('Permitiendo persona...')
