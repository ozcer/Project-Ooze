import sys
import random
import pygame
from pygame.locals import *

from src.const import *
from src.player import Player
from src.wall import Wall

class Game:
    
    def __init__(self):
        # surfaces
        self.surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
        pygame.display.set_caption(CAPTION)
        pygame.init()
    
        self.sprite_groups = ["players", "walls"]
        self.entities = {sp: pygame.sprite.Group() for sp in self.sprite_groups}
        
        # init player spawn
        player = Player(self, (200, 100))
        self.entities["players"].add(player)
        
        # init wall cd
        self.wallCd = WALL_RATE / 2

        self.fps_clock = pygame.time.Clock()
        
        self.run()
    
        
    def run(self):
        while True:
            self.surface.fill(LIGHTGREY)
            
            for group in self.entities:
                self.entities[group].update()
                self.entities[group].draw(self.surface)
                
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
            # wall creation
            if self.wallCd <= 0:
                self.wallCd = WALL_RATE
                self.make_walls()
            self.wallCd -= 1
            
            # collision
            collision = pygame.sprite.groupcollide(self.entities["walls"], self.entities["players"], False, False)
            if collision:
                for wall in collision:
                    collision[wall][0].alive = False
                    wall.hit = True
                    
            pygame.display.update()
            self.fps_clock.tick(FPS)

    def make_walls(self):
        gap_height = random.randint(GAP_SIZE/2, DISPLAY_HEIGHT-GAP_SIZE/2)
        gap_top = gap_height - GAP_SIZE / 2
        gap_bottom = gap_height + GAP_SIZE / 2
        
        # top wall
        top_height = gap_top
        top_wall = Wall(self, (DISPLAY_WIDTH+WALL_WIDTH, top_height / 2), (WALL_WIDTH, top_height))
        self.entities["walls"].add(top_wall)
    
        # bottom wall
        bottom_height = DISPLAY_HEIGHT - gap_bottom
        bottom_wall = Wall(self, (DISPLAY_WIDTH+WALL_WIDTH, gap_bottom + bottom_height / 2), (WALL_WIDTH, bottom_height))
        self.entities["walls"].add(bottom_wall)
        
        
if __name__ == "__main__":
    Game()