import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import moderngl

class Texture:
    def __init__(self, surface, ctx):
        image = surface
        image = pygame.transform.flip(image, False, True)
        image_width,image_height = image.get_rect().size
        img_data = pygame.image.tostring(image,'RGBA')
        self.texture = ctx.texture(size=image.get_size(), components=4, data=img_data)

        self.texture.filter = (moderngl.NEAREST, moderngl.NEAREST)

    def use(self):
        self.texture.use()