import os

with open('conf.yaml', 'r') as conf:
    for line in conf.readlines():
        paths = line.split(' ')[0]
        files = line.split(' ')[1:]
        if paths == 'base':
            os.mkdir(line.split(' ')[1].replace('\n', ''))
            os.chdir(line.split(' ')[1].replace('\n', ''))
            paths=os.path.join(line.split(' ')[1].replace('\n', ''), paths)
            continue
        else:
            if not os.path.exists(paths):
                os.makedirs(paths)
                for file in files:
                    with open(os.path.join(paths, file.replace('\n', '')), 'w'):
                        pass