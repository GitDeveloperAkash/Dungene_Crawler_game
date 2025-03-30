import pygame
import math

class weapon():
    def __init__(self, image):
        self.original_image = image
        self.original_image = pygame.transform.scale(self.original_image, (50, 50))
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())

    def update(self, player):
        # Update the weapon's position and angle based on the player's position
        self.rect.center = player.rect.center       
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        pos = pygame.mouse.get_pos()
        dx = pos[0] - self.rect.centerx
        dy = pos[1] - self.rect.centery
        self.angle = (180 / 3.14) * -math.atan2(dy, dx)
        self.image = pygame.transform.rotate(self.original_image, self.angle)

    def draw(self, screen):
        # Draw the weapon on the screen
        screen.blit(self.image, self.rect)  