from sqldot import *
from dtypes import *

db = SqlDot('manage.db')

class Users(model):
    id = Integer(primary_key=True)
    username = Text(unique=True)
    name = Text()

def choice():
	name = input("Name: ")
	user = input("Username: ")

	data_save = Users(name=name, username=user)
	db.save(data_save)

def show():
	names = db.select(Users)
	for name in names:
		print(name)

	print("")
	
	any_people = db.select_where(Users, name="Isko")
	for i in any_people:
		print(i)

if __name__ == "__main__":
	db.init_table(Users)
	show()