# Definition a father Class
class Character():
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
    
    def attack(self, enemy): # ----> Definition of dmg method
        damage = self.attack_power
        enemy.health -= damage
        print(f'The {self.name} dealt {damage} dmg in {enemy.name}')

    def defense(self, enemy):
        enemy.attack_power -= self.defense
        print(f'The {self.name} defended hit!')

    def show_status(self):
        print(f'Name: {self.name} | Health: {self.health} HP | Attack Power: {self.attack_power} | Defense: {self.defense} status') # Show status to player

class Human(Character): # -------------> Definition of Human class or Children Class
    def __init__(self, name, health, attack_power, defense):
        super().__init__(name, health, attack_power, defense)

    def Coumpoust_v(self):
        self.health += 20
        self.defense += 10
        print(f'{self.name} was drinked Coumpoust V and gained more status.')

    def brute(self):
        print(f'The brute says: "I niveled the game"')


class Super(Character): # -------------> Definition of Super class or Children class
    def __init__(self, name, health, attack_power, defense):
        super().__init__(name, health, attack_power, defense)

    def milk(self):
        self.health += 25
        self.defense +=15
        print(f'The hero {self.name} drinked a milk and gained new status!')

    def intimidate(self):
        print(f'The {self.name} have a rage mode and ameaced your enemy with your laser eye!')


Billy = Human('Billy Butcher', 110, 20, 30)
Billy.Coumpoust_v()
Billy.show_status()
Billy.brute()

Homelander = Super('Homelander', 120, 25, 35)
Homelander.milk()
Homelander.intimidate()
Homelander.show_status()
