import sqlite3
import json

class SqlDot:
    space = ' '

    def __init__(self, database_name):
        self.db = sqlite3.connect(f'{database_name}', check_same_thread=False)
        self.sql = self.db.cursor()

    def init_table(self, struct):
        class_st = dict(vars(struct))
        
        keys_remove = ['__module__', '__doc__']
        for key in keys_remove:
            class_st.pop(key)

        self.class_name = struct.__name__
        self.vars_dict = class_st
        
        variables_dict = ', '.join({i + self.space + j for i, j in self.vars_dict.items()})

        prompt = f"""CREATE TABLE IF NOT EXISTS {self.class_name} ({variables_dict})"""
        self.sql.execute(prompt)
        self.db.commit()

    def save(self, construct):
        self.class_name = construct.__class__.__name__
        self.kw = construct.kw

        self.rows = ', '.join(row for row in self.kw)
        self.q_sym = ', '.join('?' for i in range(len(self.kw)))

        prompt = f"""INSERT INTO {self.class_name} ({self.rows}) VALUES ({self.q_sym})"""
        val_tup = tuple(value for row, value in self.kw.items())
        
        self.sql.execute(prompt, val_tup)
        self.db.commit()

class model:
    def __init__(self, **kwargs):
        self.kw = kwargs
