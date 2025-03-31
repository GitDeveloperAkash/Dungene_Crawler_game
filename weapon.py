import pygame
import math
import config
import random

class weapon():
    def __init__(self, image, arrow_image):
        self.arrow_image = arrow_image
        self.original_image = image
        self.original_image = pygame.transform.scale(self.original_image, (50, 50))
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.trigger = False

    def update(self, player):
        new_arrow = None
        # Update the weapon's position and angle based on the player's position
        self.rect.center = player.rect.center       
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        pos = pygame.mouse.get_pos()
        dx = pos[0] - self.rect.centerx
        dy = pos[1] - self.rect.centery
        self.angle = (180 / 3.14) * -math.atan2(dy, dx)
        self.image = pygame.transform.rotate(self.original_image, self.angle)

        if pygame.mouse.get_pressed()[0] and not self.trigger:
            self.trigger = True
            # If the mouse is clicked, shoot an arrow            
            self.arrow_image = pygame.transform.scale(self.arrow_image, (50, 50))
            new_arrow = arrow(self.arrow_image, self.rect.centerx, self.rect.centery, self.angle)

        if not pygame.mouse.get_pressed()[0]:
            self.trigger = False
        return new_arrow              

    def draw(self, screen):
        # Draw the weapon on the screen
        screen.blit(self.image, self.rect)  


class arrow(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle = 0):
        super().__init__()
        self.original_image = image
        self.original_image = pygame.transform.scale(self.original_image, (15, 15))
        self.angle = angle
        self.image = pygame.transform.rotate(self.original_image, self.angle-90)
        self.rect = self.image.get_rect(center=(x, y))

        self.dx = math.cos(math.radians(self.angle)) * config.ARROW_SPEED
        self.dy = -( math.sin(math.radians(self.angle)) * config.ARROW_SPEED)

    def update(self, enemy_list):
        # Update the arrow's position based on its speed and angle
        self.rect.x += self.dx
        self.rect.y += self.dy
        damage = 0
        enemy_pos = None

        # Check if the arrow is off the screen
        if (self.rect.x < 0 or self.rect.x > config.SCREEN_WIDTH or 
            self.rect.y < 0 or self.rect.y > config.SCREEN_HEIGHT):
            self.kill()

        # Check for collision with enemies
        for enemy in enemy_list:
            if self.rect.colliderect(enemy.rect) and enemy.Alive:
                damage = random.randint(5, 15)  # Random damage between 5 and 15
                enemy.health -= damage
                enemy_pos = enemy.rect
                self.kill()
                break

        return damage, enemy_pos

    def drow(self, screen):
        # Draw the arrow on the screen
        screen.blit(self.image, self.rect)
        
        