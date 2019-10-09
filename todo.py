import sqlite3


def init_db():
    conn = sqlite3.connect('todo_db')

    query = '''
    CREATE TABLE IF NOT EXISTS todos
    (ID INTEGER PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    TODO INTEGER NOT NULL);
    '''

    conn.execute(query)
    conn.close()


def insert_todo(todo):
    conn = sqlite3.connect('todo_db')

    query = '''
    INSERT INTO todos (NAME, TODO)
    VALUES ("{todo_name}", 1)
    '''.format(todo_name=todo)

    conn.execute(query)
    conn.commit()
    conn.close()


def list_todo():
    conn = sqlite3.connect('todo_db')

    query = '''
    SELECT ID, NAME, TODO FROM todos WHERE TODO = 1
    '''

    cursor = conn.execute(query)

    todos = {}
    for row in cursor:
        todos[row[0]] = row[1]

    conn.close()
    return todos

def done_todo(todo_id):
    conn = sqlite3.connect('todo_db')

    query = '''
    UPDATE todos set TODO = 0 WHERE ID = {id}
    '''.format(id=int(todo_id))

    conn.execute(query)
    conn.commit()
    conn.close()

def start():
    print("Hi, welcome to Todo App. Insert below commands to use the app:")
    print('''
    - "add : <todo>" to add activity
    - "list todo" to see all todos
    - "done : <todo id>" to set todo as done

    to stop program, type "exit"
    ''')

    while True:
        inp = input('> ')
        inp = inp.split(' : ')
        input_prefix = inp[0]

        if input_prefix == 'add':
            insert_todo(inp[1])
            print('added todo ', inp[1])
        elif input_prefix == 'done':
            try:
                done_todo(inp[1])
            except ValueError:
                print('Wrong Input\ninput the number on the left side of the todo, not the name of todo')
        elif input_prefix == 'list todo':
            todos = list_todo()

            if todos:
                print('You have {} todo/s : '.format(len(todos)))
                print('The number on the left is Id to set to "done"\n')
                for key, val in todos.items():
                    print('{}-{}'.format(key, val))
            else:
                print("You don't have todo yet")
                print("To add todo, type 'add : <todo name>'")
        elif input_prefix == 'exit':
            break
        else:
            print('Command unknown. Type the listed commands')

    print('Good Bye!')


def main():
    init_db()
    start()


if __name__ == "__main__":
    main()
