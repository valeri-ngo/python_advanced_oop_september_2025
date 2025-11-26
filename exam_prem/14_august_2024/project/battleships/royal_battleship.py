from battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):
    AMMUNITION_AMOUNT = 100


    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.AMMUNITION_AMOUNT)


    def attack(self):
        if self.ammunition >= 25:
            self.ammunition -= 25

            return self.hit_strength

        if self.ammunition > 0:
            self.ammunition = 0

        return 0