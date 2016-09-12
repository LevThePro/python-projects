
import pygame
import sys
from pygame.locals import *

pygame.init()

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

screen = pygame.display.set_mode((800, 700))
screen.fill((255, 255, 255))
pygame.display.set_caption('Pong')
font = pygame.font.SysFont(None, 36)

main_clock = pygame.time.Clock()


score_SOnic = 0
score_opponent = 0
lives_SOnic = 10
lives_opponent = 10
alive = True

SOnic = pygame.Rect(700, 600, 60, 10)
SOnic_speed = 1000

move_left = False
move_right = True

move_left = False
move_right = False

opponent = pygame.Rect(100,100,60,10)
opponent_speed = 10

move_left2 = False
move_right2 = True

move_left2 = False
move_right2 = False

#image = pygame.image.load('redselector.png')

def draw_screen():
    screen.fill((0,0,0))
def draw_opponent():
    pygame.draw.rect(screen, (0, 255, 0),opponent)
def draw_SOnic():
    pygame.draw.rect(screen, (0, 0, 255), SOnic)

def draw_text(display_string, font, surface, x, y):
    text_display = font.render(display_string, 1, (255, 255, 255))
    text_rect = text_display.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_display, text_rect)

x_position = 650
y_position = 550
last_x = x_position
last_y = y_position
ball = pygame.draw.circle(screen, (255,255,255), (x_position, y_position), 5, 0)
ball_can_move = False

speed = [5,-5]



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                move_right = False
                move_left = True
            if event.key == K_d:
                move_left = False
                move_right = True
        if event.type == KEYUP:
            if event.key == K_a:
                move_left = False
            if event.key == K_d:
                move_right = False
            if alive:
                if event.key == K_SPACE:
                    ball_can_move = True
            if not alive:
                if event.key == K_RETURN:
                    alive = True
                    lives.SOnic = 3
                    score = 0
                    ball_can_move = False

        if event.type == KEYDOWN:
            if event.key == K_j:
                move_right2 = False
                move_left2 = True
            if event.key == K_l:
                move_left2 = False
                move_right2 = True
        if event.type == KEYUP:
            if event.key == K_j:
                move_left2 = False
            if event.key == K_l:
                move_right2 = False
            if alive:
                if event.key == K_SPACE:
                    ball_can_move = True
            if not alive:
                if event.key == K_RETURN:
                    alive = True
                    lives.opponent = 3
                    score = 0
                    ball_can_move = False

    main_clock.tick(60)

    if move_left and SOnic.left > 0:
        SOnic.x -= SOnic_speed
    if move_right and SOnic.right < 800:
        SOnic.x += SOnic_speed

    if move_left2 and opponent.left > 0:
        opponent.x -= opponent_speed
    if move_right2 and opponent.right < 800:
        opponent.x += opponent_speed

    if ball_can_move:
        last_x = x_position
        last_y = y_position

        x_position += speed[0]
        y_position += speed[1]
        if ball.x <= 0:
            x_position = 15
            speed[0] = -speed[0]
        elif ball.x >= 800:
            x_position = 785
            speed[0] = -speed[0]
        if ball.y <= 0:
           lives_opponent -= 1
           score_opponent += 1
           ball_can_move = False
        elif ball.y >=600:
            lives_Sonic -= 1
            score_Sonic += 1
            ball_can_move = False

        if ball.colliderect(SOnic):
            y_position -= 15
            speed[1] = -speed[1]

        if ball.colliderect(opponent):
            y_position += 15
            speed[-1] = -speed[-1]

        move_direction = ((x_position - last_x), (y_position - last_y))


    else:
        x_position = SOnic.x + 30
        y_position = 380

        x_position = opponent.x + 30
        y_position = 380

    draw_screen()
    draw_SOnic()
    draw_opponent()
    ball = pygame.draw.circle(screen, (255, 255, 255), (x_position, y_position), 6, 0)

    pygame.draw.circle(screen, WHITE,(400,350),75,1)
    pygame.draw.line(screen, WHITE,(0,350),(800,350),1)

    if alive:
        draw_text('Score: %s' % (score_SOnic), font, screen, 700, 5)
        draw_text('Score: %s' % (score_opponent), font, screen, 700, 600)
        draw_text('Player1 Lives: %s' % (lives_SOnic), font, screen, 5, 600)
        draw_text('Player2 Lives: %s' % (lives_opponent), font, screen, 5, 5)
    else:
        draw_text('Game Over', font, screen, 255, 5)
        draw_text('Press Enter to Play Again', font, screen, 180, 50)

    pygame.display.update()
