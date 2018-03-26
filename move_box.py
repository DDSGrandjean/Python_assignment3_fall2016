"""
    move_box.py
    illustrates basic motion
    in the IDEA/ALTER framework
    moves a rect across the screen
"""

# Initialize
import pygame
import random
pygame.init()

# Display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("move a box")

# Entities
# Make a green - gray background.
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))
# Make a red  box.
BOX_SIDE = 25
box = pygame.Surface((BOX_SIDE, BOX_SIDE))
box = box.convert()
box.fill((255, 0, 0))
# Set variables so box will bounce diagonally downwards.
box_x = 0
box_y = 0
dx = 10
dy = 20
# Set variable for box size
sec = 0
dirSec = 0
teleSec = 0
# ACTION
# Assign 
clock = pygame.time.Clock()
keepGoing = True

# Loop
while keepGoing:
    # Time
    clock.tick(30)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
    # modify box value
    box_x += dx
    box_y += dy
    # check boundaries
    if box_y + BOX_SIDE > screen.get_height():
        dy *= -1
    elif box_y < 0:
        dy *= -1
    elif box_x + BOX_SIDE > screen.get_width():
        dx *= -1
    elif box_x < 0:
        dx *= -1
    #modify sec value
    sec += 1
    dirSec += 1
    teleSec += 1
    
    #change box color
    if sec == 150:
        sec = 0
        box.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    #change box direction
    if dirSec == 320:
        dirSec = 0
        dh = dx
        dx = dy
        dy = dh
    #change box position
    if teleSec == 210:
        teleSec = 0
        box_x = random.randint(0, screen.get_width() - BOX_SIDE)
        box_y = random.randint(0, screen.get_height() - BOX_SIDE)
    
        
    #Refresh screen
    screen.blit(background, (0, 0))
    screen.blit(box, (box_x, box_y))
    pygame.display.flip()
pygame.quit()
