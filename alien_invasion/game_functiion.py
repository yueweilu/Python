import sys
import pygame

from bullet import Bullet
from alien import Alien
from time import sleep
def check_events(ai_settings,screen,ship,bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)



def check_keydown_events(event, aisettings,screen,ship,bullets):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key ==pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #创建一颗子弹，并将其加入到编组bullets中
        fire_bullet(aisettings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def update_screen(ai_settings,screen,ship,aliens,bullets):
    '''更新屏幕上的图像，并切换到新屏幕'''
    #每次循环时都会重绘屏幕
    screen.fill(ai_settings.bg_color)

    #在飞船和外星人后面重绘所有的子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    #让最近回执的屏幕可见
    pygame.display.flip()
def update_bullets(ai_settings,screen,ship,aliens,bullets):
    '''更新子弹的位置，并删除已消失的子弹'''
    #更新子弹的位置
    bullets.update()

    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    # print(len(bullets))

    check_bullet_alien_collision(ai_settings,screen,ship,aliens,bullets)

def update_aliens(ai_settings,ship,aliens):
    ''''检查是否有外星人位于屏幕边缘，并更新整群外星人的位置'''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        print('ship hit !!!')

def get_number_aliens_x(ai_settings,alien_width):
    '''计算每行可容纳多少个外星人'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    return  number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    '''创建一群外星人并将其放在当前行'''

    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def creat_fleet(ai_settings,screen,ship,aliens):

    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)

    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
def get_number_rows(ai_settings,ship_height,alien_height):
    '''计算屏幕可容纳多少行外星人'''
    available_space_y = (ai_settings.screen_height - 3 * (alien_height) - ship_height)
    number_rows = int(available_space_y/ (2 * alien_height))

    return number_rows

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)



def check_fleet_edges(ai_settings,aliens):
    '''有外星人到达边缘采取相应的措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break


def change_fleet_direction(ai_settings,aliens):
    '''将整群外星人下移，并改变他们的方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_bullet_alien_collision(ai_settings,screen,ship,aliens,bullets):
    '''响应子弹和外星人的碰撞'''
    #删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        creat_fleet(ai_settings, screen, ship, aliens)

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    '''响应被外星人撞到的飞船'''
    #将ships——left 减 1
    stats.ship_left -= 1

    #清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()

    #创建一群新的外星人，并将飞船放到屏幕底端中央

    creat_fleet(ai_settings,screen,ship,aliens)
    ship.center_ship()


    #暂停
    sleep(0.5)

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    #检测外星人和飞船碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)



