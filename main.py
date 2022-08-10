import pygame
import sys
import random
# import neccesary libraries
import paddle
import ball
# import custom scripts

pygame.init()
# initialize pygame
screen_size = [800, 800]
display = pygame.display.set_mode((screen_size))
# used for screen

clock = pygame.time.Clock()

paddle_attributes = {(100, 100):[pygame.K_s, pygame.K_w], (700, 100):[pygame.K_DOWN, pygame.K_UP]}
# position, controls for paddles
paddles = []
# list of all paddles

for pos, controls in paddle_attributes.items():
    paddles.append(paddle.Paddle(pos, (14, 14), controls, screen_size))
# adding paddles to paddles list

ball_sprite = pygame.sprite.GroupSingle(ball.Ball((200, 100), (7, 7), pygame.math.Vector2(random.choice([-1, 1]), random.choice([-1, 1])), screen_size))
# creating the ball

while True:
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for pad in paddles:
        pad.update_paddle(display, ball_sprite)
    # updating paddles

    ball_sprite.update(ball.Ball.direction * ball.Ball.speed)
    ball_sprite.draw(display)
    # updating and drawing ball

    ball_sprite.sprite.collision_check()
    # checking for ball collisions
        
    pygame.display.update()
    clock.tick(60)
    # update display at 60 frames/second