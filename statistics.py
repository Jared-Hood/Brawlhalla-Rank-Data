import math

def stdDev(file, average):
    new_average = 0
    iter = 0
    for line in file:
        new_average += (int(line) - average) ** 2
        iter += 1

    new_average = new_average / iter

    return math.sqrt(new_average)


file = open("output.txt",'r')

#statistics
maxElo = int(file.__next__())
minElo = maxElo
average = 0
mode = 0
median = 0
Std = 0

frequency = [0] * (maxElo + 1)

lines = 0
for line in file:
    frequency[int(line)] += 1
    lines += 1
    average += int(line)
    if (int(line) < minElo):
        minElo = int(line)

average = average / lines

file.close()
file = open("output.txt",'r')
Std = stdDev(file, average)
file.close()
file = open("output.txt",'r')

iter2 = 0
for line in file:
    if (iter2 == lines //2):
        median = int(line)
        break
    else:
        iter2 += 1

modeNum = 0
for i in frequency:
    if(int(i) > modeNum):
        modeNum = int(i)
        mode = frequency.index(modeNum)

print("Max Elo: " + str(maxElo))
print("Min Elo: " + str(minElo))
print("Mode: " + str(mode))
print("Number of occurances: " + str(modeNum))
print("Average: " + str(round(average,2)))
print("Median: " + str(median))
print("Standard Deviation: " + str(round(Std,2)))

file.close()


