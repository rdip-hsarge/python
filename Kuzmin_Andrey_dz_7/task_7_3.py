import os

for root, dirs, files in os.walk('my_project'):
    new_folder_root = os.path.join('templates', os.path.relpath(root, 'my_project'))
    if not os.path.exists(new_folder_root):
        os.makedirs(os.path.join('templates', os.path.relpath(root, 'my_project')))