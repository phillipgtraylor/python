# define the Vehicle class
class Vehicle:
    name = ""

    color = ""
    value = ""

    def description(self):
        desc_str = "%s is a %s car worth %s." % (
            self.name,
            self.color,
            self.value,
        )
        return desc_str


# assign values for description
car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car2.name = "Jump"

car1.color = "red"
car2.color = "blue"

car1.value = "$60,000.00"
car2.value = "$10,000.00"

# test code
print(car1.description())
print(car2.description())
