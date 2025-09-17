# 🐍 Python OOP Assignment

This repository contains solutions for **Assignment 1: Design Your Own Class** and **Activity 2: Polymorphism Challenge**.

---

## 📘 Assignment 1: Design Your Own Class 🏗️

### ✅ Task
- Create a class representing anything (Smartphone, Book, Superhero, etc.).
- Add attributes and methods.
- Use a constructor to initialize unique values.
- Add inheritance to explore polymorphism or encapsulation.

### 💻 Solution: Smartphone Class

```python
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
        super().__init__(brand, model)
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
📝 Example Output

📞 Calling 123-456-7890 from Samsung Galaxy S24...
🔋 Samsung Galaxy S24 is charging...
🎮 Asus ROG 7 enters Game Mode with Liquid Cooling cooling!
🎭 Activity 2: Polymorphism Challenge
✅ Task
Create a program with animals or vehicles.

Each class should define the same action (e.g., move()), but behave differently.

💻 Solution: Vehicle Example

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
📝 Example Output

🚗 Driving on the road!
✈️ Flying in the sky!
🚤 Sailing on water!
🛠️ Requirements
Python 3.x