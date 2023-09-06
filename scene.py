import pygame as pg

class Scene(pg.sprite.Sprite):
    def __init__(self, img, placement):
        super().__init__()
        self.image = pg.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(bottomright = placement)

scene_sprities = pg.sprite.Group()
