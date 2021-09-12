class Person:
    __name, __eye_color, __genre = "", "", ""
    __age = 0
    __weight, __height = 0.0, 0.0

    def __init__(self, name, eye_color, genre, age, weight, height):
        self.__name = name
        self.__eye_color = eye_color
        self.__genre = genre
        self.__age = age
        self.__weight = weight
        self.__height = height

    def __str__(self):
        print(f"Nombre: {self.__name}")
        print(f"Edad: {self.__age}")
        print(f"Color ojos: {self.__eye_color}")
        print(f"Género: {self.__genre}")
        print(f"Estatura: {self.__height}")
        print(f"Peso: {self.__weight}")

    def eat(self):
        print('Comer')

    def run(self):
        print('Correr')

    def drink(self):
        print('Tomar')

    def sleep(self):
        print('Dormir')

    def asleep(self):
        print('Despertar')

    def dance(self):
        print('Bailar')
