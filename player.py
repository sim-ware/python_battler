class Player:
    def __init__(self, name,  hitpoints=100):
        self.name = name
        self.hitpoints = hitpoints

    def attack(self, player):
        player.hitpoints = player.hitpoints - 10

    def heal(self):
        self.hitpoints = self.hitpoints + 10
