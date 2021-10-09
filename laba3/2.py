import pygame
from pygame.draw import *

#colordefinition
BIRDS = (66, 33, 11)
SKY = (254, 213, 162)
SAND = (254, 213, 148)
FRONTHILLS = (48, 16, 38)
MIDHILLS = (172, 67, 52)
BACKHILLS = (252, 152, 49)
SUN = (252, 238, 33)
LINE3 = (254, 213, 196)
PURPLE = (179, 134, 148)

def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

def draw_arc_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.arc(shape_surf, color, (0, 0, *target_rect.size), 0, 3.14, width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

def bird(x, y, scale=1, color=BIRDS): 
    draw_ellipse_angle(screen, color, [x - 12.5*scale, y, 40*scale, 10*scale], -45)
    draw_ellipse_angle(screen, color, [x + 12.5*scale, y - 2*scale, 43*scale, 10*scale], 50)

def painthills(color, coordinates):
    polygon(screen, color, coordinates)

def paintsun(color, coordinates, scale=1):
    circle(screen, color, coordinates, 40*scale)

pygame.init()
FPS = 30
screen = pygame.display.set_mode((800, 450))

#poligons
dmhc0 = [50, 25, 40, 45, 35, 45, 60, 50, 25, 40, 45, 30, 50, 55, 50, 25, 40, 45, 45, 0, -800]
dmhc1 = [30, -45, 25, -40, 30, -40, 10, 25, -45, 30, -40, 30, -45, 10, 30, -45, 25, -40, 45, 250, 0]
dbhc0 = [30, 80, 100, 65, 40, 80, 100, 65, 30, 80, 100, 40, -800, 0]
dbhc1 = [30, -50, 30, -40, 30, -40, 10, 30, -50, 30, -40, 40, 60, -40]
dfhc0  = [100, 150, 50, 200, 50, 50, 50, 150, 0, -800, 0]
dfhc1 = [30, 140, 50, 20, -60, 20, -100, -52, 202, 0, -250]

#starts
midhillCoord = [(0, 250)]
backhillCoord = [(0, 180)]
fronthillCoord = [(0, 200)]
for el in range(21):
    midhillCoord.append((midhillCoord[el][0] + dmhc0[el], midhillCoord[el][1] + dmhc1[el]))
for el in range(14):
    backhillCoord.append((backhillCoord[el][0] + dbhc0[el], backhillCoord[el][1] + dbhc1[el]))
for el in range(11):
    fronthillCoord.append((fronthillCoord[el][0] + dfhc0[el], fronthillCoord[el][1] + dfhc1[el]))

#painting
line(screen, SKY, (0, 50), (800, 50), 100)
line(screen, LINE3, (0, 150), (800, 150), 100)
line(screen, SAND, (0, 250), (800, 250), 100)

painthills(BACKHILLS, backhillCoord)
painthills(MIDHILLS, midhillCoord)
painthills(PURPLE, [(0, 300), (800, 250), (800, 450), (0, 450)])
paintsun(SUN, [400, 100])
painthills(FRONTHILLS, fronthillCoord)

bird(100, 100)
bird(400, 300)
bird(150, 150)
bird(600, 200)
bird(650, 230)
bird(500, 260, 0.75)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
