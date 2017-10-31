import pygame

from settings import Settings
from ship import Ship
import game_functiion as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #设置背景颜色
    bg_color = (230,230,230)
    #创建一艘飞船
    ship = Ship(screen)

    #开售游戏的住循环
    while True:
        #监听键盘和鼠标事件
        gf.check_events(ship)

        gf.update_screen(ai_settings,screen,ship)
run_game()
