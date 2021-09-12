def drop_city():
    cities = ['Medellín', 'Cali', 'Bogotá', 'Cartagena']
    print(cities)
    city = input('Ingresa la ciudad que deseas eliminar: ')
    try:
        exists = cities.index(city)
        cities.pop(exists)
        return cities
    except:
        return 'No existe la ciudad que ingresaste'


print(drop_city())
