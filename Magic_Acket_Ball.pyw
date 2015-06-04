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

class CaseIgnore(object):
    def __init__(self, s):
        self.__s = s.lower()
    def __hash__(self):
        return hash(self.__s)
    def __eq__(self, other):
        # ensure proper comparison between instances of this class
        try:
           other = other.__s
        except (TypeError, AttributeError):
          try:
             other = other.lower()
          except:
             pass
        return self.__s == other

def new_answer(answer=None):
    answer = answer or input('-> ')
    if CaseIgnore(answer) not in acketz:
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
    acket = 'Magic Acket Ball Sez: ' + str(acketz[random.randint(0, len(acketz) - 1)])
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