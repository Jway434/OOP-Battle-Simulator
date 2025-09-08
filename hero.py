import random
class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength

    def strike(self):
        choice = input("Choose Attack(Gun or Sneeze): ")
        if choice.lower() == "gun":
           return random.randint(1, 100000)
        elif choice.lower() == "sneeze":
           return random.randint(1, 2)
        else:
           print("Invalid choice! Defaulting to Gun attack.")
        return random.randint(1, 1000000)

    def receive_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0