class Vehicle:
    def __init__(self, id, manufacturer, model, cost):
        self.id = id
        self.manufacturer = manufacturer
        self.model = model
        self.cost = cost

        @property
        def id(self):
            return self.id

        @id.setter
        def id(self, value):
            self.id = value

        @property
        def manufacturer(self):
            return self.manufacturer

        @manufacturer.setter
        def manufacturer(self, value):
            self.manufacturer = value

        @property
        def model(self):
            return self.model

        @model.setter
        def model(self, value):
            self.model = value

        @property
        def cost(self):
            return self.cost

        @cost.setter
        def cost(self, value):
            self.cost = value


vehicle = Vehicle('TPQ-11F', 'HONDA MOTORS', '2022', 22000000)
vehicle.id = 'TPQ_11F'
print(vehicle.id)
print(vehicle.manufacturer)
print(vehicle.model)
print(vehicle.cost)
