import subprocess
import glob
import os.path
import shutil

def copy_and_resize (file_list, directory):
    #создание папки для полученных изображений
    if not os.path.isdir('./Result'):
        os.mkdir('./Result')
    #цикл, копирующий изображения и изменяющий размер
    for f in file_list:
        shutil.copy(os.path.join(directory, f), os.path.join(directory, "Result", f.split('/')[1]))
        subprocess.run(["sips", "--resampleWidth", "200", os.path.join(directory, "Result", f.split('/')[1])])

file_list = glob.glob(os.path.join("Source", "*.jpg")) #список исходных изображений
current_path = os.getcwd() #текущая папка

copy_and_resize(file_list, current_path)
