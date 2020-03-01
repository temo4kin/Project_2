from data import *
import random
import pprint

goal = 'study'
teachers_goal = []
for teacher in teachers:
    if goal in teacher['goals']:
        teachers_goal.append(teacher)

#pprint.pprint(teachers_goal)

goals = {"travel": ["⛱", "Для путешествий"], "study": ["🏫", "Для учебы"], "work": ["🏢", "Для работы"], "relocate": ["🚜", "Для переезда"]}

for goal in goals:
    print(goals[goal][0])
