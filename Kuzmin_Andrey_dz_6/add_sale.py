from sys import argv

with open('backery.csv', 'a') as add:
    for sale in argv[1:]:
        add.writelines(f'{sale}\n')