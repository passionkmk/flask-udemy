lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}

class LottteryPlayer: 
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)

player_one = LottteryPlayer("Rolf")
player_one.name = (1, 2, 3, 6, 7, 8)
player_two = LottteryPlayer("Jose")

print(player_one.name == player_two.name)

