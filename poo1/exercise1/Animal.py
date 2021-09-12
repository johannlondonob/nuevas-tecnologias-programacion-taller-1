class Animal:
    weight: float = 0

    def __init__(self, weight):
        self.weight = weight

    @staticmethod
    def eat():
        print('Comer...')
