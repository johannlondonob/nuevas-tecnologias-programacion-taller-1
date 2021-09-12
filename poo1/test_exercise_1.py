from poo1.exercise1.Animal import Animal
from poo1.exercise1.Dog import Dog
from poo1.exercise1.Dolphin import Dolphin
from poo1.exercise1.Mammal import Mammal
from poo1.exercise1.Oviparous import Oviparous

print("Instancia clase Animal")
animal = Animal(75)
print(f"Peso del animal: {animal.weight}")
animal.eat()
print("Fin instancia clase Animal \n")

print("Instancia clase Ovíparo")
oviparous = Oviparous(1.5)
print(f"Peso del ovíparo: {oviparous.weight}")
oviparous.eat()
oviparous.oviposit()
print("Fin instancia clase Ovíparo")

print("Instancia clase Mamífero")
mammal = Mammal(13, False)
print(f"Peso del mamífero: {mammal.weight}")
print("Animal de sangre:", "caliente" if mammal.is_hot_blood else "fría")
mammal.eat()
mammal.suckle()
print("Fin instancia clase Mamífero")

print("Instancia clase Perro")
dog = Dog(25, True, "dorado")
print(f"Peso del perro: {dog.weight}")
print(f"Color pelaje del perro: {dog.fur_color}")
print("Perro de sangre:", "caliente" if dog.is_hot_blood else "fría")
dog.eat()
dog.give_birth()
dog.suckle()
dog.bark()
print("Fin instancia clase Perro")

print("Instancia clase Delfín")
dolphin = Dolphin(89, False)
print(f"Peso del delfín: {dolphin.weight}")
print("Delfín de sangre:", "caliente" if dolphin.is_hot_blood else "fría")
dolphin.eat()
dolphin.give_birth()
dolphin.suckle()
dolphin.swim()
print("Fin instancia clase Delfín")
