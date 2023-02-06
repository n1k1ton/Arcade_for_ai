from config import *
from random import randint
from pygame import *
from modules import *
import os

background = transform.scale(image.load(os.path.join(MEDIA_DIR, 'images/background.jpg')), (win_rez_x, win_rez_y))
bush = transform.scale(image.load(os.path.join(MEDIA_DIR, 'images/Bush.png')), (win_rez_x, win_rez_y))
player = Unit(os.path.join(MEDIA_DIR, 'images/player2.png'), win_rez_x / 2, win_rez_y * 0.9, win_rez_x / 6,
              win_rez_x / 80, 3)

boss_bullets = []
boss_container = []


def release_boss():
    boss = Boss(os.path.join(MEDIA_DIR, 'images/boss.png'), win_rez_x / 2, win_rez_y / 100, win_rez_x / 2,
                win_rez_x / 200, 100, 20)
    boss_container.append(boss)


def generate_boss_bullets(boss):
    random_pos = randint(boss.rect.x, boss.rect.x + boss.size)
    boss_bullets.append(
        Unit(os.path.join(MEDIA_DIR, 'images/boss_bullet.png'), random_pos, boss.rect.y + boss.size / 2, win_rez_x / 10,
             win_rez_y / 100, 0))


enemies = []


def enemy_generate(lines):
    line = randint(1, lines)
    pos_x = win_rez_x // lines * line - win_rez_x // lines + 3
    randomEnemy = randint(1, 10)
    if randomEnemy >= 1 and randomEnemy <= 5:
        enemy = Enemy(os.path.join(MEDIA_DIR, 'images/enemy1.png'), pos_x, win_rez_y / 100, win_rez_x / lines,
                      win_rez_x * 1 / 400, 1, 1)
        enemies.append(enemy)
    elif randomEnemy >= 6 and randomEnemy <= 8:
        enemy = Enemy(os.path.join(MEDIA_DIR, 'images/enemy2.png'), pos_x, win_rez_y / 100, win_rez_x / lines,
                      win_rez_x * 1 / 400, 2, 2)
        enemies.append(enemy)
    elif randomEnemy >= 9 and randomEnemy <= 10:
        enemy = Enemy(os.path.join(MEDIA_DIR, 'images/enemy3.png'), pos_x, win_rez_y / 100, win_rez_x / lines,
                      win_rez_x * 1 / 400, 3, 3)
        enemies.append(enemy)


hearts = []


def add_heart(x):
    heart = Unit(os.path.join(MEDIA_DIR, 'images/health.png'), x, win_rez_y / 8, win_rez_x / 8, None, None)
    hearts.append(heart)


shield_icon = Unit(os.path.join(MEDIA_DIR, 'images/shield_icon.png'), 5, win_rez_y / 4, win_rez_x / 8, None, None)

bullets = []


def generate_bullets():
    bullets.append(Unit(os.path.join(MEDIA_DIR, 'images/snaryad.png'), player.rect.x + player.size / 2 - win_rez_x / 30,
                        player.rect.y, win_rez_x / 15, win_rez_y / 15, 0))


boosts = []


def boost_generate(lines):
    line = randint(1, lines)
    pos_x = win_rez_x // lines * line - win_rez_x // lines + 3
    randomBoost = randint(1, 4)
    if randomBoost == 1:
        boost = Boost((os.path.join(MEDIA_DIR, 'images/regen.png')), pos_x, win_rez_y / 100, win_rez_x / lines,
                      win_rez_x / 400, None, 'regen')
        boosts.append(boost)
    elif randomBoost == 2:
        boost = Boost((os.path.join(MEDIA_DIR, 'images/ammo.png')), pos_x, win_rez_y / 100, win_rez_x / lines,
                      win_rez_x / 400, None, 'ammo')
        boosts.append(boost)
    elif randomBoost == 3:
        boost = Boost((os.path.join(MEDIA_DIR, 'images/shield.png')), pos_x, win_rez_y / 100, win_rez_x / lines,
                      win_rez_x / 400, None, 'shield')
        boosts.append(boost)
    elif randomBoost == 4:
        boost = Boost((os.path.join(MEDIA_DIR, 'images/destroy.png')), pos_x, win_rez_y / 100, win_rez_x / lines,
                      win_rez_x / 400, None, 'clean')
        boosts.append(boost)


font.init()
font1 = font.SysFont('arialblack', 70)
font2 = font.SysFont('arialblack', 20)
win_text = font1.render('YOU WIN!', True, (0, 255, 0))
lose_text = font1.render('YOU LOST!', True, (255, 0, 0))
