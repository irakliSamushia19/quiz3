import requests
import json
import sqlite3


key = 'b0382a9da8d31051dd5eecdc220673dc'
num = int(input("Enter the page: "))
playload = {'id': num, 'appid': key}
r = requests.get(f'https://anapioficeandfire.com/api/characters/{num}')

result_json = r.text
res = json.loads(result_json)
res_structured = json.dumps(res, indent=4)
print(res_structured)
print(r.raise_for_status())
print(r.status_code)
print(r.headers)

with open('data.json', 'w') as file:
    object = json.dump(res, file, indent=4)


name = res['name']
actor = res['playedBy'][0]
aliases = res['aliases'][0]
print(name, "-ს როლს თამაშობს", actor, '-ი')


'''მოცემულ ცხრილში შემაქ მსახიობის სახელი, მისი პერსონაჟი და პერსონაჟის ყველაზე გავრცელებული მეტსახელი'''
conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor()

my = (actor, name, aliases)
#cursor.execute('''CREATE TABLE actors(id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     Actor varchar (50),
#                     Character varchar (50),
#                     Nickname varchar (50))''')

cursor.execute('INSERT INTO actors(Actor, Character, Nickname) VALUES (?,?,?)', my)
conn.commit()















