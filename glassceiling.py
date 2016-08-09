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
level_number=1

#score variable
total = 0


level_two = {
    'question': ["You are applying for a job and you know from past experience that","men get offered more money than women, so you know that the company","can pay you more than what they offer. When you arrive at the","interview, you overhear some men saying they were offered around","$ an hour. You go through your interview and you were offered","$35 an hour. What do you do?"],
    'answers': [
        { 'answer': ["Announce that it was your idea","",""],
            'x': 40,
            'y': 195
        },
        { 'answer': ["After the meeting, you pull him aside", "and offer some more ideas that he", "could suggest in the next meetings."],
            'x': 320,
            'y': 195
        },
        { 'answer': ["You join the crowd and applaud him.","",""],
            'x': 320,
            'y': 285
        },
        { 'answer': ["You throw your coffee at him and", "storm out of the room.",""],
            'x': 40,
            'y': 285
        }
    ]
}

level_three = {
    'question': ["You are an intern, and the person you’re shadowing is in","an important meeting, where they encourage interns to ask","questions. You have an idea that could make the company a","lot of money. You suggest the idea, but a man cuts you off","mid-sentence and finishes what you were saying. Everyone","applauds him and says that it’s a great idea. What do you do?"],
    'answers': [
        { 'answer': ["Take it! $35 an hour is a lot", "more than your old job.",""],
            'x': 40,
            'y': 195
        },
        { 'answer': ["Leave it. You know how much you", "are worth, and it's not $35 an hour.",""] ,
            'x': 320,
            'y': 195
        },
        { 'answer': ["Negotiate for a higher price.","",""],
            'x': 320,
            'y': 285
        },
        { 'answer': ["Pull out the “but those guys", "get $43 an hour!! Why can’t", "I???” card"],
            'x': 40,
            'y': 285
        }
    ]
}

level_one = {
    'question': ["You just became a manager in your company,","and you were assigned a group project, in which ","you were the only woman. This project has to","do with something you’re really passionate about","and would be good at doing, but you feel that they are","not happy with having a female manager. What do you do?"],
    'answers': [
        { 'answer': ["You can switch to another","group with a similar project" ,"and other females."],
            'x': 40,
            'y': 195
        },
        { 'answer': ["Try your best, use your skill", "and knowledge to prove that", "you can be a great manager."],
            'x': 320,
            'y': 195
        },
        { 'answer': ["You ask your company to add", "more females into the group", "to even out the gender ratio"],
            'x': 320,
            'y': 285
        },
        { 'answer': ["You try to get on your co-workers’", "good side by bringing cookies" , "and coffee to work every day."],
            'x': 40,
            'y': 285
        }
    ]
}

# level_one.answers[0].x => 40

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
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False

class Level():
  def __init__(self, situation):
    self.question = situation['question']
    self.wrong_answers = [situation['answers'][0],situation['answers'][2],situation['answers'][3]]
    self.right_answer = situation['answers'][1]
  def questions(self):
    y=20
    for line in self.question:
        screen.blit(l1.render(line,True,(0,0,0)),(20,y))
        y += 30
  def wronganswers(self):
    for obj in self.wrong_answers:
        y = obj['y']
        for line in obj["answer"]:
            y+=25
            screen.blit(l2.render(line, True, (230,230,230)),(obj['x'], y))

  def correctanswer(self):
    y=self.right_answer['y']
    for line in self.right_answer["answer"]:
        y+=25
        screen.blit(l2.render(line, True, (230,230,230)), (self.right_answer['x'],y))

level1=Level(level_one)
level2=Level(level_two)
level3=Level(level_three)

class woman():
  def __init__(self, screen, x_position, y_position):
    self.screen = screen
    self.x_position = x_position
    self.y_position = y_position
    self.imageList = ["running_girl_0001_Layer-3.png", "running_girl_0002_Layer-4.png", "running_girl_0003_Layer-5.png", "running_girl_0004_Layer-6.png", "running_girl_0005_Layer-7.png"]
    self.imageCount = 0

  def create_woman(self, imageFile):
    woman = pygame.image.load(imageFile)
    woman = pygame.transform.scale(woman, (100, 150))
    self.buttonList = []
    screen.blit(woman, (self.x_position, self.y_position))

  def go_to_right(self):
    # self.setImage()
    self.x_position += 20

  def go_to_left(self):
    # self.setImage()
    self.x_position -= 20

  def go_up(self):
    # self.setImage()
    self.y_position -= 10

  def go_down(self):
    # self.setImage()
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
      if level_number == 1:
        level1.questions()
      elif level_number ==2:
        level2.questions()
      elif level_number == 3:
        level3.questions()
  def show_answer(self):
    coordinates = [[30, 220],[310, 220],[30, 310],[310, 310]]
    for xy in coordinates:
        self.button = Button()
        self.buttonList.append(self.button)
        self.button.create_button(screen, (64, 64, 64), xy[0], xy[1], 260, 80, 0, "no", (64, 64, 64))
        if level_number==1:
          level1.wronganswers()
        elif level_number==2:
          level2.wronganswers()
        elif level_number==3:
          level3.wronganswers()

  def correct_answer(self):
      self.Button1 = Button()
      self.Button1.create_button(screen, (64, 64, 64),310, 220, 260, 80, 0, "no", (64, 64, 64))
      if level_number==1:
        level1.correctanswer()
      elif level_number==2:
        level2.correctanswer()
      elif level_number==3:
        level3.correctanswer()

class item(pygame.sprite.Sprite):
    def __init__(self, itemType, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("coin.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.x=random.randint (100, 600)
        self.y=random.randint (100, 400)
        self.itemType = itemType

        # self.l1coins_list = pygame.sprite.Group()

    # def pickUp(self):
    #     return self.itemType

    def move_coin(self):
        self.x=random.randint (100, 600)
        self.y=random.randint (100, 400)

    def show_coin(self):
        item = pygame.image.load("coin.png")
        item = pygame.transform.scale(item, (50, 50))
        # self.buttonList = []
        screen.blit(item, (self.x, self.y))

    def itemsCollision(self, item):
        pygame.sprite.spritecollide(self, item, True)
        # item.show_coin = False
        if woman.itemsCollision:
            item.show_coin = False

    def update(self, movex, movey, item):
        self.moveSprite(movex, movey)
        self.itemsCollision(item)
        # self.render()



coin = item(screen, "coin.png")
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
            if runner.Button1.pressed(pygame.mouse.get_pos()):
              level_number +=1
              runner.x_position = 0
            for button in runner.buttonList:
              if runner.button.pressed(pygame.mouse.get_pos()):
                runner.x_position = 0
        if level_number==1:
            BACKGROUND_PICTURE = pygame.image.load("office.jpg")
            BACKGROUND_PICTURE2 = pygame.image.load("office.jpg")
        elif level_number==2:
            BACKGROUND_PICTURE = pygame.image.load("background.jpg")
            BACKGROUND_PICTURE2 = pygame.image.load("background.jpg")
        elif level_number==3:
            BACKGROUND_PICTURE = pygame.image.load("background2.jpg")
            BACKGROUND_PICTURE2 = pygame.image.load("background2.jpg")
        if event.type == pygame.QUIT:
            done = True
 
    screen.blit(BACKGROUND_PICTURE, (0,0))
    ########### if runner touches sprite, total += 1

    BACKGROUND_PICTURE_x = 0
    BACKGROUND_PICTURE2_x = BACKGROUND_PICTURE.get_width()

    if (coin.x - 75 <= runner.x_position <= coin.x + 25) and (coin.y - 75 <= runner.y_position <= coin.y + 25):
        if level_number==1:
            if total < 5 :
                total += 1
                coin.move_coin()
            else:
                # coin.hide()
                # runner.hide()
                total = 0
                runner.show_question()
                runner.show_answer()

                runner.correct_answer()
        elif level_number==2:
            if total < 10 :
                total += 1
                coin.move_coin()
            else:
                # coin.hide()
                # runner.hide()
                total = 0
                runner.show_question()
                runner.show_answer()

                runner.correct_answer()
        elif level_number==3:
            if total < 15 :
                total += 1
                coin.move_coin()
            else:
                # coin.hide()
                # runner.hide()
                total = 0
                runner.show_question()
                runner.show_answer()

                runner.correct_answer()

    coin.show_coin()
    runner.create_woman("running_girl_0001_Layer-3.png")

    pygame.display.flip()
 
    clock.tick(60)

pygame.quit()

print(level_number)