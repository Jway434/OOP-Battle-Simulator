import random
class Boss:
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
    
    def attack(self, dmg):
        chooseattack = random.randint(1,2)
        if chooseattack == 1:
            self.dmg = random.randint(1, 1000)
        else:

            self.dmg = random.randint(1,1000000)

    def receive_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0