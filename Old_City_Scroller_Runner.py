import pygame, sys
import random
from pygame.locals import*


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

pygame.init()
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class woman():
  def __init__(self, screen, speed, x_position, y_position):
    self.screen = screen
    self.speed = speed
    self.x_position = x_position
    self.y_position = y_position

  def create_woman(self):
    woman = pygame.image.load ("woman2.png")
    woman = pygame.transform.scale(woman, (350, 250))
    screen.blit(woman, (self.x_position, self.y_position))

  def move_woman (self, speed):
    self.x_position += self.speed


class RunningPerson():
    def __init__(self, x_point, color, speed):
        self.x_point= x_point
        self.color= color
        self.runstage = 1
        self.speed = speed
        self.jumpheight = 0

    def draw(self):
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
        if self.runstage >= 40: self.runstage = 1

    def faster(self):
        if self.speed < 10:
            self.speed +=1

    def slower(self):
        if self.speed > 0:
            self.speed -= 1

    def jump(self):
        if self.jumpheight < SCREEN_HEIGHT - 100: self.jumpheight += 20

    
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
               runner.faster()
            elif event.key == pygame.K_LEFT:
                runner.slower()
            elif event.key == pygame.K_SPACE:
                runner.jump()
        if event.type == pygame.QUIT:
            done = True
 
    screen.blit(BACKGROUND_PICTURE, (0,0))


    runner.create_woman()


    pygame.display.flip()
 
    clock.tick(60)

pygame.quit()
