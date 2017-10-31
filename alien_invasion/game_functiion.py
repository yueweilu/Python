import sys
import pygame
def check_events(ship):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx +=10
            elif event.key == pygame.K_LEFT:
                ship.rect.centerx -= 10

def update_screen(ai_settings,screen,ship):
    '''更新屏幕上的图像，并切换到新屏幕'''
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()