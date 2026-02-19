class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def factory_line(self):
        return f"{self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    plant_specs = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants = []
    print("=== Plant Factory Output ===")

    for i in range(len(plant_specs)):
        name, height, age = plant_specs[i]
        p = Plant(name, height, age)
        plants.append(p)
        print("Created: " + p.factory_line())

    print("Total plants created: " + str(len(plants)))
