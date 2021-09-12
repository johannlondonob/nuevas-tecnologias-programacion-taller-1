from poo1.exercise1.Mammal import *


class Dog(Mammal):
    fur_color = ""

    def __init__(self, weight, is_hot_blood, fur_color):
        Mammal.__init__(self, weight, is_hot_blood)
        self.fur_color = fur_color

    @staticmethod
    def eat():
        print('Perro comiendo...')

    @staticmethod
    def give_birth():
        print('Perro pariendo...')

    @staticmethod
    def suckle():
        print('Perro amamantando...')

    @staticmethod
    def bark():
        print('Ladrar...')
