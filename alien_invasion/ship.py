import pygame
class Ship():
    def __init__(self,screen):
        '''初始化飞船并设置初始位置'''
        self.screen = screen
        #加载飞船图像并获取器外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #讲每搜飞船放到屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        '''在指定位置回执飞船'''
        self.screen.blit(self.image,self.rect)
        '''测试'''