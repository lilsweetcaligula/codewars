def declare_winner(fighter1, fighter2, first_attacker):
    attacker = fighter1 if fighter1.name == first_attacker else fighter2
    defender = fighter2 if fighter1.name == first_attacker else fighter1
    while True:
        defender.health -= attacker.damage_per_attack
        if defender.health <= 0: 
            break
        else:
            attacker, defender = defender, attacker
    return attacker.name