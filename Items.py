import pygame

class Items(pygame.sprite.Sprite):
    def __init__(self, x, y, item_type, animation_list):
        super().__init__()
        self.item_type = item_type
        self.animation_frames = animation_list[item_type]
        self.frame_index = 0
        self.image = pygame.transform.scale(self.animation_frames[self.frame_index], (50, 50))        
        self.rect = self.image.get_rect(center=(x, y))
        self.time_gap = pygame.time.get_ticks()
        self.refresh_time = 100