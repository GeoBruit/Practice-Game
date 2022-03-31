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

    def eat_spam(self):
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
        self.used = False


    def sword_swing(self, enemy:Character):
        """
        Function that allow us to attack  the enemy
        :param enemy: The enemy we are attacking
        """
        power = random.randint(20, 40)
        enemy.take_damage(power)
        print(f"You attacked with the sward swing ability, {enemy.name}")

    def spam_trow(self, enemy:Character):
        """An attack function, you trow a piece of old spam at the enemy and give him damage"""
        power = 25
        enemy.take_damage(power)
        print(f"Spam attack succesfull enemy life: {enemy.life}")

    def kill_them_al(self, enemy):
        """Most powerfull attack function, when used it inflicts the most damage for the Warrior class
        Can only be used once and only when playes' life is lower then 50"""
        if not self.used:
            if self.life <= 50:
                damage = random.randint(60, 90)
                enemy.take_damage(damage)
                self.used = True
                print(f"{enemy.name} attacked succesffuly damage done {damage}, {enemy.name} life is {enemy.life}")
            else:
                print("You can t use this ability yet...")
        else:
            print("You can only used this ability once...already used...try spam attack")


class Wizard(Character):

    def __init__(self, name, shield=50, life=100, mana=200):
        super().__init__(name, shield, life)
        self.name = name
        self.shield = shield
        self.life = life
        self.name = mana
        self.used = False

    def magic_spam(self, enemy:Character):
        damage = random.randint(30, 45)
        enemy.take_damage(damage)

    def wand_of_terror(self, enemy:Character):
        damage = random.randint(40, 60)
        enemy.take_damage(damage)

    def thunder_rain(self, enemy:Character):
        if not self.used:
            if self.life <= 50:
                damage = random.randint(60, 90)
                enemy.take_damage(damage)
                self.used = True
                print(f"{enemy.name} attacked succesffuly damage done {damage}, {enemy.name} life is {enemy.life}")
            else:
                print("You can t use this ability yet...")
        else:
            print("You can only used this ability once...already used...try spam attack")


