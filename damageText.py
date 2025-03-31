import pygame
import config   

class damageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, color = config.RED):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.damage = damage
        self.color = color
        self.font = pygame.font.Font(None, 36)
        self.image = self.font.render(str(damage), True, color)
        self.rect = self.image.get_rect(center=(x, y))
        self.time_gap = pygame.time.get_ticks()
        self.alive = True
        self.speed = 1
    
    def update(self):
        # Update the position of the damage text
        if self.alive:
            self.y -= self.speed
            self.rect.y = self.y
            if pygame.time.get_ticks() - self.time_gap > config.DAMAGE_TEXT_LIFETIME:
                self.alive = False
                self.kill()
        else:
            self.kill()
        # Remove the sprite after a certain time

