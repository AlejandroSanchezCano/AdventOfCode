'''
--- Day 21.2: RPG Simulator 20XX ---
Object-oriented programming with brute-force search.
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    stats = [int(line.rstrip().split(': ')[1]) for line in f.readlines()]

class Character:

    def __init__(self, life: int, damage: int = 0, armor: int = 0):
        self.life = life
        self.damage = damage
        self.armor = armor
        self.gold = 0

    def __repr__(self):
        return str(self.__dict__)

    def __gt__(self, other):
        dealt = self.damage - other.armor
        dealt = 1 if dealt < 1 else dealt
        received = other.damage - self.armor
        received = 1 if received < 1 else received
        winning_turns = other.life // dealt
        winning_turns += other.life % dealt > 0
        losing_turns = self.life // received
        losing_turns += self.life % received > 0
        return winning_turns <= losing_turns

    def equip(self, item):
        cost, damage, armor = store[item]
        self.damage += damage
        self.armor += armor
        self.gold += cost


store = {
    None : (0,0,0),
    'dagger': (8, 4, 0),
    'shortsword': (10, 5, 0),
    'warhammer': (25, 6, 0),
    'longsword': (40, 7, 0),
    'greataxe': (74, 8, 0),
    'leather': (13, 0, 1),
    'chainmail': (31, 0, 2),
    'splitmail': (53, 0, 3),
    'bandedmail': (75, 0, 4),
    'platemail': (102, 0, 5),
    'damage1': (25, 1, 0),
    'damage2': (50, 2, 0),
    'damage3': (100, 3, 0),
    'defense1': (20, 0, 1),
    'defense2': (40, 0, 2),
    'defense3': (80, 0, 3),
}

weapons = ['dagger', 'shortsword', 'warhammer', 'longsword', 'greataxe']
armors = [None, 'leather', 'chainmail', 'splitmail', 'bandedmail', 'platemail']
rings = [None, 'damage1', 'damage2', 'damage3', 'defense1', 'defense2', 'defense3']

losses = []
for weapon in weapons:
    for armor in armors:
        for ringr in rings:
            for ringl in rings:
                player = Character(100)
                boss = Character(*stats)
                player.equip(weapon)
                player.equip(armor)
                player.equip(ringr)
                player.equip(ringl)
                if not player > boss:
                    losses.append(player.gold)
                
print(max(losses))
