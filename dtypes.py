space = ' '

data_types = {
    'int': 'INTEGER',
    'text': 'TEXT',
    'real': 'REAL',
    'primary_key': 'PRIMARY KEY AUTOINCREMENT',
    'bool': 'BOOLEAN'
    'blob': 'BLOB',
    'unique': 'UNIQUE',
    'nullable': 'NOT NULL'
}

def Integer(primary_key=False, unique=False):
    set_type = data_types['int']

    if primary_key: set_type += space + data_types['primary_key']
    if unique: set_type += space + data_types['unique']

    return set_type

def Text(unique=False, nullable=True):
    set_type = data_types['text']

    if unique: set_type += space + data_types['unique']
    if not nullable: set_type += space + data_types['nullable']

    return set_type

def Real(unique=False, nullable=True):
    set_type = data_types['real']

    if unique: set_type += space + data_types['unique']
    if not nullable: set_type += space + data_types['nullable']

    return set_type

def Blob(unique=False, nullable=True):
    set_type = data_types['blob']

    if unique: set_type += space + data_types['unique']
    if not nullable: set_type += space + data_types['nullable']

    return set_type

def Bool(nullable=True):
    set_type = data_types['bool']
    if not nullable: set_type += space + data_types['nullable']

    return set_type