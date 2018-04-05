#!/usr/bin/envs python3
#-*- encoding: utf-8 -*-

# Python Multithreading introduction
# https://www.youtube.com/watch?v=PJ4t2U15ACo&list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN

import time
import threading

def calc_square(numbers):
    print("Calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n * n)

def calc_cube(numbers):
    print("Calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:', n * n * n)

arr = [ 2, 3, 8, 9]

t = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()
print("done in {:.2f} seconds ".format(time.time() - t))
print("Han... I am done with all my work now!")
