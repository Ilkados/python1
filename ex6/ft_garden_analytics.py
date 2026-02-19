class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1


class FloweringPlant(Plant):
    def __init__(self, name, height, age, flower_color):
        super().__init__(name, height, age)
        self.flower_color = flower_color

    def blooming(self):
        return self.flower_color + " flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, flower_color, prize_points):
        super().__init__(name, height, age, flower_color)
        self.prize_points = prize_points


class Garden:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
        self.plants_added = 0
        self.total_growth = 0

    def add_plant(self, plant):
        self.plants.append(plant)
        self.plants_added += 1
        print("Added " + plant.name + " to " + self.owner_name + "'s garden")

    def help_plants_grow(self):
        print(self.owner_name + " is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1
            print(plant.name + " grew 1cm")
        return self.total_growth


class GardenManager:
    class GardenStats:
        @staticmethod
        def count_plant_types(garden):
            regular = 0
            flowering = 0
            prize = 0

            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1

            return regular, flowering, prize

    def __init__(self):
        self.gardens = {}
        self.stats = self.GardenStats()

    def add_garden(self, owner_name):
        self.gardens[owner_name] = Garden(owner_name)

    def get_garden(self, owner_name):
        return self.gardens[owner_name]

    def plant_description(self, plant):
        base = plant.name + ": " + str(plant.height) + "cm"

        if isinstance(plant, PrizeFlower):
            return (
                base
                + ", "
                + plant.blooming()
                + ", Prize points: "
                + str(plant.prize_points)
            )

        if isinstance(plant, FloweringPlant):
            return base + ", " + plant.blooming()

        return base

    def report(self, owner_name):
        garden = self.get_garden(owner_name)

        print("=== " + garden.owner_name + "'s Garden Report ===")
        print("Plants in garden:")
        for plant in garden.plants:
            print("- " + self.plant_description(plant))

        print(
            "Plants added: "
            + str(garden.plants_added)
            + ", Total growth: "
            + str(garden.total_growth)
            + "cm"
        )

        regular, flowering, prize = self.stats.count_plant_types(garden)
        print(
            "Plant types: "
            + str(regular)
            + " regular, "
            + str(flowering)
            + " flowering, "
            + str(prize)
            + " prize flowers"
        )

    @staticmethod
    def validate_height(height):
        return height >= 0

    def garden_score(self, owner_name):
        garden = self.get_garden(owner_name)
        total_scores = 0
        for plant in garden.plants:
            total_scores += plant.height
        return total_scores

    def total_gardens_managed(self):
        return len(self.gardens)

    @classmethod
    def create_garden_network(cls):
        manager = cls()
        manager.add_garden("Alice")
        manager.add_garden("Bob")
        return manager


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager.create_garden_network()

    alice = manager.get_garden("Alice")
    bob = manager.get_garden("Bob")

    alice.add_plant(Plant("Oak Tree", 100, 1825))
    alice.add_plant(FloweringPlant("Rose", 25, 30, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, 60, "yellow", 10))
    print("\n")
    # Add Bob plants without printing (to match the sample style)
    bob.plants.append(Plant("Pine Tree", 60, 900))
    bob.plants.append(FloweringPlant("Daisy", 32, 15, "white"))
    bob.plants_added += 2

    alice.help_plants_grow()
print()
manager.report("Alice")

print("Height validation test: " + str(GardenManager.validate_height(10)))

alice_score = manager.garden_score("Alice")
bob_score = manager.garden_score("Bob")
print(
    "Garden scores - Alice: "
    + str(alice_score)
    + ", Bob: "
    + str(bob_score)
)

print("Total gardens managed: " + str(manager.total_gardens_managed()))
