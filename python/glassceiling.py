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

#level variable
levelnumber=1

#question variables
question1_1="You just became a manager in your company,"
question1_2="and you were assigned a group project, in which "
question1_3="you were the only woman. This project has to"
question1_4="do with something you’re really passionate about"
question1_5="and would be good at doing, but you feel that they are"
question1_6="not happy with having a female manager. What do you do?"

<<<<<<< HEAD
question2_1="You are an intern, and the person you’re shadowing is in" 
question2_2="an important meeting, where they encourage interns to ask" 
question2_3="questions. You have an idea that could make the company a" 
question2_4="lot of money. You suggest the idea, but a man cuts you off" 
question2_5="mid-sentence and finishes what you were saying. Everyone" 
question2_6="applauds him and says that it’s a great idea. What do you do?"

question3_1="You are applying for a job and you know from past experience that"
question3_2="men get offered more money than women, so you know that the company"
question3_3="can pay you more than what they offer. When you arrive at the"
question3_4="interview, you overhear some men saying they were offered around"
question3_5="$ an hour. You go through your interview and you were offered"
question3_6="$35 an hour. What do you do?"
#answer variables
answer1_1_1="You can switch to another"
answer1_1_2="group with a similar project" 
answer1_1_3="and other females." 
answer1_2_1="Try your best, use your skill"
answer1_2_2="and knowledge to prove that" 
answer1_2_3="you can be a great manager."
answer1_3_1="You ask your company to add" 
answer1_3_2="more females into the group" 
answer1_3_3="to even out the gender ratio."
answer1_4_1="You try to get on your co-workers’"
answer1_4_2="good side by bringing cookies" 
answer1_4_3="and coffee to work every day."

answer2_1_1="Announce that it was your idea"
answer2_1_2=""
answer2_1_3=""
answer2_2_1="After the meeting, you pull him aside"
answer2_2_2="and offer some more ideas that he"
answer2_2_3="could suggest in the next meetings."
answer2_3_1="You join the crowd and applaud him."
answer2_3_2=""
answer2_3_3=""
answer2_4_1="You throw your coffee at him and"
answer2_4_2="storm out of the room."
answer2_4_3=""

answer3_1_1="Take it! $35 an hour is a lot"
answer3_1_2="more than your old job."
answer3_1_3=""
answer3_2_1="Leave it. You know how much you"
answer3_2_2="are worth, and it's not $35 an hour."
answer3_2_3=""
answer3_3_1="Negotiate for a higher price."
answer3_3_2=""
answer3_3_3=""
answer3_4_1="Pull out the “but those guys"
answer3_4_2="get $43 an hour!! Why can’t"
answer3_4_3="I???” card"
=======
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

answer2_1="Try your best, use your skill"
answer2_2="and knowledge to prove that" 
answer2_3="you can be a great manager."
answer3_1="You ask your company to add" 
answer3_2="more females into the group" 
answer3_3="to even out the gender ratio."
answer4_1="You try to get on your co-workers’"
answer4_2="good side by bringing cookies" 
answer4_3="and coffee to work every day."
>>>>>>> origin/master

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


class level():
  def __init__(self, question_part1, question_part2, question_part3, question_part4, question_part5, question_part6, one_part1, one_part2, one_part3, two_part1,two_part2,two_part3,three_part1,three_part2,three_part3, thepart1, thepart2, thepart3):
    self.question_part1=question_part1
    self.question_part2=question_part2
    self.question_part3=question_part3
    self.question_part4=question_part4
    self.question_part5=question_part5
    self.question_part6=question_part6
    self.one_part1=one_part1
    self.one_part2=one_part2
    self.one_part3=one_part3
    self.two_part1=two_part1
    self.two_part2=two_part2
    self.two_part3=two_part3
    self.three_part1=three_part1
    self.three_part2=three_part2
    self.three_part3=three_part3
    self.thepart1=thepart1
    self.thepart2=thepart2
    self.thepart3=thepart3
  def questions(self):
    screen.blit(l1.render(self.question_part1,True,(0,0,0)),(20,20))
    screen.blit(l1.render(self.question_part2,True,(0,0,0)),(20,50))
    screen.blit(l1.render(self.question_part3,True,(0,0,0)),(20,80))
    screen.blit(l1.render(self.question_part4,True,(0,0,0)),(20,110))
    screen.blit(l1.render(self.question_part5,True,(0,0,0)),(20,140))
    screen.blit(l1.render(self.question_part6,True,(0,0,0)),(20,170))
  def wronganswers(self):
    screen.blit(l2.render(self.one_part1,True,(230, 230, 230)),(40,220))
    screen.blit(l2.render(self.one_part2,True,(230, 230, 230)),(40,245))
    screen.blit(l2.render(self.one_part3,True,(230, 230, 230)),(40,270))
    screen.blit(l2.render(self.two_part1,True,(230, 230, 230)),(40,310))
    screen.blit(l2.render(self.two_part2,True,(230, 230, 230)),(40,335))
    screen.blit(l2.render(self.two_part3,True,(230, 230, 230)),(40,360))
    screen.blit(l2.render(self.three_part1,True,(230, 230, 230)),(320,310))
    screen.blit(l2.render(self.three_part2,True,(230, 230, 230)),(320,335))
    screen.blit(l2.render(self.three_part3,True,(230, 230, 230)),(320,360))
  def correctanswer(self):
    screen.blit(l2.render(self.thepart1,True,(230, 230, 230)),(320,220))
    screen.blit(l2.render(self.thepart2,True,(230, 230, 230)),(320,245))
    screen.blit(l2.render(self.thepart3,True,(230, 230, 230)),(320,270))
    
level1=level(question1_1, question1_2, question1_3,question1_4,question1_5,question1_6,answer1_1_1,answer1_1_2,answer1_1_3,answer1_2_1,answer1_2_2,answer1_2_3,answer1_3_1,answer1_3_2,answer1_3_3,answer1_2_1,answer1_2_2,answer1_2_3)
level2=level(question2_1, question2_2, question2_3,question2_4,question2_5,question2_6,answer2_1_1,answer2_1_2,answer2_1_3,answer2_2_1,answer2_2_2,answer2_2_3,answer2_3_1,answer2_3_2,answer2_3_3,answer2_2_1,answer2_2_2,answer2_2_3)
level3=level(question1_1, question3_2, question3_3,question3_4,question3_5,question3_6,answer3_1_1,answer2_1_2,answer2_1_3,answer3_2_1,answer3_2_2,answer3_2_3,answer3_3_1,answer3_3_2,answer3_3_3,answer3_2_1,answer3_2_2,answer3_2_3)

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
    self.buttonList = []
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
    self.x_position=self.x_position-20

  def go_up(self):
    self.y_position=self.y_position-10
  def go_down(self):
    self.y_position=self.y_position+10

  def show_question(self):
    if self.x_position ==500:
      if levelnumber == 1:
        level1.questions()
      elif levelnumber ==2:
        level2.questions()
      elif levelnumber == 3:
        level3.questions()
  def show_answer(self):
<<<<<<< HEAD
    coordinates = [[30, 220],[30, 310],[310, 310]]
=======
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

  def show_answer(self):
    coordinates = [[30, 220],[310, 220],[30, 310],[310, 310]]
>>>>>>> origin/master
    for xy in coordinates:
      if self.x_position == 500:
        button = Button()
        self.buttonList.append(button)
        button.create_button(screen, (64, 64, 64), xy[0], xy[1], 260, 80, 0, "no", (64, 64, 64))
        if levelnumber==1:
          level1.wronganswers()
        elif levelnumber==2:
          level2.wronganswers()
        elif levelnumber==3:
          level3.wronganswers()
  def correct_answer(self):
    if self.x_position == 500:
      Button1 = Button()
      Button1.create_button(screen, (64, 64, 64),310, 220, 260, 80, 0, "no", (64, 64, 64))
      if levelnumber==1:
        level1.correctanswer()
      elif levelnumber==2:
        level2.correctanswer()
      elif levelnumber==3:
        level3.correctanswer()

if levelnumber==1:
   BACKGROUND_PICTURE = pygame.image.load("office.jpg")
elif levelnumber==2:
  BACKGROUND_PICTURE = pygame.image.load("background.jpg")
elif levelnumber==3:
  BACKGROUND_PICTURE = pygame.image.load("background2.jpg")

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
        elif event.type == MOUSEBUTTONDOWN:
            for button in runner.buttonList:
              if button.pressed(pygame.mouse.get_pos()):
                runner.x_position = 0
        elif event.type == MOUSEBUTTONDOWN:
            if Button1.pressed(pygame.mouse.get_pos()):
              levelnumber = levelnumber+1
              print(levelnumber)
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
<<<<<<< HEAD
    runner.correct_answer()
    
=======
    # runner.show_answer2()
    # runner.show_answer3()
    # runner.show_answer4()
>>>>>>> origin/master

    pygame.display.flip()
 
    clock.tick(60)

pygame.quit()
