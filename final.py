import pygame
import random


pygame.init()
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Glass Ceiling")

background = pygame.image.load ("C:\Desktop\Adobe-SIP-2016\week6/background.jpg")
screen = pygame.display.set_mode(background_size)
done = False

# clock = pygame.time.clock()

# -------- Main Program Loop -----------
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# screen.fill(WHITE)
	# gameDisplay.blit(bg, (0, 0))





	pygame.display.flip()

	# clock.tick(60)


pygame.quit()
exit()

