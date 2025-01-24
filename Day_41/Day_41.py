#Implement inheritance between classes.


class Appliance:
    """Base class representing a generic appliance."""

    def __init__(self, brand, model, power_rating):
        self.brand = brand
        self.model = model
        self.power_rating = power_rating
        self.is_on = False

    def turn_on(self):
        """Turn the appliance on."""
        if self.is_on:
            print(f"The {self.brand} {self.model} is already on.")
        else:
            self.is_on = True
            print(f"The {self.brand} {self.model} has been turned on.")

    def turn_off(self):
        """Turn the appliance off."""
        if not self.is_on:
            print(f"The {self.brand} {self.model} is already off.")
        else:
            self.is_on = False
            print(f"The {self.brand} {self.model} has been turned off.")

    def __str__(self):
        return f"{self.brand} {self.model} (Power: {self.power_rating}W)"


class WashingMachine(Appliance):
    """Derived class representing a washing machine."""

    def __init__(self, brand, model, power_rating, load_capacity):
        super().__init__(brand, model, power_rating)
        self.load_capacity = load_capacity

    def start_wash_cycle(self):
        """Start the wash cycle."""
        if not self.is_on:
            print(f"Turn on the {self.brand} {self.model} before starting the wash cycle.")
        else:
            print(f"The {self.brand} {self.model} has started the wash cycle with a capacity of {self.load_capacity} kg.")

    def __str__(self):
        return f"{super().__str__()}, Load Capacity: {self.load_capacity}kg"


# Main program
def main():
    print("Create a new appliance or washing machine:")
    appliance_type = input("Enter 'A' for Appliance or 'W' for Washing Machine: ").strip().upper()

    brand = input("Enter the brand: ").strip()
    model = input("Enter the model: ").strip()
    power_rating = int(input("Enter the power rating in watts: ").strip())

    if appliance_type == 'W':
        load_capacity = int(input("Enter the load capacity in kg: ").strip())
        appliance = WashingMachine(brand, model, power_rating, load_capacity)
    else:
        appliance = Appliance(brand, model, power_rating)

    print("\nYour appliance details:")
    print(appliance)

    while True:
        action = input("\nChoose an action: (on/off/start/exit): ").strip().lower()
        if action == "on":
            appliance.turn_on()
        elif action == "off":
            appliance.turn_off()
        elif action == "start" and isinstance(appliance, WashingMachine):
            appliance.start_wash_cycle()
        elif action == "exit":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid action. Please try again.")


if __name__ == "__main__":
    main()

