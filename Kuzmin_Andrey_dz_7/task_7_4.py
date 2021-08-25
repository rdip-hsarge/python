import os

data_dict = {}
interesting_folder = 'exmpl'
size_degree = []

for root, dirs, files in os.walk(interesting_folder):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        degree = 10

        while size > 10:
            size = size / 10
            degree = degree * 10

        size_degree.append(degree)
        data_dict[degree]=size_degree.count(degree)

data_dict = dict(sorted(data_dict.items(), key = lambda x: x[0]))
print(data_dict)
