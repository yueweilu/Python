'''存储（外星人入侵）的所有游戏设置的类'''
class Settings():
    def __init__(self):
        '''初始化游戏的设置'''
        #屏幕的设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #飞船的设置
        self.ship_speed_factor = 10

        #子弹的设置
        self.bullet_speed_factor = 7.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60,60
        self.bullets_allowed = 10

        #外星人的设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

        #飞船的设置

        self.ship_speed_factor = 1.5
        self.ship_limit = 3