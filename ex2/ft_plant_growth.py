class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height = self.height + 1

    def age_plant(self):
        self.age = self.age + 1

    def get_info(self):
        text = f"{self.name}: {self.height}cm, {self.age} days old"
        return text


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    Sunflower = Plant("Sunflower", 80, 45)

    start1 = rose.height
    start2 = Sunflower.height

    print("=== Day 1 ===")
    print(rose.get_info())
    print(Sunflower.get_info())

    for day in range(6):
        rose.grow()
        rose.age_plant()
        Sunflower.grow()
        Sunflower.age_plant()

    print("=== Day 7 ===")
    end1 = rose.height
    end2 = Sunflower.height
    print(rose.get_info())
    print(Sunflower.get_info())

    growth1 = end1 - start1
    growth2 = end2 - start2

    print(f"Growth this week: +{growth1}cm")
