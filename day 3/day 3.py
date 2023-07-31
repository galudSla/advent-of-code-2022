from string import ascii_letters as letters

with open('input.txt') as f:
    seq = [line.strip() for line in f.readlines()]

priorities = {letter: priority + 1 for priority, letter in enumerate(letters)}

totalSum = 0
for i in seq:
    first = set(i[:len(i)//2])
    second = set(i[len(i)//2:])
    for j in first:
        if j in second:
            totalSum += priorities[j]

print('task one:', totalSum)

totalSum1 = 0
for i in range(0, len(seq)-2, 3):
    first = set(seq[i])
    second = set(seq[i+1]) 
    third = set(seq[i+2])
    for j in first:
        if j in second and j in third:
            totalSum1 += priorities[j]
   
print('task two:', totalSum1)

