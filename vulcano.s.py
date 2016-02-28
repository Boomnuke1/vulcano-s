from os.path import dirname, realpath, sep, pardir
import sys,os
curpath=dirname(realpath('__file__'))

print curpath

#importing#
import pygame

#init#
pygame.init()
#gameDisplay#
gameDisplay = pygame.display.set_mode((1000,700))
pygame.display.set_caption("vulcano's")
#colors#
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
#clock#
clock = pygame.time.Clock()
#stop variable#
stop=False
#level#
level = 1
leveldata = 0
#images
gameIcon = pygame.image.load("vulcano.png")
startpage = pygame.image.load('startpage.png')
level1BackGround = pygame.image.load('level1.png')
playbutton1 = pygame.image.load('start.png')
playbutton2 = pygame.image.load('start2.png')
lvl1button = pygame.image.load('lvl1icon.png')
standing = pygame.image.load('standing.png')
down = pygame.image.load('down.png')
right = pygame.image.load('right.png')
right2 = pygame.image.load('right2.png')
left = pygame.image.load('left.png')
left2 = pygame.image.load('left2.png')
jumpright = pygame.image.load('jump.png')
jumpleft = pygame.image.load('jump2.png')
finishdoor = pygame.image.load('finishdoor.png')
#icon#
pygame.display.set_icon(gameIcon)
#levelclass#
class levels:
    def __init__(self,doorX,doorY,startX,startY):
        self.doorX = doorX
        self.doorY = doorY
        self.startX = startX
        self.startY = startY
    def startup(self):
        gameDisplay.blit(finishdoor,(self.doorX,self.doorY))
        gameDisplay.blit(standing,(self.startX,self.startY))
#level objects#
level1 = levels(900,326,45,336)
#game loop#
while not stop:
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop=True
        print(event)
    if level == 0 and leveldata == 0:
        gameDisplay.blit(startpage,(0,0))
        if 350 > mouse[0] > 150 and 590 > mouse[1] > 500:
            gameDisplay.blit(playbutton2,(145,498))
            if click[0] == 1:
                leveldata += 1      
        else:
            gameDisplay.blit(playbutton1,(150,500))
    elif level == 1:
        gameDisplay.blit(level1BackGround,(0,0))
        level1.startup()
    elif level == 0 and leveldata == 1:
        print(event)
    pygame.display.update()
    clock.tick(60)
#quit#
pygame.quit()
quit()
