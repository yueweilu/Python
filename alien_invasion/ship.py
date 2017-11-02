import pygame
class Ship():
    def __init__(self,ai_setting,screen):


        '''初始化飞船并设置初始位置'''
        self.screen = screen
        self.ai_setting = ai_setting


        #加载飞船图像并获取器外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #讲每搜飞船放到屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False
    def update(self):
        '''根据移动的标志调整飞船的位置'''
        # 更新飞船的center值而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor

        #根据self.center 更新rect对象
        self.rect.centerx = self.center
    def blitme(self):
        '''在指定位置回执飞船'''
        self.screen.blit(self.image,self.rect)
        '''测试哈哈哈哈'''
