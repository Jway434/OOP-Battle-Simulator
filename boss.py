import random
from enemy import Enemy
class Boss(Enemy):
    """
    Boss blueprint.
    

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the boss can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, hp):
        self.name = "Jeromy"
        self.hp = 10000000000
    
    def attack(self):
        if random.randint(1,2) == 1:
            self.dmg = random.randint(1, 1000)
        else:
            self.dmg = random.randint(1,1000000)
    
    def is_alive(self):
        return self.hp > 0