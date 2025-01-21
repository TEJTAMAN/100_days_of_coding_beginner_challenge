#Create a class for a simple car with methods like start and stop.

class Car:
    """A simple car class with start and stop functionality."""

    def __init__(self, make, model, year):
       
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        """Start the car."""
        if self.is_running:
            print(f"The {self.year} {self.make} {self.model} is already running.")
        else:
            self.is_running = True
            print(f"The {self.year} {self.make} {self.model} has started.")

    def stop(self):
        
        if not self.is_running:
            print(f"The {self.year} {self.make} {self.model} is already stopped.")
        else:
            self.is_running = False
            print(f"The {self.year} {self.make} {self.model} has stopped.")

    def __str__(self):
        
        return f"{self.year} {self.make} {self.model}"
    
    
"""
# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Interact with the car
print(my_car)           # Output: 2020 Toyota Corolla
my_car.start()          # Output: The 2020 Toyota Corolla has started.
my_car.start()          # Output: The 2020 Toyota Corolla is already running.
my_car.stop()           # Output: The 2020 Toyota Corolla has stopped.
my_car.stop()           # Output: The 2020 Toyota Corolla is already stopped.
"""
