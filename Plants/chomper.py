import pygame
class Chomper:
    def __init__(self, texture_name, x, y, screen):
        self.texture_name = texture_name
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.Surface((1280, 720))
        self.rect = self.image.get_rect()
        self.texture_coordinates = {
            "upper_jaw": (),
            "lower_jaw": (),
            "lower_teeth": (),
            "back_teeth": (),
            "tongue": (),
            "spike": (),
            "head_leaf1": (),
            "head_leaf2": (),
            "head_leaf3": (),
            "head_leaf4": (),
            "stem1": (),
            "stem2": (),
            "stem3": (),
            "ground_leaf1": (),
            "ground_leaf2": (),
            "ground_leaf3": (),
            "ground_leaf4": (),
            "ground_leaf5": (),
            "ground_leaf6": (),
            "zombie_arm1": (),
            "zombie_arm2": (),
            "stomach": (),

            
        }
        atlas_image_path = 'Plants/Assets/PC Computer - Plants vs Zombies - Chomper.png'
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