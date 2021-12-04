#Advent of Code day 1
#Part 1
input = open("Input/input.txt")
increases = 0
numbers= []
i = 0

for line in input:
    inputNum = int(line)
    numbers.append(inputNum)

    if (len(numbers) >= 2):
        if (numbers[i] > numbers[i-1]):
            increases = increases + 1
    i = i + 1
    

print("First increases:", increases)

#Part 2
input = open("Input/input.txt")
increases = 0
newNumbers= []
i = 0

for line in input:
    inputNum = int(line)
    newNumbers.append(inputNum)

    if (len(numbers) > 4):
        triplet1 = numbers[i] + numbers[i-1] + numbers[i-2]
        triplet2 = numbers[i-1] + numbers[i-2] + numbers[i-3]
        if triplet1 > triplet2:
            increases = increases + 1

    i = i + 1
    

print("Second increases:", increases)