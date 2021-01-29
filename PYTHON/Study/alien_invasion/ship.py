import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('D:/My OpenResource/Python/PYTHON/Study/alien_invasion/images/ship.bmp')
        self.rect  = self.image.get_rect()

        #对于每艘新飞船，都将其放在屏幕底端的中央
        self.rect.midbottom = self.screen_rect.midbottom

        #在飞船的属性x中存储小数值
        self.x = float(self.rect.x)#rect对象的x属性只能存储整数值

        #移动标志位
        self.moving_right_flag = False
        self.moving_left_flag  = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """根据移动标志位调整飞船的位置"""
        if self.moving_right_flag and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left_flag and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #根据self.x更新rect对象
        self.rect.x = self.x

    def center_ship(self):
        """让飞船在屏幕底端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)