digit_map = {
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}

sum = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        for alpha_numeric in digit_map.keys():
            alpha_numeric_found = True
            while alpha_numeric_found:
                alpha_numeric_index = line.find(alpha_numeric)
                if(alpha_numeric_index) >= 0:
                    line = line[:alpha_numeric_index+1] + digit_map[alpha_numeric] + line[alpha_numeric_index+len(alpha_numeric)-1:]
                else:
                    alpha_numeric_found = False
        numbers = list(filter(lambda c : c.isdigit(), line))
        sum += int(numbers[0] + numbers[len(numbers)-1])
print(sum)