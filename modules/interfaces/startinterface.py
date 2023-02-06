import sys
import pygame
from config import *

'''Интерфейс запуска игры'''
def startInterface(screen, start_button_path):
    begin_image = transform.scale(image.load(os.path.join(MEDIA_DIR,'images/startimage.jpg')), (win_rez_x, win_rez_y))
    start_images = [transform.scale(pygame.image.load(start_button_path[0]), (100, 100)),transform.scale(pygame.image.load(start_button_path[1]),(100, 100))]

    start_button = start_images[0]
    while True:
        for event in pygame.event.get():
            #условия выхода из игры
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[False] in list(range(150, 250)) and mouse_pos[True] in list(range(300, 400)):
                    start_button = start_images[1]
                else:
                    start_button = start_images[0]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if event.button == True and mouse_pos[False] in list(range(150, 250)) and mouse_pos[True] in list(range(300, 400)):
                    return True
        screen.blit(begin_image, (0, 0))
        screen.blit(start_button, (150, 300))
        pygame.display.update()