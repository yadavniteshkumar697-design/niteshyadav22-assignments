class Automobile:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def start(self):
        print(f"{self.name} {self.model} is starting.")

    def brake(self):
        print(f"{self.name} {self.model} is braking.")


class Car:
    def __init__(self, name, model, num_doors):
        self.automobile = Automobile(name, model)
        self.num_doors = num_doors

    def show_details(self):
        print(f"Car: {self.automobile.name} {self.automobile.model}")
        print(f"Doors: {self.num_doors}")
        self.automobile.start()
        self.automobile.brake()


class Bike:
    def __init__(self, name, model, has_sidecar):
        self.automobile = Automobile(name, model)
        self.has_sidecar = has_sidecar

    def show_details(self):
        print(f"Bike: {self.automobile.name} {self.automobile.model}")
        print(f"Sidecar: {self.has_sidecar}")
        self.automobile.start()
        self.automobile.brake()


car = Car("Tata", "Nexon", 5)
bike = Bike("Royal Enfield", "Classic 350", False)

car.show_details()

print()

bike.show_details()
