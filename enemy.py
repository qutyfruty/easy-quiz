class Enemy:
    def __init__(self, name, health, level):
        self.name=name
        self.health=health
        self.level=level


    def take_damage(self, amount=10):
        self.health -=amount
        if self.health<0:
            self.health=0
        print(f"{self.name} a primit {amount} damage, mai are {self.health} HP.")