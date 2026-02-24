import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("my first game screen")

img = pygame.image.load("image.png")
img = pygame.transform.scale(img, (300, 300))

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill((58, 58, 58))
    screen.blit(img, (100, 100))
    pygame.display.update()

pygame.quit()