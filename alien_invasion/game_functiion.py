import sys
import pygame
def check_events():
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
def update_screen(ai_settings,screen,ship):
    '''更新屏幕上的图像，并切换到新屏幕'''