import pygame
import os
from pygame import mixer
import random

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init()
mixer.init()


pygame.display.set_caption('not a virus')
clock = pygame.time.Clock()

mixer.music.load(resource_path("wee.mp3"))
mixer.music.play(loops=-1)

#openness
#conscientnous
#extroversion
#agreeable
#neuroticism
colors = [(255,0,0), (0,255,0), (0,0,255), (255, 255,0), (0, 255, 255), (255, 0, 255)]


screen=pygame.display.set_mode([660, 480])


running=True

size = 30 #should go into 660 and 480 evenly... probly

squares = [[colors[0]] * int(660/size) for x in range(int(480/size))]
print(squares)

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    for i in range(10):
        randy = random.randint(0,480/size-1)
        randx = random.randint(0,660/size-1)
        randC = random.choice(colors)

        squares[randy][randx] = randC



    print(squares[0][0])

    screen.fill((255, 0, 255))
    
    for y in range(len(squares)):
        for x in range(len(squares[0])):
            pygame.draw.rect(screen, squares[y][x], pygame.Rect(x*size, y*size, size, size))
        
    pygame.display.flip()
    clock.tick(40)


pygame.quit()