
#pygame hearts
#gets you started to draw a valentine's day card

import pygame #gaming module (aka library) 
pygame.init() #initializes Pygame
pygame.display.set_caption("Valentine's day card") #sets the window title
screen = pygame.display.set_mode((900, 900)) #creates game screen
fontle = pygame.font.get_fonts()
print(fontle)
font = pygame.font.SysFont('comicsansms', 28) #load font
img = pygame.image.load("dog.jpg") #make sure this is saved to the same folder as your code
img2 = pygame.image.load("dog2.jpg")

#first Heart

pygame.draw.circle(screen, (250,0,0), (180, 200), 20) #top left circle
pygame.draw.circle(screen, (250,0,0), (220, 200), 20) #top right circle
pygame.draw.polygon(screen, (250,0,0), ((160, 205),(239, 205), (200, 250))) #triangle to form base

pygame.draw.circle(screen, (250,0,90), (280, 250), 30) 
pygame.draw.circle(screen, (250,0,90), (320, 250), 30) 
pygame.draw.polygon(screen, (250,0,90), ((250, 257),(349, 257), (301, 310)))

pygame.draw.circle(screen, (210,0,190), (380, 150), 35) 
pygame.draw.circle(screen, (210,0,190), (430, 150), 35) 
pygame.draw.polygon(screen, (210,0,190), ((347, 165),(462, 165), (404, 210)))

#text
text1 = font.render('I despise you!', True, (150, 30, 30), (250,0,200)) #numbers give color
text2 = font.render('I await the day you are dismissed from our mortal plane', True, (250, 0, 0), (200,150,150)) #this one includes background color\\
text3 = font.render('Happy Valentines Day', True, (250, 100, 100)) #numbers give color
screen.blit(text1, (200, 100)) #numbers give position
screen.blit(text2, (100, 300))
screen.blit(text3, (500, 000))

#image
img = pygame.transform.scale(img, (600, 400))
screen.blit(img, (0, 400))#draw pic
img2 = pygame.transform.scale(img2, (200, 300))
screen.blit(img2, (600, 420))#draw pic
pygame.display.flip() #this flips all those shapes onto the game screen (needed for every game)
pygame.time.wait(150000) #pause so screen stays up (no game loop)



