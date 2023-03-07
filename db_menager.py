import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"The error {e} occurred")


def execute_query(conn, query, data =''):
    """ Execute query in connected database """
    cursor = conn.cursor()
    try:
        if data == '':
            cursor.execute(query)
        else:
            cursor.execute(query, data)
        conn.commit()
        print("Query executed successfully")
    except Error as e:
        print(query)
        print(f"The error '{e}' occurred")


def create_todos_table(conn):
    """ Create table todos in database """
    create_users_table = """
        CREATE TABLE IF NOT EXISTS todos (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          task TEXT NOT NULL
        );
        """
    execute_query(conn, create_users_table)


def get_whole_table(conn, table):
    """ Geting whole table from connection to database """
    select_all = """SELECT * from """ + table
    cursor = conn.cursor()
    cursor.execute(select_all)
    return cursor.fetchall()


def insert_task(conn, task): 
    """ Saving new task into todos table """
    print(task)
    insert_query = ''' INSERT INTO todos (task)
              VALUES(?) '''
    execute_query(conn, insert_query, task)


def update_task(conn, old_task, new_task):
    """ Updating task in todos table """
    print(old_task, new_task)
    update_query = ''' UPDATE todos
              SET task = ?
              WHERE task = ? '''
    execute_query(conn, update_query, (old_task, new_task))


def delete_task(conn, task):
    """ Removing task from todos table """
    print(task)
    delete_query = ''' DELETE FROM todos 
                        WHERE task=? '''
    execute_query(conn, delete_query, task)