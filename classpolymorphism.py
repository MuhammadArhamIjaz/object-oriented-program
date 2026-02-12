class BMW:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed

    def car_info(self):
        print("BMW Car")
        print("Fuel Type:", self.fuel_type)
        print("Max Speed:", self.max_speed, "km/h")
        print()


class Ferrari:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed

    def car_info(self):
        print("Ferrari Car")
        print("Fuel Type:", self.fuel_type)
        print("Max Speed:", self.max_speed, "km/h")
        print()

bmw_car = BMW("Petrol", 250)
ferrari_car = Ferrari("Petrol", 340)

for car in (bmw_car, ferrari_car):
    car.car_info()
