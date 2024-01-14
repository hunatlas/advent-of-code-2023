import numpy as np

with open('input.txt', 'r') as f:
    lines = f.readlines()
    play_counter = np.ones((1, len(lines)))
    for idx, line in enumerate(lines):
        winning_numbers = [int(x) for x in list(filter(lambda x: x.isdigit(), line.split('|')[0].split(':')[1].split(' ')))]
        played_numbers = [int(x) for x in filter(lambda x: x.isdigit(), list(map(lambda x: x.strip(), line.split('|')[1].split(' '))))]
        hits = len([x for x in winning_numbers if x in played_numbers])
        play_counter[0][np.arange(idx+1, idx+hits+1)] += play_counter[0][idx]
print(np.sum(play_counter).astype(int))