import pygame
import config 
import math

class player():
    def __init__(self, character_list, character_index, health = 100):
        self.health = health    
        self.character_index = character_index
        self.animation_frames = character_list[character_index]
        self.frame_index = 0
        self.time_gap = pygame.time.get_ticks()
        self.image = pygame.transform.scale(self.animation_frames[self.frame_index], (50, 50))      
        self.flip = False        
        self.rect = pygame.Rect(120, 120, self.image.get_width(), self.image.get_height())  # Example rect for the character
        self.Alive = True

    def update(self):
        if self.health <= 0:
            self.health = 0
            self.Alive = False
                                
        refresh_time = config.REFRESH_TIME
        if pygame.time.get_ticks() - self.time_gap > refresh_time:
            self.frame_index += 1
            if self.frame_index >= len(self.animation_frames):
                self.frame_index = 0
            self.time_gap = pygame.time.get_ticks()
        self.image = pygame.transform.scale(self.animation_frames[self.frame_index], (50, 50))

    def move(self, dx, dy):               
        if(dx < 0):
            self.flip = True
        if(dx > 0):
            self.flip = False

        if(dx != 0 and dy != 0):
            # Normalize the diagonal movement          
            dx = dx * math.sqrt(2)/2
            dy = dy * math.sqrt(2)/2 
            
        self.rect.x += dx       
        self.rect.y += dy
    
    def drow(self, screen):
        # Draw the character on the screen
        if self.character_index == 0:
            screen.blit( pygame.transform.flip(self.image, self.flip, False), (self.rect.x, self.rect.y - config.OFFSET))
        else:                        
            screen.blit( pygame.transform.flip(self.image, self.flip, False), self.rect)
        pygame.draw.rect(screen, config.GREEN, self.rect, 1)

    def display_health(self, screen):
        # Display the health bar above the character
        health_bar_width = 50
        health_bar_height = 10
        health_ratio = self.health / 100
        health_bar_x = self.rect.x + (self.rect.width - health_bar_width) // 2  
        health_bar_y = self.rect.y - health_bar_height - 5
        pygame.draw.rect(screen, config.RED, (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
        pygame.draw.rect(screen, config.GREEN, (health_bar_x, health_bar_y, health_bar_width * health_ratio, health_bar_height))
        font = pygame.font.Font(None, 24)
        text_surface = font.render(str(self.health), True, config.GREEN)
        text_rect = text_surface.get_rect(center=(self.rect.centerx, health_bar_y - 10))
        screen.blit(text_surface, text_rect)
        