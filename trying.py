import random


class Warrior:
    def __init__(self, name, shield=50, life=100):
        self.name = name
        self.shield = shield
        self.life = life

    def take_damage(self, damage):
        if self.life != 0:
            if damage > self.shield:
                damage_took = damage - self.shield
                self.life -= damage_took
                self.shield = 0
                print(f"Shield is down to {self.shield} and life is now {self.life}")
            elif self.shield != 0:
                self.shield -= damage
                print(f"Sheild is down to {self.shield}")
        else:
            print("You can t attack a dead warrior")

    def sward_swing(self, enemy):
        damage = random.randint(40, 70)
        print(f"You attacked {enemy.name} damage given {damage}")
        enemy.take_damage(damage)


class Wizard(Warrior):

    def __init__(self, name, life=100, mana=200):
        super().__init__( name, life=life)
        self.name = name
        self.life = life
        self.mana = mana
        self.alive = True
        self.shield = False

    def take_damage(self, damage):
        self.chance = random.randint(1, 4)
        if self.life <= damage:
            print("The wizard is dead")

        elif self.chance != 2:
            if self.life != 0:
                self.life -= damage
                print(f"Life is now {self.life}")
        else:
            print(f"Dodged with the magic shield life is still {self.life}")

    def attack_1(self, spell, enemy):
        spell = 'magic ball'
        damage = 30
        print(f"You attacked {enemy.name}")
        enemy.take_damage(damage)





gabi = Wizard("Gabi", mana=300, life=100)
radu = Warrior("Radu")

radu.sward_swing(gabi)
radu.sward_swing(gabi)

gabi.attack_1('magic ball', radu)
gabi.attack_1('magic ball', radu)

gabi.attack_1('magic ball', radu)

gabi.attack_1('magic ball', radu)
gabi.attack_1('magic ball', radu)

gabi.attack_1('magic ball', radu)

radu.sward_swing(gabi)
radu.sward_swing(gabi)
radu.sward_swing(gabi)
radu.sward_swing(gabi)








