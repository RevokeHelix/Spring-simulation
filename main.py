import math
import time

import pygame


def getvelocity(energy, mass):
    return math.sqrt((2 * energy) / mass)


def getenergy(springconst, stretch):
    return 1 / 2 * springconst * stretch * stretch


def gety(mass, springconst, stretch, angle, time):
    energy = getenergy(springconst, stretch)
    initialvelocity = getvelocity(energy, mass)
    return (initialvelocity * math.sin(angle)) * time - 1 / 2 * 9.81 * time * time


def getx(mass, springconst, stretch, angle, time):
    energy = getenergy(springconst, stretch)
    initialvelocity = getvelocity(energy, mass)
    return (initialvelocity * math.cos(angle)) * time


from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_w,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 600
TIME = 0


# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.x = 0
        self.rect.y = 500
    def update(self):
        global XValueText,Xvalue,YValueText,Yvalue
        move(player, TIME)
        XValueText = str(player.rect.x)
        Xvalue = font.render(XValueText, False, green, white)
        YValueText = str(550-player.rect.y)
        Yvalue = font.render(YValueText, False, green, white)

# Initialize pygame sd
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
player = Player()
font = pygame.font.Font('freesansbold.ttf', 32)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
XValueText = "df"
Xvalue = font.render(XValueText, False, green, white)
YValueText = "df"
Yvalue = font.render(YValueText, False, green, white)
# create a rectangular object for the
# text surface object
XLabelRect = Xvalue.get_rect()
YLabelRect = Yvalue.get_rect()
# set the center of the rectangular object.
XLabelRect.center = (1160, 70)
YLabelRect.center = (1160,150)
# Variable to keep the main loop running
running = True


def move(self, t):
    global TIME
    time.sleep(0.01)
    pygame.display.flip()
    springconst = 30.7
    mass = 0.5
    stretch = 10
    angle = math.pi / 2

    if not (self.rect.y >= 550):
        self.rect.x += round(getx(mass, springconst, stretch, angle, t + 0.1) - getx(mass, springconst, stretch, angle, t))
        print(self.rect.x, "x")
        self.rect.y -= round((gety(mass, springconst, stretch, angle, t + 0.1) - gety(mass, springconst, stretch, angle, t)))
        print(self.rect.y, "y")
        TIME += 0.1
    else:
        self.rect.y = 550
        return

# Main loop
while running:
    # Look at every event in the queue
    player.update()
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    # Fill the screen with black
    screen.fill((255, 255, 255))

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)
    screen.blit(Xvalue, XLabelRect)
    screen.blit(Yvalue, YLabelRect)
    # Update the display
    pygame.display.flip()
