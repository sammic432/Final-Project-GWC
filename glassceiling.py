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
    woman = pygame.image.load ("woman-still.png")
    woman = pygame.transform.scale(woman, (80, 35))
    screen.blit(woman, (300, 450))

  def move_woman (self, speed):
    self.x_position += self.speed

class Building():
  def __init__(self, x_point, y_point, width, height, color):
    self.x_point= x_point
    self.y_point= y_point
    self.width= width
    self.height= height
    self.color= color

  def draw(self):
    pygame.draw.rect(screen, self.color, (self.x_point, SCREEN_HEIGHT - self.height, self.width, self.height))

  def move(self, speed):
    self.x_point -= speed

class Scroller(object):
  
  def __init__(self, width, height, base, color, speed):
    self.width= width
    self.height= height
    self.base= base
    self.color= color
    self.speed= speed
    self.building_list= []
    self.add_buildings()
    
  def add_buildings(self):
    self.add_building(-120,120)
    random_width = 0
    x_location=0
    while x_location<= self.width:
      random_width = random.randint(40, 180)
      self.add_building(x_location, random_width)
      x_location = x_location + random_width  + 20
 
  def add_building(self, x_location, combined_width):
    building1 = Building(x_location, self.base, combined_width, random.randint(80, 200), random_color())
    self.building_list.append(building1)

  def draw_buildings(self):
    pygame.draw.rect(screen, self.color, (0, SCREEN_HEIGHT, self.width, SCREEN_HEIGHT - self.height))
    for building1 in self.building_list:
      building1.draw()

  def move_buildings(self, runningspeed):
    for building1 in self.building_list:
      building1.move(self.speed + runningspeed)
      last_building = self.building_list[-1]
      if last_building.x_point > self.width:
        self.building_list.remove(last_building) 
      first_building = self.building_list[0]
      if first_building.x_point > 20:
        building_width = random.randint(40,180)
        b = Building(-building_width, 0, building_width, random.randint(80, 400), random_color())
        self.building_list.insert(0,b)

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

    
FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (135,206,235)
 
front_scroller = Scroller(SCREEN_WIDTH, 500, 0, FRONT_SCROLLER_COLOR, 6)
middle_scroller = Scroller(SCREEN_WIDTH, 300, 100, MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 400, 200, BACK_SCROLLER_COLOR, 1)
runner = RunningPerson(int(SCREEN_WIDTH/2), WHITE, 0)

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
 
   screen.fill(BACKGROUND_COLOR)
 
   back_scroller.draw_buildings()
   middle_scroller.draw_buildings()
   front_scroller.draw_buildings()
   runner.draw()


   woman.create_woman(10)

   if runner.speed > 0:
     back_scroller.move_buildings(runner.speed)
     middle_scroller.move_buildings(runner.speed)
     front_scroller.move_buildings(runner.speed)

   pygame.display.flip()
 
   clock.tick(60)

pygame.quit()