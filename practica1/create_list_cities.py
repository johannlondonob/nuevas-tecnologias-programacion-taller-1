def create_list_cities():
    city = ""
    cities = []
    watcher = 'y'

    while watcher.lower() == "y":
        city = input('Ingresa el nombre de una ciudad turística de Colombia: ')
        cities.append(city)
        watcher = input('¿Ingresar más candidatos? Presiona \'Y\' para continuar ingresando... ')

    return cities


print(create_list_cities())
