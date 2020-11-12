import shelve
from datetime import datetime

from task1.Client import Client

FILENAME = "db\\shelve_data"


def getYoungestClient(clients):
    first_comparsion = True
    result = None

    for client in clients:
        if first_comparsion or client.birthday > result.birthday:
            first_comparsion = False
            result = client

    return result


def getCreditsSum(clients):
    return sum(map(lambda c: c.credit_amount, clients))


def printData():
    try:
        with shelve.open(FILENAME) as db:
            clients = db.values()

            if clients:
                print('Youngest client: ', getYoungestClient(clients))
                print('Credits sum: ', getCreditsSum(clients))
            else:
                print('Database is empty')
    except FileNotFoundError:
        print('Database file not found')


def inputData():
    first_name = input('first_name: ')
    last_name = input('last_name: ')
    birthday = input('birthday (y.m.d): ').split('.')
    sex = input('sex: ')
    credit_amount = input('credit_amount: ')
    tel = input('tel: ')

    client = Client(
        first_name,
        last_name,
        datetime(year=int(birthday[0]), month=int(birthday[1]), day=int(birthday[2])),
        sex,
        int(credit_amount),
        tel
    )

    with shelve.open(FILENAME) as clients:
        clients[str(hash(client))] = client

    print('Record saved')


def processCommand(cmd):
    if cmd == 'exit':
        return False
    elif cmd == 'read':
        printData()
    elif cmd == 'write':
        inputData()
    else:
        print('Unknown command')

    return True


print('> Available commands: read, write, exit')

continueLoop = True
while continueLoop:
    command = input('> Enter command: ')
    continueLoop = processCommand(command)
