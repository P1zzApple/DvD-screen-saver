import pygame

pygame.init()
w = 900
h = 760
run = True
win = pygame.display.set_mode((w, h))
pygame.display.set_caption("DVD tyda cyda")
clock = pygame.time.Clock()
dvd = pygame.image.load("dvd.png").convert_alpha()
speed = [3, 4]
fps = 60
rect = dvd.get_rect()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        pygame.display.flip()

        win.blit(dvd, rect)
        rect.top += speed[1]
        rect.left += speed[0]
        if rect.left < 0:
            speed[0] = -speed[0]
        if rect.right > w:
            speed[0] = -speed[0]
        if rect.top < 0:
            speed[1] = -speed[1]
        if rect.bottom > h:
            speed[1] = -speed[1]

        clock.tick(fps)


pygame.quit()
quit()
