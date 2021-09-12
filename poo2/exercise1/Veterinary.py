from poo2.exercise1.Person import Person


class Veterinary(Person):
    __identification_card, __specialty = "", ""

    def __init__(self, name, eye_color, genre, age, weight, height, identification_card, specialty):
        Person.__init__(self, name, eye_color, genre, age, weight, height)
        self.__identification_card = identification_card
        self.__specialty = specialty

    def __str__(self):
        Person.__str__(self)
        print(f"Cédula: {self.__identification_card}")
        print(f"Especialidad: {self.__specialty}")

    def eat(self):
        print('Veterinario comiendo...')

    def run(self):
        print('Veterinario corriendo...')

    def drink(self):
        print('Veterinario bebiendo...')

    def sleep(self):
        print('Veterinario durmiendo...')

    def asleep(self):
        print('Veterinario despertando...')

    def dance(self):
        print('Veterinario bailando...')

    def in_consultation(self):
        print("En consulta...")

    def in_surgery(self):
        print("En cirugía...")

    def inactive(self):
        print("Inactivo...")
