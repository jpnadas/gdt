from mongoengine import connect
import sys


if len(sys.argv) > 1:
    database_name = sys.argv[1]
else:
    database_name = input("Which database do you want to drop?")

opt = 'n'

opt = input(f'Are you sure you want to drop {database_name}?(y/N) ')
if opt == 's':
    print('nothing to do')
else:
    response = input(f'In order to drop the database, you must type its name ({database_name}) again:\n')
    if response == database_name:
        print(f'no more turning back... dropping {database_name}.')
        db = connect(database_name)
        db.drop_database(database_name)
