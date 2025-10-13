class Dogs:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

# Create objects (outside the class)
Jack = Dogs("Jack", "Bulldog", "Brown")
Max = Dogs("Max", "Beagle", "Tricolor")

# Print details
print("{} is a {}".format(Jack.name, Jack.breed))
print("{} is a {}".format(Max.name, Max.breed))
print("{} is {}".format(Jack.name, Jack.color))
print("{} is {}".format(Max.name, Max.color))
