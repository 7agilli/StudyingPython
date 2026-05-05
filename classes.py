class Character():
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    
    def attack(self, enemy):
        damage = self.attack_power
        enemy.health -= damage   
        print(f'The {self.name} has attacked {enemy.name}. Your health now is {enemy.health}')

    def is_alive(self):
        return self.health > 0
    
    def show_status(self):
        print(f'Name: {self.name} | Health: {self.health} HP | Attack Power: {self.attack_power} ATK')


class Hero(Character):
    def __init__(self, name, health, attack_power, level):
        super().__init__(name, health, attack_power)
        self.level = level

    def heal(self):
        self.health += 20
        print(f'The hero {self.name} has drinked and healed 20 hp')

    
    def level_up(self):
        self.level += 1
        self.attack_power += 5
        print(f'Level up! Level: {self.level}')
    
    def armor(self):
        self.health += 15
        print(f'The hero used armor and your health is {self.health}')

    
class Villain(Character):
    def __init__(self, name, health, attack_power, exp_gained):
        super().__init__(name, health, attack_power)
        self.exp_gained = exp_gained

    def rage(self):
        self.attack_power += 10
        print(f'{self.name} is enraged! ATK {self.attack_power}')

    def roar(self):
        print(f'{self.name} is Enraged! Say ROAAAAAAAAAAR!')



José = Hero('José', 100, 30, 10)
Ogre = Villain('Ogre', 120, 35, 50)




José.show_status()
José.armor()
José.attack(Ogre)
print('---------------------------------------------------')
Ogre.attack(José)
Ogre.roar()
Ogre.rage()

