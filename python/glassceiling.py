import pygame
import random
from pygame.locals import*


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)


pygame.init()
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

woman_detail= pygame.image.load('woman-still.png').convert_alpha()

class woman():
  def __init__(self, screen, x_position, y_position):
    self.screen = screen
    self.x_position = x_position
    self.y_position = y_position
    self.jumpheight = 0

  def creat_woman(self):
    pygame.image.load ("woman-still.png")
    pygame.transform.scale(pygame.image.load('woman-still.png'), (350, 250))
    screen.blit(pygame.image.load('woman-still.png'), (self.x_position, self.y_position))

  def go_to_right(self):
    self.x_position= self.x_position+20

  def go_to_left(self):
    self.x_position=self.x_position-20




  def jump(self):
    if self.jumpheight < SCREEN_HEIGHT - 100: 
      self.jumpheight += 20



    
BACKGROUND_PICTURE = pygame.image.load("office.jpg")
BACKGROUND_PICTURE2 = pygame.image.load("office.jpg")
BACKGROUND_PICTURE_x = 0
BACKGROUND_PICTURE2_x = BACKGROUND_PICTURE.get_width()
 
runner = woman(screen, 80, 350)


pygame.display.set_caption("CityScroller") 
clock = pygame.time.Clock() 
done = False


while not done:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
               runner.go_to_right()
            elif event.key == pygame.K_LEFT:
                runner.go_to_left()
            elif event.key == pygame.K_SPACE:
                runner.jump()
        if event.type == pygame.QUIT:
            done = True

    screen.blit(BACKGROUND_PICTURE, (0,0))

    runner.creat_woman()

    pygame.display.flip()
 
    clock.tick(60)

pygame.quit()



