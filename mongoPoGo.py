
from datetime import datetime

# Connection URI
uri = 'mongodb://localhost:27017'
client = (uri)


CharmanderStats = {
    'Name': 'Charmander', 
    'Attack': 116, 
    'Defense': 93, 
    'Stamina': 118, 
    'CPMax': 1108, 
    'Type': 'Fire', 
    'Fast Moves': ['Ember', 'Scratch'], 
    'Charged Moves': ['Flamethrower', 'Flame Burst', 'Flame Charge'], 
    'Weaknesses': ['Water', 'Ground', 'Rock'], 
    'Resistances': ['Fire', 'Grass', 'Ice', 'Bug', 'Steel', 'Fairy'], 
    'Boosted Weather': ['Sunny'], 
    'Raid Attacker': ['Unranked'], 
    'Gym Defender': ['Unranked'], 
    'Competitive Tier': 'Unranked', 
    'Fire Type Attacker': 'Unranked',
    'Best Moveset': 'Ember & Flamethrower',
    'DPS': 4.79,
    'TDO': 32.09
    }

CharmeleonStats = {
    'Name': 'Charmeleon', 
    'Attack': 158, 
    'Defense': 126, 
    'Stamina': 151, 
    'CPMax': 1868, 
    'Type': 'Fire', 
    'Fast Moves': ['Ember', 'Scratch', 'Fire Fang'], 
    'Charged Moves': ['Flamethrower', 'Flame Burst', 'Fire Fang'], 
    'Weaknesses': ['Water', 'Ground', 'Rock'], 
    'Resistances': ['Fire', 'Grass', 'Ice', 'Bug', 'Steel', 'Fairy'], 
    'Boosted Weather': ['Sunny'], 
    'Raid Attacker': ['Unranked'], 
    'Gym Defender': ['Unranked'], 
    'Competitive Tier': 'C Tier Great League', 
    'Fire Type Attacker': 'F Tier',
    'Best Moveset': 'Fire Fang & Flamethrower',
    'DPS': 8.33,
    'TDO': 90.90
}

CharizardStats = {
    'Name': 'Charizard',
    'Attack': 223,
    'Defense': 173,
    'Stamina': 186,
    'CPMax': 3266,
    'Type': 'Fire/Flying',
    'Fast Moves': ['Fire Spin', 'Air Slash', 'Wing Attack', 'Dragon Breath', 'Ember'],
    'Charged Moves': ['Blast Burn', 'Overheat', 'Dragon Claw', 'Flamethrower', 'Fire Blast', 'Air Cutter'],
    'Weaknesses': ['Water', 'Electric', '2x Rock'],
    'Resistances': ['Fire', '2x Grass', 'Fighting', '2x Bug', 'Steel', 'Fairy'],
    'Boosted Weather': ['Sunny', 'Windy'],
    'Raid Attacker': ['F Tier'],
    'Gym Defender': ['D Tier'],
    'Competitive Tier': ['B tier Great League', 'B Tier Ultra League', 'C Tier Master League'],
    'Fire Type Attacker': 'B Tier',
    'Flying Type Attacker': 'F Tier',
    'Best Moveset': 'Fire Spin & Blast Burn',
    'DPS': 14.01,
    'TDO': 246.72}

CharizardXStats = {
    'Name': ' Mega Charizard X',
    'Attack': 273,
    'Defense': 213,
    'Stamina': 186,
    'CPMax': 4353,
    'Type': 'Fire/Dragon',
    'Fast Moves': ['Fire Spin', 'Dragon Breath', 'Wing Attack', 'Air Slash'],
    'Charged Moves': ['Blast Burn', 'Dragon Claw', 'Flamethrower', 'Fire Blast', 'Overheat', 'Air Cutter'],
    'Weaknesses': ['Ground', 'Rock', 'Dragon'],
    'Resistances': ['2x Fire', '2x Grass', 'Electric', 'Bug', 'Steel'],
    'Boosted Weather': ['Sunny', 'Windy'],
    'Raid Attacker': ['A Tier'],
    'Gym Defender': ['Unranked'],
    'Competitive Tier': ['Unranked'],
    'Fire Type Attacker': 'S Tier',
    'Dragon Type Attacker': 'B Tier',
    'Best Moveset': 'Fire Spin & Blast Burn',
    'DPS': 17.02,
    'TDO': 363.63
}

CharizardYStats = {
    'Name': ' Mega Charizard Y',
    'Attack': 319,
    'Defense': 212,
    'Stamina': 186,
    'CPMax': 5037,
    'Type': 'Fire/Flying',
    'Fast Moves': ['Fire Spin', 'Air Slash', 'Wing Attack', 'Dragon Breath', 'Ember'],
    'Charged Moves': ['Blast Burn', 'Overheat', 'Dragon Claw', 'Flamethrower', 'Fire Blast', 'Air Cutter'],
    'Weaknesses': ['Water', 'Electric', '2x Rock'],
    'Resistances': ['Fire', '2x Grass', 'Fighting', '2x Bug', 'Steel', 'Fairy', 'Ground'],
    'Boosted Weather': ['Sunny', 'Windy'],
    'Raid Attacker': ['A+ Tier'],
    'Gym Defender': ['Unranked'],
    'Competitive Tier': ['Unranked'],
    'Fire Type Attacker': 'S Tier',
    'Flying Type Attacker': 'A+ Tier',
    'Best Moveset': 'Fire Spin & Blast Burn',
    'DPS': 19.68,
    'TDO': 418.62
}
