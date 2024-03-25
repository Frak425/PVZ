import pygame
class Gravebuster:
    def __init__(self, texture_name, x, y, screen):
        self.texture_name = texture_name
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.Surface((1280, 720))
        self.rect = self.image.get_rect()
        self.texture_coordinates = {
            "body": (),
            "eyebrows": (),
            "leg1": (),
            "leg2": (),
            "leg3": (),
            "leg4": (),
            "leg5": (),
            "leg6": (),
            "vine_wreath": (),
            "single_bulb": (),
            "double_bulb": ()
        }
        atlas_image_path = 'Plants/Assets/PC Computer - Plants vs Zombies - Grave Buster.png'
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