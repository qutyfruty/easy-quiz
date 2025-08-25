class Player:
    def __init__(self, name, health=100):
        self.name=name
        self.health=health

    def take_damage(self, amount=10):
        self.health -=amount
        if self.health<0:
            self.health=0
        print(f"{self.name}, ai primit {amount} damage, mai ai {self.health} HP.")