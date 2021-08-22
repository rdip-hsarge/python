from sys import argv

manual = argv[1:]
with open('backery.csv', 'r', encoding='utf-8') as show:
    if len(argv) == 1:
        print(show.read())
    elif len(argv) == 2:
        for line in show.readlines()[int(argv[1])-1:]:
            print(line.replace('\n', ''))
    elif len(argv) == 3:
        for line in show.readlines()[int(argv[1]) - 1: int(argv[2])]:
            print(line.replace('\n', ''))