def calculate_score(opponent_move, your_move):
    move_scores = {'X': 1, 'Y': 2, 'Z': 3}
    outcomes = {
        ('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
        ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
        ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3
    }
    score = move_scores[your_move] + outcomes[(opponent_move, your_move)]
    return score

def main():
    with open('input_6.txt', 'r') as file:
        total_score = 0
        for line in file:
            opponent_move, your_move = line.strip().split(' ')
            round_score = calculate_score(opponent_move, your_move)
            total_score += round_score
    
    print('Total score:', total_score)

if __name__ == '__main__':
    main()
