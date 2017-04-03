import subprocess
import glob
import os.path
import shutil

folder_name = 'Result'

def make_folder():
    #создание папки для полученных изображений
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

def resize_img(filename, directory):
    subprocess.run(["sips", "--resampleWidth", "200", os.path.join(directory, folder_name, filename.split('/')[1])])

def copy_and_resize (file_list, directory):
    #цикл, копирующий изображения и изменяющий размер
    for f in file_list:
        shutil.copy(os.path.join(directory, f), os.path.join(directory, folder_name, f.split('/')[1]))
        resize_img(f)

file_list = glob.glob(os.path.join("Source", "*.jpg")) #список исходных изображений
current_path = os.getcwd() #текущая папка

copy_and_resize(file_list, current_path)
