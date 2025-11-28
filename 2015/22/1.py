'''
--- Day 22.1: Wizard Simulator 20XX ---

'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    stats = [int(line.rstrip().split(': ')[1]) for line in f.readlines()]

class Character:

    def __init__(
        self, 
        life: int, 
        damage: int = 0, 
        armor: int = 0, 
        mana: int = 0,
        role: str = 'player'
        ):
        self.life = life
        self.damage = damage
        self.armor = armor
        self.mana = mana
        self.role = role

        self.shield_timer = 0
        self.poison_timer = 0
        self.recharge_timer = 0

    def __repr__(self):
        return str(self.__dict__)
    
    def receive_damage(self, damage: int):
        if damage == 0: return
        net_damage = damage - self.armor
        net_damage = 1 if net_damage < 1 else net_damage
        self.life -= net_damage

    def cast(self, spell: str, other: 'Character'):
        # Basic attributes
        cost, damage, healing, turns, effect = spell_store[spell]
        self.mana -= cost
        other.receive_damage(damage)
        self.life += healing
        # Effect attributes
        if spell == 'shield':
            self.shield_timer = turns
            self.armor += 7
        if spell == 'poison':
            self.poison_timer = turns
        if spell == 'recharge':
            self.recharge_timer = turns 

    def available_spells(self):
        # Insufficient mana
        if self.mana < 53:
            return set()
        elif self.mana < 73:
            spells = {'magic_missile'}
        elif self.mana < 113:
            spells = {'magic_missile', 'drain'}
        elif self.mana < 173:
            spells = {'magic_missile', 'drain', 'shield'}
        elif self.mana < 229:
            spells = {'magic_missile', 'drain', 'shield', 'poison'}
        else:
            spells = {'magic_missile', 'drain', 'shield', 'poison', 'recharge'}
        # Effect active 
        if self.shield_timer:
            spells = spells - set(('shield'))
        if self.poison_timer:
            spells = spells - set(('poison'))
        if self.recharge_timer:
            spells = spells - set(('recharge'))
        return spells

class Fight:
    
    def __init__(self, player, boss):
        self.player = player
        self.boss = boss
        self.turns = 0
        self.winner = None

    def check_winner(self):
        if self.boss.life <= 0:
            self.winner = self.player
            print('Player wins!')
            return
        if self.player.life <= 0:
            self.winner = self.boss
            print('Boss wins!')
            return

    def start_turn(self):
        # Winner check
        self.check_winner()
        # Increment turn counter
        self.turns += 1
        # Reduce timer
        shield_timer_start = self.player.shield_timer
        self.player.shield_timer -= 1 if self.player.shield_timer else 0
        self.player.poison_timer -= 1 if self.player.poison_timer else 0
        self.player.recharge_timer -= 1 if self.player.recharge_timer else 0
        # Apply effects
        if shield_timer_start and not self.player.shield_timer:
            self.player.armor -= 7
        if self.player.poison_timer > 0:
            self.boss.receive_damage(3)
        if self.player.recharge_timer > 0:
            self.player.mana += 101        
    
    def player_attacks(self, spell = None):
        # Available spells
        spells = self.player.available_spells()
        # Defeat by lack of options
        if not spells:
            self.player.receive_damage(self.player.life)
        # Winner check
        self.check_winner()
        #CHOSE SPELL HEREEEEEEEEEEEE
        spell = spell
        # Cast spell
        self.player.cast(spell, self.boss)

    def boss_attacks(self):
        # Winner check
        self.check_winner()
        # Boss atack
        self.player.receive_damage(self.boss.damage)

    def turn(self, spell):
        if not self.winner:
            self.start_turn()
        if not self.winner:
            print('-----------------PLAYER-----------------')
            print(self.player)
            print(self.boss)
            self.player_attacks(spell)
        
        if not self.winner:
            self.start_turn()
        if not self.winner:
            print('-----------------BOSSSS-----------------')
            print(self.player)
            print(self.boss)
            self.boss_attacks()

spell_store = {
    'magic_missile': (53, 4, 0, 0, 0),
    'drain': (73, 2, 2, 0 ,0),
    'shield': (113, 0, 0, 6, 7),
    'poison': (173, 0, 0, 6, 3),
    'recharge': (229, 0, 0, 5, 101)
}


player = Character(10, 0, 0, 250, 'Player')
boss = Character(14, 8, 0 , 0, 'Boss')
game = Fight(player, boss)
game.turn('recharge')
game.turn('shield')
game.turn('drain')
game.turn('poison')
game.turn('magic_missile')
