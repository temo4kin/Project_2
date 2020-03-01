import json
from pprint import pprint
from data import *

client_weekday = "mon"
client_time = "8:00"
client_teacher = "10"
client_name = "Artem"
client_phone = "+7 917 070-44-10"


client = dict(weekday = client_weekday, 
time = client_time,
teacher = int(client_teacher),
name = client_name,
phone = client_phone)

pprint(client)
print('\n\n\n')



with open("booking.json", "w") as f:
    json.dump(client, f)

with open("booking.json", "r") as f:
    my_list = json.load(f)

pprint(my_list)
