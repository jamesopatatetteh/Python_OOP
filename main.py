# Assignment 1: Design Your Own Class 🏗️

class Device:
    """Base class for all devices"""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


class Smartphone(Device):
    """Smartphone class inheriting from Device"""
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Initialize parent attributes
        self.storage = storage
        self.battery = battery

    def call(self, number):
        return f"📞 Calling {number} from {self.info()}..."

    def charge(self):
        return f"🔋 {self.info()} is charging..."


class GamingPhone(Smartphone):
    """Child class with extra features"""
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def game_mode(self):
        return f"🎮 {self.info()} enters Game Mode with {self.cooling_system} cooling!"


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S24", "256GB", "4500mAh")
print(phone1.call("+233551088952"))
print(phone1.charge())

gaming_phone = GamingPhone("Asus", "ROG 7", "512GB", "6000mAh", "Liquid Cooling")
print(gaming_phone.game_mode())


# Activity 2: Polymorphism Challenge 🎭

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")


class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road!"


class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky!"


class Boat(Vehicle):
    def move(self):
        return "🚤 Sailing on water!"


# Demonstration
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())