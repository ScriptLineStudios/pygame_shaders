import pygame
import pygame_shaders
import random

pygame.init()

screen = pygame.display.set_mode((800, 800), pygame.OPENGL | pygame.DOUBLEBUF)

clock = pygame.time.Clock()
display = pygame.Surface((50, 50))
display.set_at((10, 10), (255, 255, 255))
display.set_at((11, 10), (255, 255, 255))

conway_shader = pygame_shaders.Shader(pygame_shaders.DEFAULT_VERTEX_SHADER, "conway.glsl", display)
screen_shader = pygame_shaders.DefaultScreenShader(display)

texture = pygame_shaders.Texture(display, screen_shader.ctx)
texture.texture.bind_to_image(0)

x = 0
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

    new = conway_shader.render()
    display.blit(new, (0, 0))

    screen_shader.render()
    pygame.display.set_caption(f"FPS: {clock.get_fps()}")
    pygame.display.flip()
    clock.tick(60)
