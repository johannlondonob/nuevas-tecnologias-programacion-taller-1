from poo1.exercise1.Animal import Animal


class Oviparous(Animal):

    def __init__(self, weight):
        Animal.__init__(self, weight)

    @staticmethod
    def eat():
        print('Ovíparo comiendo...')

    @staticmethod
    def oviposit():
        print('Poner huevos...')
