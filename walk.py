import os


def walk(start_path: str = '/', level=0):

    items = os.listdir(start_path)

    for item in items:

        if level == 0:
            print(item)
        else:
            print('│   ' * (level-1) + '├── ' + item)

        if start_path =='/':
            path = start_path + item
        else:
            path = start_path + '/' + item

        try:
            walk(path, level+1)
        except OSError:
            pass


walk()
