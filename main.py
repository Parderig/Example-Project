import sys, pygame, time
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

size = (width,height) = (screen_info.current_w,screen_info.current_h)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (194,20,255)

orange_fish = pygame.image.load('images/Good_Fish.png')
orange_fish = pygame.transform.smoothscale(orange_fish, (60,60))
fish_rect = orange_fish.get_rect()
fish_rect.center = (width // 2,height // 2)

speed_x = 0
speed_y = 0
moving = False

def move(x,y):
  global speed_x, speed_y, moving
  speed_x += x
  speed_y += y
  fish_rect.move_ip(speed_x,speed_y)

def reset():
  global speed_x, speed_y
  speed_x = 0
  speed_y = 0

def main():
  global moving
  while True:
    clock.tick(60)
    screen.fill(color)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      #try this with a while so we can skip keyup events
      if event.type == KEYDOWN:
        if event.key == K_UP:
          move(0,-5)
          reset()
        if event.key == K_DOWN:
          move(0,5)
          reset()
        if event.key == K_RIGHT:
          move(5,0)
          reset()
        if event.key == K_LEFT:
          move(-5,0)
          reset()
    #get some keydown events for pygame and run the move function
    screen.blit(orange_fish,fish_rect)
    pygame.display.flip()

if __name__ == '__main__':
  main()