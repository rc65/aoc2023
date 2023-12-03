limits = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def possible(pulls):
    pulls = pulls.replace(';', ',').split(',')

    for pull in pulls:
        count, colour = pull.strip().split(' ')
        count = int(count)

        if count > limits[colour]:
            return False
    
    return True

with open('input.txt', 'r') as f:
    res = 0
    while game := f.readline():
        game_id, game_pulls = game.strip().split(':')
        _, game_id = game_id.split(' ')
        game_id = int(game_id)

        if possible(game_pulls):
            res += game_id

    print(res)


