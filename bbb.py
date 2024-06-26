print("ready!")
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen = pygame.display.set_mode((800, 600))

# Set the title of the window
pygame.display.set_caption("My Game")

# Set the FPS
FPS = 30
clock = pygame.time.Clock()

gameIsRunning = True

ball_x = 100
ball_y = 100

# Game loop
while gameIsRunning:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False

		# Clear the screen
    screen.fill((0, 0, 0))

    ball_x = ball_x + 1
    ball_y = ball_y + 1

    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 20)

    # Flip the display
    pygame.display.flip()

    # Limit the frame rate to 30 FPS
    clock.tick(FPS)


pygame.quit()
sys.exit()