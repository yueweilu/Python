'''存储（外星人入侵）的所有游戏设置的类'''
class Settings():
    def __init__(self):
        '''初始化游戏的设置'''
        #屏幕的设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 10
        #子弹的设置
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
