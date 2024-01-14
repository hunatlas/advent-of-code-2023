with open('input.txt', 'r') as f:
    lines = f.readlines()

sum = 0
for r,line in enumerate(lines):
    for c,char in enumerate(line):
        if char != '.' and char != '\n' and not char.isdigit():
            print('Symbol ' + char + ' found at (' + str(r) + ',' + str(c) + ')')
            if r == 0 and c == 0:
                indexes = [(r, c+1), (r+1, c), (r+1, c+1)]
            elif r == 0 and c == len(line) - 1:
                indexes = [(r, c-1), (r+1, c-1), (r+1, c)]
            elif r == len(lines) - 1 and c == 0:
                indexes = [(r-1, c), (r-1, c+1), (r, c+1)]
            elif r == len(lines) - 1 and c == len(line) - 1:
                indexes = [(r-1, c-1), (r-1, c), (r, c-1)]
            elif r == 0:
                indexes = [(r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]
            elif r == len(lines) - 1:
                indexes = [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1)]
            elif c == 0:
                indexes = [(r-1, c), (r-1, c+1), (r, c+1), (r+1, c), (r+1, c+1)]
            elif c == len(line) - 1:
                indexes = [(r-1, c-1), (r-1, c), (r, c-1), (r+1, c-1), (r+1, c)]
            else:
                indexes = [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]
            print('Indexes to check: ', indexes)
            for coord in indexes:
                char_to_check = lines[coord[0]][coord[1]]
                if char_to_check.isdigit():
                    print('Digit found: ', char_to_check)
                    number = char_to_check
                    lines[coord[0]] = lines[coord[0]][:coord[1]] + '.' + lines[coord[0]][coord[1]+1:]
                    x_before = coord[1] - 1
                    x_after = coord[1] + 1
                    y = coord[0]
                    while x_before >= 0 and lines[y][x_before].isdigit():
                        number = lines[y][x_before] + number
                        lines[y] = lines[y][:x_before] + '.' + lines[y][x_before+1:]
                        x_before -= 1
                    while x_after <= len(line) - 1 and lines[y][x_after].isdigit():
                        number = number + lines[y][x_after]
                        lines[y] = lines[y][:x_after] + '.' + lines[y][x_after+1:]
                        x_after += 1
                    print('Number ' + number + ' constructed.')
                    sum += int(number)
print('Sum of used parts numbers: ', sum)