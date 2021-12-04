#Advent of Code Day 3
#Part 1
from os import pipe, popen
from typing import Generator


input = open("Input/input3.txt")
binaryNums = [] #has 1000 values at the end
oxygen = []
scrubber = []


for line in input: 
    currNum = str(line)
    currNum = currNum.rstrip()
    oxygen.append(currNum)
    scrubber.append(currNum)
    binaryNums.extend(currNum) 

sum = 0
digitTotals = [0]*12
gamma = [""]*12
epsilon = [""]*12

for i in range(0, len(binaryNums)):
    digitTotals[i%12] = digitTotals[i%12] + int(binaryNums[i])

print(digitTotals)

for i in range(0, len(digitTotals)):
    if (digitTotals[i] > 499):
        gamma[i] = "1"
        epsilon[i] = "0"
    else:
        gamma[i] = "0"
        epsilon[i] = "1"

#for use in part 2 
gammaBin = gamma
epsilonBin = epsilon

#part one finish
gamma = "".join(gamma)
gamma = int(gamma, 2)
epsilon = "".join(epsilon)
epsilon = int(epsilon, 2)
print("Part one:")
print(gamma)
print(epsilon)
print(gamma * epsilon)


# part 2