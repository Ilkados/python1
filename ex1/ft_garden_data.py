class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    plants = [rose, sunflower, cactus]

    print("=== Garden Plant Registry ===")
    for i in range(len(plants)):
        p = plants[i]
        print(f"{p.name}: {p.height}cm, {p.age} days old")
