MAX_RED = 12
MAX_BLUE = 14
MAX_GREEN = 13

cubes_dict = {
    'red' : 0,
    'blue' : 0,
    'green' : 0
}

possible_games_sum = 0
sum_of_power_of_min_cubes = 0
with open('input.txt', 'r') as f:
    for game, line in enumerate(f.readlines()):
        for round in line.split(':')[1].split(';'):
            for draw in round.split(','):
                if int(draw.split()[0]) > cubes_dict[draw.split()[1]]:
                    cubes_dict[draw.split()[1]] = int(draw.split()[0])
        if cubes_dict['red'] <= MAX_RED and cubes_dict['blue'] <= MAX_BLUE and cubes_dict['green'] <= MAX_GREEN:
            possible_games_sum += game + 1
        sum_of_power_of_min_cubes += cubes_dict['red'] * cubes_dict['blue'] * cubes_dict['green']
        cubes_dict['red'] = 0
        cubes_dict['blue'] = 0
        cubes_dict['green'] = 0
print(possible_games_sum)
print(sum_of_power_of_min_cubes)