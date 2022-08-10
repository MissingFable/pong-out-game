import pygame
import random

class Block(pygame.sprite.Sprite):
    def __init__(self, position, dimensions):
        super().__init__()
        self.image = pygame.Surface(dimensions)
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = position
    
    def update(self, move_amt = 0, direct_move = False, direct_move_pos = pygame.math.Vector2(0, 0)):
        if not direct_move:
            self.rect.topleft += move_amt