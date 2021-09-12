from poo2.exercise1.Person import Person


class Lawyer(Person):
    __title = ""
    __courses = []

    def __init__(self, name, eye_color, genre, age, weight, height, title, courses):
        Person.__init__(self, name, eye_color, genre, age, weight, height)
        self.__title = title
        self.__courses = courses

    def __str__(self):
        Person.__str__(self)
        print(f"Título: {self.__title}")
        print(f"Cursos: {self.__courses}")

    def eat(self):
        print('Abogado comiendo...')

    def run(self):
        print('Abogado corriendo...')

    def drink(self):
        print('Abogado bebiendo...')

    def sleep(self):
        print('Abogado durmiendo...')

    def asleep(self):
        print('Abogado despertando...')

    def dance(self):
        print('Abogado bailando...')

    def litigate(self):
        print("Litigar...")
