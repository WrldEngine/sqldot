# Sqldot
Simpliest ORM on Sqlite3

### How to use:
```
from sqldot import *
from dtypes import *

db = SqlDot('manage.db')

class Users(model):
    id = Integer(primary_key=True)
    username = Text(unique=True)
    name = Text()

db.init_table(Users)

user = input('username')
name = input('name')

new_user = Users(username=user, name=name)
db.save(new_user)
```
