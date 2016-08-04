import pygame
import random
import pygame, Buttons
from pygame.locals import*


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)

#question variables
question1_1="You just became a manager in your company,"
question1_2="and you were assigned a group project, in which "
question1_3="you were the only woman. This project has to"
question1_4="do with something you’re really passionate about"
question1_5="and would be good at doing, but you feel that they are"
question1_6="not happy with having a female manager. What do you do?"

pygame.init()
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

woman_detail= pygame.image.load('woman-still.png').convert_alpha()

l1=pygame.font.SysFont("comicsansms",20)

class woman():
  def __init__(self, screen, x_position, y_position):
    self.screen = screen
    self.x_position = x_position
    self.y_position = y_position

  def create_woman(self):
    woman = pygame.image.load ("woman-still.png")
    woman = pygame.transform.scale(woman, (175, 300))
    screen.blit(woman, (self.x_position, self.y_position))

  def go_to_right(self):
    self.x_position= self.x_position+20

  def go_to_left(self):
    self.x_position=self.x_position-20

  def go_up(self):
    self.y_position=self.y_position-10
  def go_down(self):
    self.y_position=self.y_position+10
  def show_question(self):
    if self.x_position ==500:
      screen.blit(l1.render(question1_1,True,(0,0,0)),(20,20))
      screen.blit(l1.render(question1_2,True,(0,0,0)),(20,50))
      screen.blit(l1.render(question1_3,True,(0,0,0)),(20,80))
      screen.blit(l1.render(question1_4,True,(0,0,0)),(20,110))
      screen.blit(l1.render(question1_5,True,(0,0,0)),(20,140))
      screen.blit(l1.render(question1_6,True,(0,0,0)),(20,170))


   
BACKGROUND_PICTURE = pygame.image.load("office.jpg")
BACKGROUND_PICTURE2 = pygame.image.load("office.jpg")
BACKGROUND_PICTURE_x = 0
BACKGROUND_PICTURE2_x = BACKGROUND_PICTURE.get_width()
 
# runner = woman(screen, 80, 350)

runner = woman(screen, 0, 200)



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
            elif event.key == pygame.K_UP:
                runner.go_up()
            elif event.key == pygame.K_DOWN:
                runner.go_down()
        if event.type == pygame.QUIT:
            done = True

    screen.blit(BACKGROUND_PICTURE, (0,0))


    runner.create_woman()
    runner.show_question()

    # if __name__ == '__main__':
    #   obj = Button_Example()

    pygame.display.flip()
 
    clock.tick(60)

pygame.quit()



