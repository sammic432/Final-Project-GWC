
import pygame, math, itertools
import random
from pygame.locals import*
import os


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]
 
def random_color():
  return random.choice(colors)

def magnitude(v): 
    return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))

def sub(u, v):
    return [u[i]-v[i] for i in range(len(u))]

def normalize(v): 
    return [v[i]/magnitude(v)  for i in range(len(v))]


pygame.init()

path = itertools.cycle([(26, 43), (105, 110), (45, 225), (145, 295), (266, 211), (178, 134), (250, 56), (147, 12)])
target = next(path)
ball, speed = pygame.rect.Rect(target[0], target[1], 10, 10), 3.6
pause_text = pygame.font.SysFont('Consolas', 32).render('Pause', True, pygame.color.Color('White'))

pause = False
unpause = True

RUNNING, PAUSE = 0, 1
state = RUNNING
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class woman():
    def __init__(self, screen, speed, x_position, y_position):
        self.screen = screen
        self.speed = speed
        self.x_position = x_position
        self.y_position = y_position
        self.jumpheight = 0

    def create_woman(self):
        woman = pygame.image.load ("woman-still.png")
        woman = pygame.transform.scale(woman, (350, 250))
        screen.blit(woman, (self.x_position, self.y_position))

    def move_woman (self, speed):
        self.x_position += self.speed

        if self.jumpheight > 0: self.jumpheight -= 1
        feet_y = SCREEN_HEIGHT - self.jumpheight
        if self.speed == 0:
            # woman1- still
            print ("still woman")

        elif self.runstage < 20:
            # woman2
            print ("woman 2")
            self.runstage += self.speed

        elif self.runstage < 40:
            # woman3
            print ("woman 3")
            self.runstage += self.speed
        elif self.runstage >= 40: self.runstage = 1

    def right(self):
        self.x_position = self.x_position + 15

    def left(self):
        self.x_position = self.x_position - 15

    def jump(self):
        # if self.jumpheight < SCREEN_HEIGHT - 100: self.jumpheight += 10
        self.y_position -= 15

        self.y_position +=15

class button():
    def __init__(self, text, position, size, font, color):
        self.text = text
        self.position = position
        self.size = size
        self.font = font
        self.color = color
    def paused():
      largeText = pygame.font.SysFont("comicsansms",115)
      TextSurf, TextRect = text_objects("Paused", largeText)
      TextRect.center = ((display_width/2),(display_height/2))
      gameDisplay.blit(TextSurf, TextRect)


    
BACKGROUND_PICTURE = pygame.image.load("office.jpg")
BACKGROUND_PICTURE2 = pygame.image.load("office.jpg")
BACKGROUND_PICTURE_x = 0
BACKGROUND_PICTURE2_x = BACKGROUND_PICTURE.get_width()
 
runner = woman(screen, 3, 80, 350)


pygame.display.set_caption("CityScroller") 
clock = pygame.time.Clock() 
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                runner.right()
            elif event.key == pygame.K_LEFT:
                runner.left()
            elif event.key == pygame.K_SPACE:
                runner.jump()
            if event.key == pygame.K_p: 
                state = PAUSE
            if event.key == pygame.K_s: 
                state = RUNNING
        if event.type == pygame.QUIT:
            done = True

        if state == RUNNING:
          target_vector = sub(target, ball.center) 

        if magnitude(target_vector) < 2: 
          target = next(path)
        else:
          ball.move_ip([c * speed for c in normalize(target_vector)])

          pygame.draw.rect(screen, pygame.color.Color('Yellow'), ball)

        if state == PAUSE:
          screen.blit(pause_text, (100, 100))
          os.system("pause")

    screen.blit(BACKGROUND_PICTURE, (0,50))

    runner.create_woman()

    button("Continue", (300, 350), 36, "comicsansms", GREEN)
    button("Quit", (500, 350), 36, "comicsansms", RED)

    pygame.display.flip()
 
    clock.tick(60)

pygame.quit()