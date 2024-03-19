import pygame
pygame.init()

w, h = 320, 350
speed = [2, 2]
BLACK = (0, 0, 0)
pygame.display.set_mode((w, h), pygame.RESIZABLE)
pygame.display.set_caption("First Window")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()



    # чтоб двигался горизатально
    # if flLeft and flUp:
    #     x -= speed
    #     y -= speed
    # elif flLeft and flDown:
    #     x -= speed
    #     y += speed
    # elif flRight and flUp:
    #     x += speed
    #     y -= speed
    # elif flRight and flDown:
    #     x += speed
    #     y += speed
