from get_content import get_content

def get_required(f,s):
    if s == 'Z': # WIN
        if f == 'A':
            return 'B'
        elif f == 'B':
            return 'C'
        elif f == 'C':
            return 'A'
    elif s == 'Y': # DRAW
        return f
    elif s == 'X': # LOSS
        if f == 'A':
            return 'C'
        elif f == 'B':
            return 'A'
        elif f == 'C':
            return 'B'


def get_score(scores: list[str]):
    f, s = scores
    score = 0

    s = get_required(f,s)
    
    if s == 'A':
        score += 1
        if f == 'A':
            score += 3
        elif f == 'C':
            score += 6
    elif s == 'B':
        score += 2
        if f == 'B':
            score += 3
        elif f == 'A':
            score += 6
    elif s == 'C':
        score += 3
        if f == 'C':
            score += 3
        elif f == 'B':
            score += 6
    return score
    

def main():
    filename = 'day2.txt'
    content = [i.split() for i in get_content(filename).splitlines()] # A ROCK, B PAPER, C Scissors, X ROCK, Y Paper, Z scissors
    
    counter = 0
    for game in content:

        counter += get_score(game)
    print(counter)

main()
