import sqlite3

FILENAME = 'clients.db'


def getConnection():
    return sqlite3.connect(FILENAME)


def migrateTable():
    with getConnection() as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS clients")
        cursor.execute("""CREATE TABLE clients
                          (first_name text, last_name text, birthday date, sex text, credit_amount int, tel text)
                       """)


def readData():
    with getConnection() as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM clients WHERE birthday = (SELECT MAX(birthday) FROM clients)')
        print("Youngest client: ", cursor.fetchone())

        cursor.execute('SELECT SUM(credit_amount) FROM clients')
        print("Sum of credits: ", cursor.fetchone()[0])


def inputData():
    with getConnection() as conn:
        cursor = conn.cursor()

        first_name = input('first_name: ')
        last_name = input('last_name: ')
        birthday = input('birthday (y.m.d): ')
        sex = input('sex: ')
        credit_amount = input('credit_amount: ')
        tel = input('tel: ')

        cursor.execute('INSERT INTO clients VALUES (?, ?, ?, ?, ?, ?)',
                       (first_name, last_name, birthday, sex, credit_amount, tel))


def processCommand(cmd):
    if cmd == 'exit':
        return False
    elif cmd == 'migrate':
        migrateTable()
    elif cmd == 'read':
        readData()
    elif cmd == 'write':
        inputData()
    else:
        print('Unknown command')

    return True


print('> Available commands: migrate, read, write, exit')

continueLoop = True
while continueLoop:
    command = input('> Enter command: ')
    continueLoop = processCommand(command)
