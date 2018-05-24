import os
import wget
import time

file_url = 'ftp://ftp.f-secure.com/support/tools/fsdiag/fsdiag_standalone.exe'
file_name = wget.download(file_url)

# running both threads simultaneously so that program does not stop while waiting for focus
from threading import Thread

def func1():
    print os.system('notepad.exe')

def func2():
    # I put in the sleep time purely to give a pause after opening notepad and before running application
    time.sleep(3)
    print os.system('fsdiag_standalone.exe')

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()



