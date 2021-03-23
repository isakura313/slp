import shutil
import os
import zipfile

print("Программа, которая дублирует папку и ее содержимое")

folder = input("Введите название папки для бекапа")
# file = input("Введите название файла, который нужно откопировать")
try:
    os.mkdir(folder)
except FileExistsError:
    print("Придумайте другое имя для папки")

for file in os.listdir():
    if file.endswith('.py'):
        shutil.copy(file, folder)
shutil.make_archive(folder, 'zip')
