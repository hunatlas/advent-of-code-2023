score = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        winning_numbers = [int(x) for x in list(filter(lambda x: x.isdigit(), line.split('|')[0].split(':')[1].split(' ')))]
        played_numbers = [int(x) for x in filter(lambda x: x.isdigit(), list(map(lambda x: x.strip(), line.split('|')[1].split(' '))))]
        hits = len([x for x in winning_numbers if x in played_numbers])
        if hits > 0:
            score += pow(2, hits-1)
print(score)