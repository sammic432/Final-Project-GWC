import pygame
import random
import Buttons
from pygame.locals import*
import itertools


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

answer1_1="You can switch to another"
answer1_2="group with a similar project" 
answer1_3="and other females." 
answer1_4=" " 
answer1_5=""



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
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# woman_detail= pygame.image.load('running_girl_0001_Layer-3.png').convert_alpha()

l1=pygame.font.SysFont("comicsansms",20)
l2=pygame.font.SysFont("comicsansms",16)

class Button:
    def __init__(self, nothing):
      self.nothing=nothing
    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x,y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y):
        font_size = int(length//len(text))
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):           
        for i in range(1,10):
            s = pygame.Surface((length+(i*2),height+(i*2)))
            s.fill(color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x-i,y-i,length+i,height+i), width)
            surface.blit(s, (x-i,y-i))
        pygame.draw.rect(surface, color, (x,y,length,height), 0)
        pygame.draw.rect(surface, (190,190,190), (x,y,length,height), 1)  
        return surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print ("Some button was pressed!")
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False

Button1=Button(832)

class woman():
  def __init__(self, screen, x_position, y_position):
    self.screen = screen
    self.x_position = x_position
    self.y_position = y_position
    self.imageList = ["running_girl_0001_Layer-3.png", "running_girl_0002_Layer-4.png", "running_girl_0003_Layer-5.png", "running_girl_0004_Layer-6.png", "running_girl_0005_Layer-7.png"]
    self.imageCount = 0

  def create_woman(self, imageFile):
    print(imageFile)
    woman = pygame.image.load(imageFile)
    woman = pygame.transform.scale(woman, (100, 150))
    screen.blit(woman, (self.x_position, self.y_position))

  def go_to_right(self):
    self.setImage()
    self.x_position += 20

  def go_to_left(self):
    self.setImage()
    self.x_position -= 20

  def go_up(self):
    self.setImage()
    self.y_position -= 10

  def go_down(self):
    self.setImage()
    self.y_position += 10

  def setImage(self):
    last = self.imageList.pop
    print(last)
    print(self.imageList)
    self.imageList.insert(0, last)
    # self.create_woman(self.imageList[0])


  def show_question(self):
    if self.x_position ==500:
      screen.blit(l1.render(question1_1,True,(0,0,0)),(20,20))
      screen.blit(l1.render(question1_2,True,(0,0,0)),(20,50))
      screen.blit(l1.render(question1_3,True,(0,0,0)),(20,80))
      screen.blit(l1.render(question1_4,True,(0,0,0)),(20,110))
      screen.blit(l1.render(question1_5,True,(0,0,0)),(20,140))
      screen.blit(l1.render(question1_6,True,(0,0,0)),(20,170))
  def show_answer(self):
    if self.x_position ==500:
      Button1.create_button(screen, (102, 204, 255), 30, 220, 250, 70, 0, "noone", (102,204,255))
      screen.blit(l2.render(answer1_1,True,(255,255,255)),(40,220))
      screen.blit(l2.render(answer1_2,True,(255,255,255)),(40,245))
      screen.blit(l2.render(answer1_3,True,(255,255,255)),(40,270))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            if Button1.pressed(pygame.mouse.get_pos()):
                self.x_position = 0



   
BACKGROUND_PICTURE = pygame.image.load("office.jpg")
BACKGROUND_PICTURE2 = pygame.image.load("office.jpg")
BACKGROUND_PICTURE_x = 0
BACKGROUND_PICTURE2_x = BACKGROUND_PICTURE.get_width()


# runner = woman(screen, 80, 350)

runner = woman(screen, 0, 200)



pygame.display.set_caption("Glass Ceiling") 
clock = pygame.time.Clock() 
done = False

pygame.key.set_repeat(10,10)

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

    # keys_pressed = key.get_pressed()

    # if keys_pressed[K_LEFT]:
    #     woman.go_to_left()

    # if keys_pressed[K_RIGHT]:
    #     woman.go_to_right()

    # if keys_pressed[K_UP]:
    #     woman.go_up()

    # if keys_pressed[K_DOWN]:
    #     woman.go_down()

    screen.blit(BACKGROUND_PICTURE, (0,0))


    runner.create_woman("running_girl_0001_Layer-3.png")
    runner.show_question()
    runner.show_answer()
    

    pygame.display.flip()
 
    clock.tick(60)

pygame.quit()



