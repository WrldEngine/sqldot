space = ' '

data_types = {
    'int': 'INTEGER',
    'text': 'TEXT',
    'real': 'REAL',
    'primary_key': 'PRIMARY KEY AUTOINCREMENT',
    'blob': 'BLOB',
    'unique': 'UNIQUE'
}

def Integer(primary_key=False):
    set_type = data_types['int']
    if primary_key: set_type += space + data_types['primary_key']

    return set_type

def Text(unique=False):
    set_type = data_types['text']
    if unique: set_type += space + data_types['unique']

    return set_type

def Real(unique=False):
    set_type = data_types['real']
    if unique: set_type += space + data_types['unique']

    return set_type

def Blob(unique=False):
    set_type = data_types['blob']
    if unique: set_type += space + data_types['unique']

    return set_type