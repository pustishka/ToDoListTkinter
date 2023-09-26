from typing import Any

import sqlalchemy as db
from sqlalchemy import delete, update

engine = db.create_engine('sqlite:///tasks.db')  # create db engine sqlalchemy
connection = engine.connect()  # connection to engine
metadata = db.MetaData()  # wrapper db
tasks = db.Table('tasks', metadata,
                 db.Column('task', db.Text))  # custom table in db with 'task' column
metadata.create_all(engine)  # creating db and table


# adding function in db
def add_task(entry_data: str):
    new_task = tasks.insert().values({'task': entry_data})  # insert record in table
    result = connection.execute(new_task)
    return result


# getting function in db
def get_tasks():
    records = db.select([tasks])  # select query with all records in table
    results = connection.execute(records).fetchall()
    return results


# deleting function in db
def del_task(name: str) -> Any:
    record = delete(tasks).where(tasks.columns.task == name)  # delete record from table where task equel name Listbox
    result = connection.execute(record)
    return result


# editing function in db
def edit_task(name: str, new_name: str) -> Any:
    record = update(tasks).where(tasks.columns.task == name).values(task=new_name)  # update with name from listbox
    result = connection.execute(record)
    return result
