with open('input.txt') as f:
    seq = f.readlines()

sumList = [0 for i in seq if i == '\n'] + [0]
index = 0

for calories in seq:
    if calories == '\n':
        index += 1
        continue                       
    sumList[index] += int(calories)

print('task one:', max(sumList))

topThreeSum = 0
for i in range(3):
    topThreeSum += max(sumList)
    sumList.remove(max(sumList))

print('task two:',topThreeSum)