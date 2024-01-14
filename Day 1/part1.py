sum = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        numbers = list(filter(lambda c : c.isdigit(), line))
        sum += int(numbers[0] + numbers[len(numbers)-1])
print(sum)