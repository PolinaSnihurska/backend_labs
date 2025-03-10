def parse_cubes(cube_str):
    red, green, blue = 0, 0, 0
    cube_list = cube_str.split(', ')
    for cube in cube_list:
        count, color = cube.split(' ')
        count = int(count)
        if color == 'red':
            red += count
        elif color == 'green':
            green += count
        elif color == 'blue':
            blue += count
    return red, green, blue

def is_game_possible(game_data, bag_capacity):
    game_lines = game_data.split('; ')
    for line in game_lines:
        red, green, blue = parse_cubes(line)
        if red > bag_capacity[0] or green > bag_capacity[1] or blue > bag_capacity[2]:
            return False
    return True

def main():
    bag_capacity = [12, 13, 14]
    
    games = {}
    
    with open('input_5.txt', 'r') as file:
        for line in file:
            game_id, game_data = line.strip().split(': ')
            game_id = int(game_id.split(' ')[1])
            games[game_id] = game_data
    
    possible_games = []
    
    for game_id, game_data in games.items():
        if is_game_possible(game_data, bag_capacity):
            possible_games.append(game_id)
    
    total_sum = sum(possible_games)
    print('Possible games:', possible_games)
    print('Sum of IDs of possible games:', total_sum)

if __name__ == '__main__':
    main()
