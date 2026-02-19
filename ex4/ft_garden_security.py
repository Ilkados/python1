class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = 0
        self._age = 0
        self.set_age(age)
        self.set_height(height)

    def set_height(self, new_height):
        if new_height < 0:
            print(
                "Invalid operation attempted : height "
                + str(new_height)
                + " cm [REJECTED]"
            )
            print("Security: Negative height rejected")
        else:
            self._height = new_height
            print("Height updated: " + str(self._height) + "cm [OK]")

    def set_age(self, new_age):
        if new_age < 0:
            print(
                "Invalid operation at tempted : age "
                + str(new_age)
                + " days [REJECTED]"
            )
            print("Security: Negative age rejected")
        else:
            self._age = new_age
            print("Age updated: " + str(self._age) + " days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def get_info(self):
        return (
            self.name
            + " ("
            + str(self._height)
            + "cm, "
            + str(self._age)
            + " days)"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25, 30)
    print("Plant created: " + plant.name)

    plant.set_height(-5)

    print("Current plant: " + plant.get_info())
