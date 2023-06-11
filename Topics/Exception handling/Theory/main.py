#  You can experiment here, it won’t be checked
import os

cwd = os.getcwd()
print(cwd)

os.chdir('/home/denamyte')
cwd2 = os.getcwd()
print(cwd2)

os.chdir(cwd)
print(os.getcwd())

new_dir1 = 'test_dir'
new_dir2 = 'test-dir-0/test-dir-0-0/test-dir-0-0-0'
new_dir3 = 'test-dir-0/test-dir-0-1/test-dir-0-1-0'
not os.path.exists(new_dir1) and os.mkdir(new_dir1)
not os.path.exists(new_dir2) and os.makedirs(new_dir2)
not os.path.exists(new_dir3) and os.makedirs(new_dir3)

dirs = os.listdir()
print('current directory content:', dirs)

isdirs = {name: os.path.isdir(name) for name in dirs}
print('is directory dict:', isdirs)

print('\nos.access')
print('not_existent.txt exists: ', os.access('not_existent.txt', os.F_OK))
print('task.html exists: ', os.access('task.html', os.F_OK))
print('task.html can be read: ', os.access('task.html', os.R_OK))
print('task.html can be written: ', os.access('task.html', os.W_OK))
print('task.html can be executed: ', os.access('task.html', os.X_OK))

print('\nos.path')
joined_path = os.path.join('dir1/dir2', 'dir3/dir4')
print('joined path:', joined_path)
print('split path:', os.path.split(joined_path))
print('os.path.basename:', os.path.basename(joined_path))

print('os.name:', os.name)
print('os.name:', os.uname())

