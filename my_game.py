import random

# Creating the superClass that the other classes will inherit from:
class Character:

    def __init__(self, name, shield=0, life=100):
        self.name = name
        self.shield = shield
        self.life = life

    def take_damage(self, damage: int):
        """
        Take_damage function will reduce the life or shield of the character based on the damage
        inflicted  by the opponent
        :param damage: based on the attack chosen by the opponent damage my very
        :return: self.life and or self.shield after the attack
        """
        if damage < self.life > 0:      #TODO solve issue if damage > 100
            if self.shield:
                if damage > self.shield:
                    damage_took = damage - self.shield
                    self.life -= damage_took
                    self.shield = 0
                    print(f"Shield down to {self.shield}, life is now {self.life}")
                elif self.shield != 0:
                    self.shield -= damage
                    print(f"Shield down to {self.shield}")
            elif self.shield == 0:
                self.life -= damage
                print(f"Shield down to {self.shield}, life is now {self.life}")

        else:
            print("The opponent is dead you won!!!")
            self.life = 0

    def magical_potion(self):
        chance = random.randint(1, 4)
        if self.life == 0:
            if chance == 2:
                self.life = random.randint(40, 60)
                print(f"The magical potion worked you got one more chance an winning."
                      f"life has been restored to: {self.life}")
            else:
                print("Looks like the potion was a fake you lose!")


# Creating  individual characters to choose from *all based on the  superclass: Character
class Warrior(Character):

    def __init__(self, name, shield=50, life=100):
        super().__init__(name, shield, life)
        self.name = name
        self.shield = shield
        self.life = life

    def sword_swing(self, enemy:Character):
        """
        Function that allow us to attack  the enemy
        :param enemy: The enemy we are attacking
        """
        power = random.randint(20, 40)
        enemy.take_damage(power)
        print(f"You attacked with the sward swing ability, {enemy.name}")









