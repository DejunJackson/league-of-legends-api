"""This module holds the constructor class for each champion object. 
The serialize method returns a dictionary of the stats that is ready to be transformed into json"""


class Champion:
    def __init__(self, name, hp, hp_gain_per_lvl, hp_regen, hp_regen_gain_per_lvl, mana, mana_gain_per_lvl, mana_regen, mana_regen_per_lvl, attack_damage, attack_damage_gain_per_lvl, attack_speed, attack_speed_gain_per_lvl,
    armor, armor_gain_per_lvl, magic_resist, magic_resist_gain_per_lvl, movement_speed, range_):
        self.name = name
        self.hp = hp
        self.hp_gain_per_lvl = hp_gain_per_lvl
        self.hp_regen = hp_regen
        self.hp_regen_gain_per_lvl = hp_regen_gain_per_lvl
        self.mana = mana
        self.mana_gain_per_lvl = mana_gain_per_lvl
        self.mana_regen = mana_regen
        self.mana_regen_gain_per_lvl = mana_regen_per_lvl
        self.attack_damage = attack_damage
        self.attack_damage_gain_per_lvl = attack_damage_gain_per_lvl
        self.attack_speed = attack_speed
        self.attack_speed_gain_per_lvl = attack_speed_gain_per_lvl
        self.armor = armor
        self.armor_gain_per_lvl = armor_gain_per_lvl
        self.magic_resist = magic_resist
        self.magic_resist_gain_per_lvl = magic_resist_gain_per_lvl
        self.movement_speed = movement_speed
        self.range = range_
        self.ability_power = 0
        self.crit = 0

    def serialize(self):
        return{
            'name': self.name,
            'hp': self.hp,
            'hp_gain_per_lvl': self.hp_gain_per_lvl,
            'hp_regen': self.hp_regen,
            'hp_regen_gain_per_lvl': self.hp_regen_gain_per_lvl,
            'mana': self.mana,
            'mana_gain_per_lvl': self.mana_gain_per_lvl,
            'mana_regen': self.mana_regen,
            'mana_regen_gain_per_lvl': self.mana_regen_gain_per_lvl,
            'attack_damage': self.attack_damage,
            'attack_damage_gain_per_lvl': self.attack_damage_gain_per_lvl,
            'attack_speed': self.attack_speed,
            'attack_speed_gain_per_lvl': self.attack_speed_gain_per_lvl,
            'armor': self.armor,
            'armor_gain_per_lvl': self.armor_gain_per_lvl,
            'magic_resist': self.magic_resist,
            'magic_resist_gain_per_lvl': self.magic_resist_gain_per_lvl,
            'movement_speed': self.movement_speed,
            'range': self.range,
            'ability_power': self.ability_power,
            'crit': self.crit
        }