from poo1.exercise1.Animal import Animal


class Mammal(Animal):
    is_hot_blood = True

    def __init__(self, weight, is_hot_blood):
        Animal.__init__(self, weight)
        self.is_hot_blood = is_hot_blood

    @staticmethod
    def eat():
        print('Mamífero comiendo...')

    @staticmethod
    def give_birth():
        print('Parir...')

    @staticmethod
    def suckle():
        print('Amamantar...')
