import pygame
from objects import *
from config import *
from enum import Enum
import numpy as np


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


def init_game():
    screen = pygame.display.set_mode(SCREENSIZE)
    pygame.display.set_caption('Аркада')
    return screen


def return_states(lose, reward, points):
    return lose, reward, points


def move(self, action):
    # [straight, right, left]
    clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
    idx = clock_wise.index(self.direction)
    if np.array_equal(action, [1, 0, 0]):
        new_dir = clock_wise[idx]  # no change
    elif np.array_equal(action, [0, 1, 0]):
        next_idx = (idx + 1) % 4
        new_dir = clock_wise[next_idx]  # right turn r -> d -> l -> u
    else:  # [0, 0, 1]
        next_idx = (idx - 1) % 4
        new_dir = clock_wise[next_idx]  # left turn r -> u -> l -> d
    self.direction = new_dir
    x = player.rect.x
    y = player.rect.y
    if self.direction == Direction.RIGHT:
        x += player.speed
    elif self.direction == Direction.LEFT:
        x -= player.speed
    elif self.direction == Direction.DOWN:
        y += player.speed
    elif self.direction == Direction.UP:
        y -= player.speed


def main():
    screen = init_game()

    # startInterface(screen, START_BUTTONS_IMAGEPATHS)

    init_time = pygame.time.get_ticks()

    x = 5
    time_start = 0
    time_start_shield = 0
    is_boost_attack = False
    is_boost_ammo = False
    is_boost_shield = False
    is_boss_coming = False
    is_boss_dead = True
    # Тики и счетчики
    FPS = 60
    clock = time.Clock()
    boss_reload = 0
    # Счетчик врагов и усложнения

    enem_count = 1
    koeficient = 0.5
    harder = 100

    NUR = FPS
    NUR_count = 0
    fps_fiks = FPS * 1
    fps_fiks_count = 0

    FPS * koeficient
    NBR_count = 0
    lines = 12
    points = 0
    check_one_boost = True

    # Исходы игры
    game = True
    win = False
    lose = False
    player.hp = 3
    player.rect.x = win_rez_x / 2
    player.rect.y = win_rez_y * 0.9

    reward = 0

    # Генерация начального HP
    for i in range(player.hp):
        add_heart(x)
        x += win_rez_x / 8

    last_shot = pygame.time.get_ticks()

    # Игровой цикл
    while game:
        clock.tick(FPS)
        if not lose:
            time_to_boost = round((pygame.time.get_ticks() - init_time) / 1000)
            time_label = font2.render('Time:', True, (0, 0, 0))
            time_text = font2.render(str(time_to_boost), True, (0, 0, 0))

            text_points = font2.render('Points:', True, (0, 0, 0))
            text_points_count = font2.render(str(points), True, (0, 0, 0))

            NUR_count += 1
            NBR_count += 1
            fps_fiks_count += 1
            # Время спавна бустов
            if time_to_boost % 20 == 0 and check_one_boost and time_to_boost != 0:
                boost_generate(lines)
                check_one_boost = False

            if time_to_boost % 21 == 0:
                check_one_boost = True

            # Условие босса
            if points % 100 <= 2 and is_boss_dead and points >= 100:
                is_boss_dead = False
                is_boss_coming = True
                release_boss()

            # Прорисовка фона и моделек
            screen.blit(background, (0, 0))
            player.draw(screen)

            for boost in boosts:
                boost.draw(screen)
                boost.move("DOWN")

            for enemy in enemies:
                enemy.draw(screen)
                enemy.move('DOWN')

            # Функционал босса
            for boss in boss_container:
                boss.draw(screen)
                if boss.hp >= 99:
                    if boss.rect.y <= win_rez_y / 10:
                        boss.move("DOWN")
                boss.first()
                if boss.hp <= 50:
                    boss.second()
                # if boss.hp <= 60:

                if boss.shoted:
                    if boss.shoted_count == 30:
                        points += boss.give_points
                        boss_container.remove(boss)
                        is_boss_coming = False
                        is_boss_dead = True

                    else:
                        boss.shoted_count += 1
                boss_reload += 1
                if boss_reload >= 50:
                    generate_boss_bullets(boss)
                    if boss.hp <= 40:
                        generate_boss_bullets(boss)
                    boss_reload = 0

                for bullet in bullets:
                    if sprite.collide_rect(bullet, boss):
                        bullets.remove(bullet)
                        if boss.hp > 1:
                            boss.hp -= 1
                            punch.play()
                        elif boss.hp == 1:
                            boss.killed()
                            crash.play()

            for boss_bullet in boss_bullets:
                boss_bullet.draw(screen)
                boss_bullet.move('DOWN')
                if boss_bullet.rect.y <= -10:
                    boss_bullets.remove(boss_bullet)

                if sprite.collide_rect(boss_bullet, player):
                    if not is_boost_shield:
                        if player.hp > 0:
                            boss_bullets.remove(boss_bullet)
                            player.hp -= 1
                            reward -= 5
                            hearts.pop(len(hearts) - 1)
                            x -= win_rez_x / 8
                            crash.play()

            if fps_fiks_count == fps_fiks:
                fps_fiks_count = 0
                # усложнение
                if points != 0 and points % harder == 0:
                    if 1 >= koeficient > 0.25:
                        koeficient -= 0.1
                    NBR = FPS * koeficient
                    if enem_count < 3:
                        enem_count += 1
                    harder += 100
                    NUR -= 5

            # Генерация врагов
            if not is_boss_coming:
                if NUR_count >= NUR:
                    for i in range(enem_count):
                        enemy_generate(lines)
                        # enem.play()
                    NUR_count = 0

            # Прорисовка и движение пуль
            for bullet in bullets:
                bullet.draw(screen)
                bullet.move('UP')
                if bullet.rect.y <= -10:
                    bullets.remove(bullet)

            # 23.07.2022 Boost функционал
            for boost in boosts:
                if sprite.collide_rect(boost, player):
                    enem.play()
                    reward += 5
                    if boost.boost_type == "regen":
                        boosts.remove(boost)
                        player.hp += 1
                        add_heart(x)
                        x += win_rez_x / 8

                    if boost.boost_type == "ammo":
                        time_start = pygame.time.get_ticks()
                        is_boost_ammo = True
                        boosts.remove(boost)
                    if boost.boost_type == "shield":
                        time_start_shield = pygame.time.get_ticks()
                        is_boost_shield = True
                        boosts.remove(boost)
                    if boost.boost_type == "clean":
                        time_start_shield = pygame.time.get_ticks()
                        boosts.remove(boost)
                        enemies.clear()

            # Отсчет времени буста для пуль
            if is_boost_ammo == True:
                is_boost_attack = True
                if ((5000 - (pygame.time.get_ticks() - time_start)) / 1000) <= 0:
                    is_boost_attack = False
                    is_boost_ammo = False

            # Отсчет времени буста для щита
            if is_boost_shield:
                shield_icon.draw(screen)
                if ((5000 - (pygame.time.get_ticks() - time_start_shield)) / 1000) <= 0:
                    is_boost_shield = False

            for enemy in enemies:
                if enemy.shoted == True:
                    if enemy.shoted_count == 5:
                        points += enemy.give_points
                        enemies.remove(enemy)
                        reward

                    else:
                        enemy.shoted_count += 1

                for bullet in bullets:
                    if sprite.collide_rect(enemy, bullet):
                        bullets.remove(bullet)
                        if enemy.hp > 1:
                            enemy.hp -= 1
                            punch.play()
                        elif enemy.hp == 1:
                            enemy.killed()

                            crash.play()

                if enemy.rect.y > win_rez_y - 5:
                    if not is_boost_shield:
                        if player.hp > 0:
                            player.hp -= 1
                            reward -= 5
                            hearts.pop(len(hearts) - 1)
                            x -= win_rez_x / 8
                    enemies.remove(enemy)
                    enem.play()

                if sprite.collide_rect(enemy, player):
                    # if player.hp > 1:
                    if not is_boost_shield:
                        if player.hp > 0:
                            player.hp -= 1
                            reward -= 5
                            hearts.pop(len(hearts) - 1)
                            x -= win_rez_x / 8
                    enemies.remove(enemy)
                    enem.play()

                    # elif player.hp == 1:
                    #     enem.play()
                    #     lose = True

            # Управление
            keys_pressed = key.get_pressed()

            if keys_pressed[K_LEFT] and player.rect.x > 5:
                player.rect.x -= player.speed
            if keys_pressed[K_RIGHT] and player.rect.x < win_rez_x - player.size - 5:
                player.rect.x += player.speed
            if keys_pressed[K_UP] and player.rect.y > win_rez_y - win_rez_y / 3:
                player.rect.y -= player.speed
            if keys_pressed[K_DOWN] and player.rect.y < win_rez_y - player.size - 20:
                player.rect.y += player.speed
            if is_boost_attack:
                if keys_pressed[K_SPACE]:
                    punch.play()
                    generate_bullets()

            if player.hp <= 0:
                reward -= 10
                lose = True

            return_states(lose, reward, points)

            if points % 50 <= 2 and points >= 50:
                reward += 10

            if not is_boost_attack:
                now = pygame.time.get_ticks()
                if now - last_shot > 300:  # задержка в миллисекундах
                    punch.play()
                    generate_bullets()
                    last_shot = now
            else:
                punch.play()
                generate_bullets()

            for e in event.get():
                if e.type == QUIT:
                    game = False

            # Прорисовка интерфейса
            screen.blit(bush, (0, 0))
            screen.blit(text_points, (5, win_rez_x // 12))
            screen.blit(text_points_count, (win_rez_x // 5, win_rez_x // 12))
            screen.blit(time_label, (5, win_rez_x // 8))
            screen.blit(time_text, (win_rez_x // 5, win_rez_x // 8))
            for heart in hearts:
                heart.draw(screen)


        display.flip()


if __name__ == '__main__':
    while True:
        main()
