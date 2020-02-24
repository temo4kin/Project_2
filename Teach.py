from data import *
import random

teachers_number = []

while len(teachers_number) != 6:
    a = random.randint(0, 11)
    if a in teachers_number:
        a = random.randint(1, 16)
    else:
        teachers_number.append(a)

print(teachers_number)
for i in teachers_number:
    print(teachers[i]['name'])
