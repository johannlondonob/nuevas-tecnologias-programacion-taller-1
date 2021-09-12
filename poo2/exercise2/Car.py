from poo2.exercise2.FourWheel import FourWheel


class Car(FourWheel):
    __number_snow_chains = None

    def __init__(self, color, weight, number_doors, number_snow_chains):
        FourWheel.__init__(self, color, weight, number_doors)
        self.__number_snow_chains = number_snow_chains

    def __str__(self):
        FourWheel.__str__(self)
        print(f"Número de cadenas para nieve: {self.__number_snow_chains}")

    def transit(self):
        print('Carro transitando...')

    def install_snow_chains(self, chains):
        self.__number_snow_chains = self.__number_snow_chains + chains
        print(f'Instalando {chains} cadenas para nieve')

    def uninstall_snow_chains(self, chains):
        self.__number_snow_chains = self.__number_snow_chains - chains
        print(f'Desinstalando {chains} cadenas para nieve')
