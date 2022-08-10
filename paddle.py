import pygame
import block
import ball

class Paddle():
    def __init__(self, position, dimensions, inputs, screen_size):
        self.paddle_blocks = pygame.sprite.Group()
        self.speed = 5
        self.inputs = inputs

        self.axis_loop_amt = [3, 7]
        self.rect = pygame.Rect(position[0], position[1], dimensions[0] * self.axis_loop_amt[0], dimensions[1] * self.axis_loop_amt[1])

        self.screen_size = screen_size

        for x in range(self.axis_loop_amt[0]):
            for y in range(self.axis_loop_amt[1]):
                self.paddle_blocks.add(block.Block(self.rect.topleft + pygame.math.Vector2(x * dimensions[0], y * dimensions[1]), dimensions))

    def update_paddle(self, display, ball_sprite_group):
        keys = pygame.key.get_pressed()
        key_input = pygame.math.Vector2(0, keys[self.inputs[0]] - keys[self.inputs[1]]) * self.speed
        
        for block in self.paddle_blocks.sprites():
            if block.rect.colliderect(ball_sprite_group.sprite.rect):
                inverse_dir = ball.Ball.direction * -1
                ball_sprite_group.sprite.rect.topleft += inverse_dir * ball.Ball.speed

                self.paddle_blocks.remove(block)
                ball.Ball.direction.x *= -1

        if key_input.y > 0 and self.rect.bottom >= self.screen_size[1] or key_input.y < 0 and self.rect.top <= 0:
            key_input = pygame.math.Vector2(0, 0)

        self.rect.topleft += key_input
        self.paddle_blocks.update(key_input)

        self.paddle_blocks.draw(display)

    def __len__(self):
        return len(self.paddle_blocks)