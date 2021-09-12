from poo2.exercise1.Lawyer import Lawyer
from poo2.exercise1.Person import Person
from poo2.exercise1.Veterinary import Veterinary

person = Person('Johan', 'cafés', 'masculino', 26, 97.8, 1.75)
person.__str__()
person.eat()
person.run()
person.dance()
person.drink()
person.sleep()
person.asleep()

veterinary = Veterinary('María', 'cafés', 'femenino', 38, 82, 1.68, "43.687.173", "cardiología")
veterinary.__str__()
veterinary.eat()
veterinary.run()
veterinary.dance()
veterinary.drink()
veterinary.sleep()
veterinary.asleep()
veterinary.in_consultation()
veterinary.in_surgery()
veterinary.inactive()

lawyer = Lawyer('Guillermo', 'cafés', 'masculino', 33, 76, 1.75, 'Abogado penalista',
                ['Diplomado de Excel', 'Inglés VII', 'Licenciado en Ciencias Sociales'])
lawyer.__str__()
lawyer.eat()
lawyer.run()
lawyer.dance()
lawyer.drink()
lawyer.sleep()
lawyer.asleep()
lawyer.litigate()
