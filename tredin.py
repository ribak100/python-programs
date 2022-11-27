

# this is threading runing multiple programs at the same time

import threading

class Deadpool_play(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

    


right = Deadpool_play(name="i am going right ")
left = Deadpool_play(name="i am going left ")

right.start()
left.start()


# word frequency counter
'''
import request
from bs4 import beautifulSoup
import operator

'''

import threading 

class Facebook_messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())


x = Facebook_messenger(name=" recieve message ")
y = Facebook_messenger(name=" send out message ")

y.start()
x.start()





