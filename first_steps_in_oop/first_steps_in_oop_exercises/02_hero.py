class Hero:

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int):
        current_health = self.health - damage
        self.health = current_health

        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"
        return None

    def heal(self, amount: int):
        self.health += amount
        return self.health

hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))