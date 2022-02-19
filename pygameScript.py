import pygame
import os
import time
import numpy as np
import itertools
from pygame.locals import *

pygame.init()

#variables
white = (0, 0, 0)
green = (0, 255, 0)
blue = (255, 255, 255)
X = 900
Y = 900
display_surface = pygame.display.set_mode((X, Y))
font = pygame.font.Font('freesansbold.ttf', 30)
text = font.render('Exercise 1', True, white, blue)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 1.5)
c = white
keynum = 0
i = 0

#images
exercise1 = pygame.image.load(r'/home/harvey/HRI/images/exercise1.png')
exercise2 = pygame.image.load(r'/home/harvey/HRI/images/exercise2.png')
exercise3 = pygame.image.load(r'/home/harvey/HRI/images/exercise3.png')
exercise4 = pygame.image.load(r'/home/harvey/HRI/images/exercise4.png')
exercise5 = pygame.image.load(r'/home/harvey/HRI/images/exercise5.png')

# for i in os.listdir(r'/home/harvey/HRI/images/'):
#     print(i)


ex_dict = {
    exercise1 : 3, 
    exercise2 : 8,
    exercise3 : 40,
    exercise4 : 50,
    exercise5 : 60,
}


def count_routine(rep, initiated_time, count, keynum):
    current_time = pygame.time.get_ticks()
    # print("cxurrent time %d" %current_time)
    # print("start time %d" %initiated_time)
    delta = current_time - initiated_time
    # print("time delta %d" %delta)
    # print("rep number %d" %rep)
    if (delta) >= 1500 :

        initiated_time = starttime_reset()
        
        new_count = count+1
        # print(rep)
        if new_count > rep-1:
            keynum +=1
            count = 0
        else:
            count = new_count
    
    return initiated_time, count, keynum


def starttime_reset():
    # print("start time reset")
    time = pygame.time.get_ticks()
    return time

    
def print_repCount():
    string = 'Current rep number: {}  Total reps:{}'.format(count + 1, rep_count)
    text = font.render(string, True, white, blue)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 1.5)
    display_surface.blit(text, textRect)  

def print_continue():
    string = 'Press [y] to continue and [n] to exit'
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(string, True, white, blue)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 1.2)
    display_surface.blit(text, textRect)
    wait = 1
    return wait





def waiting(wait):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    wait = 0
                    return
                elif event.key == pygame.K_n:
                    quit()

 
  





pygame.display.set_caption('test routine')
start_time = starttime_reset()
count = 0
wait = 0
while True:
    pygame.display.update()

    exercise = list(ex_dict.keys())[keynum]


    
    if wait == 1:
        wait = waiting(wait)
 



    exercise1 = pygame.transform.scale(exercise, (900, 900))
    display_surface.blit(exercise1, (0, 0))
    rep_count = ex_dict[exercise]
  

   
        
    
    # print("count number %d" %count)

    start_time, count, keynum = count_routine(rep_count, start_time, count, keynum)
    print(count)
    print(rep_count)
    print_repCount()  


    if count == rep_count-1:
        wait = print_continue()
    
     
 
    # if pygame.key.get_pressed()[pygame.K_a ]:
    #     c = (0,0,255)
        
    #     # display_surface.fill(c)
       
    #     font = pygame.font.Font('freesansbold.ttf', 40)
    #     text = font.render('Are you finished?', True, white, blue)
    #     textRect = text.get_rect()
    #     textRect.center = (X // 2, Y // 2)
     
        
        # display_surface.blit(text, textRect)
        # pygame.display.flip()
    




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # quit the program.
            quit()
        # Draws the surface object to the screen.
    
