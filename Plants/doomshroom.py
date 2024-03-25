import pygame
class Doomshroom:
    def __init__(self, texture_name, x, y, screen):
        self.texture_name = texture_name
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.Surface((1280, 720))
        self.rect = self.image.get_rect()
        self.texture_coordinates = {
            "small_eyes_closed": (),
            "small_eyes_open": (),
            "medium": (),
            "large": (),
            "stem": (),
            "hole_light": (),
            "hole_dark": (),
            "dirt_light": (),
            "dirt_dark": (),
            "shattered_large_red": (),
            "shattered_small_red": (),
            "shattered_large_orange": (),
            "shattered_small_orange": (),
            "water_large_lb": (),
            "water_small_lb": (),
            "water_large_db": (),
            "water_small_db": ()
        }
        atlas_image_path = 'Plants/Assets/PC Computer - Plants vs Zombies - Doomshroom.png'
        self.atlas_surface = pygame.image.load(atlas_image_path).convert_alpha()

    def update_position(self, x, y):
        # Update the position of the Tallnut instance
        self.x = x
        self.y = y
        self.rect.topleft = (x, y)

    def draw(self):
        x, y, w, h = self.texture_coordinates[self.texture_name]
        self.image.blit(self.atlas_surface, (0, 0), (x, y, w, h))
        self.screen.blit(self.image, self.rect.topleft)