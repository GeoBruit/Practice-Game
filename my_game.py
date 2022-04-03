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

        if damage < self.life > 0:      # TODO solve issue if damage > 100
            if self.shield:
                if damage > self.shield:
                    damage_took = damage - self.shield
                    self.life -= damage_took
                    self.shield = 0
                    print(f"{self.name} Shield down to {self.shield}, life is now {self.life}")
                elif self.shield != 0:
                    self.shield -= damage
                    print(f"Shield down to {self.shield}")
            elif self.shield == 0:
                self.life -= damage
                print(f"{self.name} Shield down to {self.shield}, life is now {self.life}")

        else:
            print(f"{self.name} is dead you won!!!")
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

    @staticmethod
    def sword_swing(enemy: Character):
        """
        Function that allow us to attack  the enemy
        :param enemy: The enemy we are attacking
        """
        power = random.randint(20, 40)
        enemy.take_damage(power)
        print(f"You attacked with the sward swing ability, {enemy.name}")

    @staticmethod
    def spam_trow(enemy: Character):
        """An attack function, you trow a piece of old spam at the enemy and give him damage"""
        power = 25
        enemy.take_damage(power)
        print(f"Spam attack successful enemy life: {enemy.life}")

    def kill_them_all(self, enemy):
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

    @staticmethod
    def magic_spam(enemy: Character):
        damage = random.randint(30, 45)
        enemy.take_damage(damage)
        print(f"The magic spam worked. Enemy life: {enemy.life}")

    @staticmethod
    def wand_of_terror(enemy: Character):
        damage = random.randint(40, 60)
        enemy.take_damage(damage)
        print(f"The want of terror attacked enemy life: {enemy.life}")

    def thunder_rain(self, enemy: Character):
        if not self.used:
            if self.life <= 50:
                damage = random.randint(60, 90)
                enemy.take_damage(damage)
                self.used = True
                print(f"{enemy.name} attacked successful damage done {damage}, {enemy.name} life is {enemy.life}")
            else:
                print("You can t use this ability yet...")
        else:
            print("You can only used this ability once...already used...try spam attack")


def choose_character():
    character_choose = input("Please choose 1 to play as a Warrior or 2 to play as a Wizard: ")

    global choose_name

    choose_name = input("Name your character: ")

    global player

    if character_choose == "1":
        player = Warrior(choose_name)
        return player
    else:
        player = Wizard(choose_name)
        return player


def choose_opponent():

    global opponent

    if player == Warrior:
        opponent = Wizard("Slayer")
        return opponent
    else:
        opponent = Warrior("Slayer")
        return opponent


def choose_attack():
    if isinstance(player, Warrior):
        attack = input("Choose your attack move: 1.Sword Swing, 2.Spam Trow, 3.Kill Them All: ")
        if attack == "1":
            player.sword_swing(opponent)
        elif attack == "2":
            player.spam_trow(opponent)
        elif attack == "3":
            player.kill_them_all(opponent)
    elif isinstance(player, Wizard):
        attack = input("Choose your attack move: 1.Magic Spam, 2.Wand Of Terror, 3.Thunder Rain: ")
        if attack == "1":
            player.magic_spam(opponent)
        elif attack == "2":
            player.wand_of_terror(opponent)
        elif attack == "3":
            player.thunder_rain(opponent)


def main():
    pass
