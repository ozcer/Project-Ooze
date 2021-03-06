import pygame

from src.const import *
from src.game_objects.scenic import Scenic


class Period(Scenic):
    def __init__(self, *args,
                 length,
                 name,
                 left=DISPLAY_WIDTH,
                 depth=PERIOD_DEPTH,
                 color=OLIVE,
                 ):
        self.images = {"init": pygame.Surface((length, TIMELINE_HEIGHT))}
        x = left + length / 2
        y = DISPLAY_HEIGHT - TIMELINE_HEIGHT / 2
        super().__init__(*args, pos=(x, y), depth=depth, init_image_key="init")
        
        self.name = name
        self.length = self.rect.w

        self.color = color
        self.image.fill(self.color)
        
        self.dx = 0
        self.dy = 0
    
    def set_left(self, left):
        self.x = left + self.rect.w / 2
        self.y = DISPLAY_HEIGHT - TIMELINE_HEIGHT / 2
        self.rect.center = (self.x, self.y)
    
    def display_name(self):
        text_surf = self.debug_font.render(f"{self.name}",
                                           True,
                                           BLACK)
        text_rect = text_surf.get_rect()
        text_rect.center = self.x, self.y
        self.game.surface.blit(text_surf, text_rect)
    
    
    def draw(self):
        super().draw()
        self.display_name()
    
    def update(self):
        super().update()