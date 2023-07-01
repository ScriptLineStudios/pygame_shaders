import pygame
import pygame_shaders
import math
import random

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF)

display = pygame.Surface((600, 600))

screen_shader = pygame_shaders.DefaultScreenShader(display)
compute_shader = pygame_shaders.ComputeShader("compute.glsl")
surf = pygame.Surface((600, 600))
surf.fill((40, 100, 255))
display_shader = pygame_shaders.Shader(pygame_shaders.DEFAULT_VERTEX_SHADER, pygame_shaders.DEFAULT_FRAGMENT_SHADER, surf)


texture = pygame_shaders.Texture(surf, compute_shader.ctx)
dt = 0
while True:
    display.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    texture.bind(0, True, True)    
    compute_shader.dispatch(600, 600, 1)

    screen_shader.render()
    
    display_shader.set_target_texture(texture)
    display_shader.render_direct(pygame.Rect(0, 0, 600, 600), False)

    pygame.display.flip()

    clock.tick()
    # pygame.display.set_caption(f"{clock.get_fps()}")
