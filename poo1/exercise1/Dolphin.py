from poo1.exercise1.Mammal import Mammal


class Dolphin(Mammal):

    def __init__(self, weight, is_hot_blood):
        Mammal.__init__(self, weight, is_hot_blood)

    @staticmethod
    def eat():
        print('Delfín comiendo...')

    @staticmethod
    def give_birth():
        print('Delfín pariendo...')

    @staticmethod
    def suckle():
        print('Delfín amamantando...')

    @staticmethod
    def swim():
        print('Nadar...')
