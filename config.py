from pygame import *
import os


#пути к папкам
BASE_DIR = os.path.curdir
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

#Инициализация музыки и звуков
mixer.init()
mixer.music.load(os.path.join(MEDIA_DIR, 'sounds/back_sound2.mp3'))
mixer.music.set_volume(0.1)
mixer.music.play(-1)




enem = mixer.Sound(os.path.join(MEDIA_DIR,'sounds/enem_sound.mp3'))
win_sound = mixer.Sound(os.path.join(MEDIA_DIR,'sounds/win_m.mp3'))
lose_sound = mixer.Sound(os.path.join(MEDIA_DIR,'sounds/lose_m.mp3'))
punch = mixer.Sound(os.path.join(MEDIA_DIR,'sounds/punch.mp3'))
crash = mixer.Sound(os.path.join(MEDIA_DIR,'sounds/crash.mp3'))


START_BUTTONS_IMAGEPATHS = [os.path.join(MEDIA_DIR, 'images/start1.png'), os.path.join(MEDIA_DIR, 'images/start2.png')]



#Размеры окна
win_rez_x = 400
win_rez_y = 700

#дисплей
SCREENSIZE = (win_rez_x, win_rez_y)




