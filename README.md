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
---
### Supported datatypes:
```REAL``` - ```Real()``` <br>
```TEXT``` - ```Text()``` <br>
```INTEGER``` - ```Integer()``` <br>
```BLOB``` - ```Blob()``` <br>
---
### Desc
- Connect to Database: ```db = SqlDot('some.db')```
- Create table: ```db.init_table(table_class)```
- Set variables: ```setter = table_class(row1=var1, row2=var2)```
- Save to db: ```db.save(setter)```
