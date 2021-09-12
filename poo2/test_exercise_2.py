from poo2.exercise2.Car import Car
from poo2.exercise2.FourWheel import FourWheel
from poo2.exercise2.Truck import Truck
from poo2.exercise2.TwoWheel import TwoWheel
from poo2.exercise2.Vehicle import Vehicle

vehicle = Vehicle('rojo', 450)
vehicle.transit()
vehicle.allow_person(77.8)
vehicle.__str__()

two_wheel = TwoWheel('verde', 467, 290.43)
two_wheel.transit()
two_wheel.allow_person(71.43)
two_wheel.fill_gasoline(2.88)
two_wheel.__str__()

four_wheel = FourWheel('púrpura', 467, 3)
four_wheel.transit()
four_wheel.allow_person(83.6)
four_wheel.repaint('amarillo')
four_wheel.__str__()

car = Car('negro', 467, 5, 4)
car.transit()
car.allow_person(73.3)
car.repaint('gris')
car.install_snow_chains(3)
car.uninstall_snow_chains(1)
car.__str__()

truck = Truck('azul', 467, 2, 9)
truck.transit()
truck.allow_person(92.9)
truck.repaint('blanco')
truck.install_trailer(15.4)
truck.__str__()
