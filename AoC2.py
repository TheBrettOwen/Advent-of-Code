#Advent of Code day 2
#Part 1
input = open("Input/input2.txt")
directions = []

depth = 0
horizontal = 0

for line in input:
    currentDirection = str(line)
    currentDirection = currentDirection.rstrip()

    currentDirection = currentDirection.rsplit(" ")
    if currentDirection[0] == "forward":
        horizontal = horizontal + int(currentDirection[1])
    if currentDirection[0] == "up":
        if (depth - int(currentDirection[1])) > 0:
            depth = depth - int(currentDirection[1])
        else:
            depth = 0
    if currentDirection[0] == "down":
        depth = depth + int(currentDirection[1])

finalMult = horizontal * depth

print(horizontal)
print(depth)
print(finalMult)

aim = 0
depth = 0
horizontal = 0

#Part 2
input2 = open("Input/input2.txt")

for line in input2:
    currentDirection = str(line)
    currentDirection = currentDirection.rstrip()

    currentDirection = currentDirection.rsplit(" ")
    if currentDirection[0] == "forward":
        horizontal = horizontal + int(currentDirection[1])
        depthMult = aim * int(currentDirection[1])
        if (depth + depthMult) > 0:
            depth = depth + depthMult
        else:
            depth = 0
    if currentDirection[0] == "up":
        aim = aim - int(currentDirection[1])
    if currentDirection[0] == "down":
        aim = aim + int(currentDirection[1])

finalMult2 = horizontal * depth
print(horizontal)
print(depth)
print(finalMult2)