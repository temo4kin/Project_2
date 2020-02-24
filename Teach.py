from data import *
import random
import pprint

teachers_number = []

while len(teachers_number) != 1:
    a = random.randint(0, 11)
    if a in teachers_number:
        a = random.randint(1, 16)
    else:
        teachers_number.append(a)

print(teachers_number)
for i in teachers_number:
    print(teachers[i]['name'])

work_week = []
for i in teachers_number:
    for day in teachers[i]['free']:
        days_new = {x: True for x in teachers[i]['free'][day].keys() if teachers[i]['free'][day][x] == True}
        days_name = {x: True for x in teachers[i]['free'].keys()}
        work_week.append(days_new)
print(work_week)
print(days_name)

for i in teachers_number:
    for day in teachers[i]['free']:
        print(day)
'''
взять сипском dict.keys() и dict.values()
и сформировать новый словрь dict.fromkeys из списка dict.keys()
с индексами dict.values() у которых True
'''
#pprint.pprint(teachers[i]['free'])
keys = teachers[i]['free']['mon'].keys()
values = teachers[i]['free']['mon'].values()
#print(keys)
#print(values)
monday = teachers[i]['free']['mon']
#print(monday)

monday_new = {x: True for x in monday.keys() if monday[x] == True}

#print(days_new)

        

#work_week.update(

'''
for i in teachers_number:
    for key, value in teachers[i]['free']:
        for val in value:
            print(val)


pprint.pprint(teachers[i]['free'])


 # импортируем библиотеку random
import random


# читаем файл в список
# file - название файла
def read2list(file):
    # открываем файл в режиме чтения utf-8
    file = open(file, 'r', encoding='utf-8')

    # читаем все строки и удаляем переводы строк
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]
   
    # закрываем файл
    file.close()
   
    # возвращаем список строк из файла
    return lines


# возвращает 5 случайных вопросов
def get_questions(numberOfAnswers = 5):
    # получаем список строк из файла
    answers = read2list('answers_data.txt')
   
    # выбираем 5 случайных строк из списка с помощью встроенной функции choices
    items = random.choices(population=answers, k=numberOfAnswers)

    # или такой вариант
    items = random.shuffle(teach_list)
   
    # возвращаем список
    return items
'''
