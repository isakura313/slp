import os
import shutil
import glob

print(os.name)
print(os.listdir())  # перечисляение директорий
print(os.getcwd())
path = os.getcwd()
# for i in range(10):
#     os.mkdir(str(i))
# try:
#     os.mkdir('backup')
# except FileExistsError:
#     os.rmdir('backup')
# for i in os.listdir():
#     if i.endswith('.py'):
#         shutil.copyfile(i, path + '/backup')

# for i in glob.glob('*.py'):
    # shutil.copyfile(i, path + '/backup/')
# os.remove('code.sh')
shutil.rmtree('backup')












