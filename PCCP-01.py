def solution(bandage, health, attacks):
    heal_stack = 0
    current_health = health
    attacks = sorted(attacks, key=lambda t: t[0])

    for time in range(1, attacks[-1][0] + 1):
        if attacks[0][0] == time:
            current_health -= attacks[0][1]
            heal_stack = 0
            del attacks[0]

            if current_health <= 0:
                current_health = -1
                break
        else:
            heal_stack += 1
            if heal_stack == bandage[0]:
                heal = bandage[1] + bandage[2]
                heal_stack = 0
            else:
                heal = bandage[1]
            current_health = min(health, current_health + heal)

    return current_health


bandage = [5, 1, 5]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
result = solution(bandage, health, attacks)

print(result)
