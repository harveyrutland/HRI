import pygame
import os
import time
import numpy as np
from pygame.locals import *

def count_routine(rep, initiated_time, count, keynum, skip_wait):
    current_time = pygame.time.get_ticks()
    # print("cxurrent time %d" %current_time)
    # print("start time %d" %initiated_time)
    delta = current_time - initiated_time
    print("time delta %d" %delta)
    # print("rep number %d" %rep)
    print(count)
    
   

    if (delta) >= 1500 and skip_wait == False:

        initiated_time = starttime_reset()
        
        new_count = count+1
        # print(rep)
        if new_count > rep-1:
            keynum +=1
            count = 0
        else:
            count = new_count
    
    elif skip_wait == True:

        
        
        new_count = count + 1
        # print(rep)
        if new_count > rep-1:
            keynum +=1
            count = 0
        else:
            count = new_count

        skip_wait = False
        initiated_time = starttime_reset()
    
    return initiated_time, count, keynum, skip_wait


def starttime_reset():
    # print("start time reset")
    time = pygame.time.get_ticks()
    return time

    
def print_repCount():
    string = 'Current rep number: {}  Total reps:{}'.format(count, rep_count-1)
    text = font.render(string, True, white, blue)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 1.5)
    display_surface.blit(text, textRect)  

def print_continue():
    string = 'Press [y] to continue and [n] to exit'
    text = font2.render(string, False, black)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 1.2)
    display_surface.blit(text, textRect)
    wait = True
    return wait


def waiting(w):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    w = False
                    return w
                    
                elif event.key == pygame.K_n:
                    quit()

def New_routineCountdown():
    countdownls = [5,4,3,2,1]
    for i in countdownls:

       
        background_colour = (255,255,255)
        display_surface.fill(background_colour)
        string = str(i)
        text = font2.render(string, False, black)
        textRect = text.get_rect()
        textRect.center = (X // 2, Y // 1.2)
        display_surface.blit(text, textRect)
        pygame.display.update()
        pygame.time.wait(1000)
    new_routine = False
    return new_routine 



        
       


pygame.init()

#variables
white = (0, 0, 0)
black = (0, 0, 0)
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
start_time = starttime_reset()
count = 0
wait = False
skip_wait = False
font2 = pygame.font.Font('freesansbold.ttf', 30)


#images
exercise1 = pygame.image.load(r'/home/harvey/HRI/images/exercise1.png')
exercise2 = pygame.image.load(r'/home/harvey/HRI/images/exercise2.png')
exercise3 = pygame.image.load(r'/home/harvey/HRI/images/exercise3.png')
exercise4 = pygame.image.load(r'/home/harvey/HRI/images/exercise4.png')
exercise5 = pygame.image.load(r'/home/harvey/HRI/images/exercise5.png')

# for i in os.listdir(r'/home/harvey/HRI/images/'):
#     print(i)


ex_dict = {
    exercise1 : 5, 
    exercise2 : 7,
    exercise3 : 3,
    exercise4 : 10,
    exercise5 : 60,
}




currentkeynum = keynum 
pygame.display.set_caption('test routine')
new_routine = True
while True:

    if new_routine == True:
        new_routine = New_routineCountdown()

    pygame.display.update()

    if wait == True:
            wait = waiting(wait)
            new_routine = New_routineCountdown()
            skip_wait = True
    else:
        exercise = list(ex_dict.keys())[keynum]
        exercise1 = pygame.transform.scale(exercise, (900, 900))
        

        
    
    
    rep_count = ex_dict[exercise]

    start_time, count, keynum, skip_wait = count_routine(rep_count, start_time, count, keynum, skip_wait)
    # print(count)
    display_surface.blit(exercise1, (0, 0))
    # print(rep_count)
    print_repCount() 
 

    if count == rep_count-1:
        wait = print_continue()
    

    

    
