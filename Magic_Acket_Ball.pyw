#!python3
import os
import sys
import codecs
import random
import pdb
import clipboard
from tkinter import messagebox

acketz = []
default_file = os.path.join(os.getcwd(), 'acketz.txt')

def new_answer(answer=None):
    answer = answer or input('-> ')
    if answer not in acketz:
        acketz.append(answer)
        return True
    else:
        print('This option is already in the list.')
        return False
    
def save_answers(file=None):
    file = file or default_file
    with codecs.open(file, 'w', 'utf-8') as f:
        for choice in acketz:
            f.write(str(choice) + '\r\n')
            
def get_choices_from_file(file=None):
    file = file or default_file
    with codecs.open(file, 'r', 'utf-8') as f:
        for line in f:
            new_answer(line.strip('\r\n'))
            
def get_random_acket():
    acket = acketz[random.randint(0, len(acketz) - 1)]
    clipboard.copy(acket)
    
def go():
    get_random_acket()
    exit()
    
def exit(file=None):
    file = file or default_file
    save_answers(file)
    os._exit(0)
    
get_choices_from_file()

if len(sys.argv) < 2:
    go()
else:
    sys.argv.remove(sys.argv[0])
    new_acket = ' '.join(sys.argv)
    if not new_answer(new_acket):
        messagebox.showinfo(title='Ooops', message='This option is already in the list.')
        
exit()