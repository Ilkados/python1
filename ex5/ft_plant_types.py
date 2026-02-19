class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def base_info(self):
        text = f"{self.name}: {self.height}cm, {self.age} days old"
        return text


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def __str__(self):
        return (
            self.name
            + "(Flower): "
            + str(self.height)
            + "cm, "
            + str(self.age)
            + "days, "
            + self.color
            + "color"
        )

    def bloom(self):
        print(self.name + " is blomming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def __str__(self):
        return (
            self.name
            + " (Tree): "
            + str(self.height)
            + "cm, "
            + str(self.age)
            + " days, "
            + str(self.trunk_diameter)
            + "cm diameter"
        )

    def produce_shade(self):
        shade_area = (int(self.trunk_diameter * self.trunk_diameter) / 32)
        print(
            self.name
            + "provides "
            + str(shade_area)
            + " square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def __str__(self):
        return (
            self.name
            + " (Tree): "
            + str(self.height)
            + "cm, "
            + str(self.age)
            + " days, "
            + self.harvest_season
            + "harvest"
        )

    def describe_nutrition(self):
        print(self.name + " is rich in " + self.nutritional_value)


if __name__ == "__main__":
    print("=== Garden plant types ===")

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Lily", 40, 90, "white"),
    ]

    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pink", 790, 2000, 12),
    ]

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 75, "spring", "beta-carotene"),
    ]

    print(flowers[0])
    flowers[0].bloom()

    print("\n")

    print(trees[0])
    trees[0].produce_shade()
    print("\n")

    print(vegetables[0])
    vegetables[0].describe_nutrition()
