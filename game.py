# class Player:
#     def __init__(self, name,  hitpoints=100):
#         self.name = name
#         self.hitpoints = hitpoints
#
#     def attack(self, player):
#         player.hitpoints = player.hitpoints - 10
#         # pass
#
#     def heal(self):
#         # self.hitpoints + 10 if self.hitpoints > 90
#         self.hitpoints = self.hitpoints + 10
#         # pass
class Game:
    def __init__(self, player_one, player_two, game_over=False):
        self.player_one = player_one
        self.player_two = player_two
        self.game_over = game_over

    def checkGamestate(self):
        # self.game_over = True if self.player_one.hitpoints == 100 or self.player_two.hitpoints == 100
        if self.player_one.hitpoints == 0:
            self.game_over = True
            print(self.player_two.name + ' wins!')
        elif self.player_two.hitpoints == 0:
            self.game_over = True
            print(self.player_one.name + ' wins!')
        else:
            print('Carry on...')
        # pass