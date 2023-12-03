import math

def calculate(pulls):
    pulls = pulls.replace(';', ',').split(',')
    
    ball_counts = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for pull in pulls:
        count, colour = pull.strip().split(' ')
        count = int(count)

        ball_counts[colour] = max(ball_counts[colour], count)

    return ball_counts
    
with open('input.txt', 'r') as f:
    res = 0
    while game := f.readline():
        game_id, game_pulls = game.strip().split(':')
        _, game_id = game_id.split(' ')
        game_id = int(game_id)

        res += math.prod(calculate(game_pulls).values()) 

    print(res)
