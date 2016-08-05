import pygame
import random
import Buttons
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

answer1_1="You can switch to another"
answer1_2="group with a similar project" 
answer1_3="and other females." 
answer2_1="Try your best, use your skill"
answer2_2="and knowledge to prove that" 
answer2_3="you can be a great manager."
answer3_1="You ask your company to add" 
answer3_2="more females into the group" 
answer3_3="to even out the gender ratio."
answer4_1="You try to get on your co-workers’"
answer4_2="good side by bringing cookies" 
answer4_3="and coffee to work every day."

pygame.init()
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

woman_detail= pygame.image.load('woman-still.png').convert_alpha()

l1=pygame.font.SysFont("comicsansms",20)
l2=pygame.font.SysFont("comicsansms",16)

class Button:
    
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



class woman():
  def __init__(self, screen, x_position, y_position):
    self.screen = screen
    self.x_position = x_position
    self.y_position = y_position
    self.buttonList = []

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

  def show_answer(self):
    coordinates = [[30, 220],[310, 220],[30, 310],[310, 310]]
    for xy in coordinates:
      if self.x_position == 500:
        button = Button()
        self.buttonList.append(button)
        button.create_button(screen, (64, 64, 64), xy[0], xy[1], 260, 80, 0, "no", (64, 64, 64))
        screen.blit(l2.render(answer1_1,True,(230, 230, 230)),(40,220))
        screen.blit(l2.render(answer1_2,True,(230, 230, 230)),(40,245))
        screen.blit(l2.render(answer1_3,True,(230, 230, 230)),(40,270))
        screen.blit(l2.render(answer2_1,True,(230, 230, 230)),(320,220))
        screen.blit(l2.render(answer2_2,True,(230, 230, 230)),(320,245))
        screen.blit(l2.render(answer2_3,True,(230, 230, 230)),(320,270))
        screen.blit(l2.render(answer3_1,True,(230, 230, 230)),(40,310))
        screen.blit(l2.render(answer3_2,True,(230, 230, 230)),(40,335))
        screen.blit(l2.render(answer3_3,True,(230, 230, 230)),(40,360))
        screen.blit(l2.render(answer4_1,True,(230, 230, 230)),(320,310))
        screen.blit(l2.render(answer4_2,True,(230, 230, 230)),(320,335))
        screen.blit(l2.render(answer4_3,True,(230, 230, 230)),(320,360))

   
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
        elif event.type == MOUSEBUTTONDOWN:
            for button in runner.buttonList:
              if button.pressed(pygame.mouse.get_pos()):
                runner.x_position = 0
        if event.type == pygame.QUIT:
            done = True

    screen.blit(BACKGROUND_PICTURE, (0,0))


    runner.create_woman()
    runner.show_question()
    runner.show_answer()
    # runner.show_answer2()
    # runner.show_answer3()
    # runner.show_answer4()
    

    pygame.display.flip()
 
    clock.tick(60)

pygame.quit()



