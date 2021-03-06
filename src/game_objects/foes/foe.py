import pygame

from src.game_objects.dynamic import Dynamic
from src.const import *


class Foe(Dynamic):

    def __init__(self, *args, script, **kwargs):
        super().__init__(*args, **kwargs)
        self.script = script
        self.script.host = self
    
    def decayable(self):
        """
        Overriding decayable in GameObject
        :return: bool
        """
        return self.rect.right < 0
    
    def draw(self):
        super().draw()
    
    def is_alive(self):
        return self.hp > 0
    
    def update(self):
        super().update()
        self.script.update()
        if not self.is_alive():
            self.kill()



