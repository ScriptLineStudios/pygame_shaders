import pygame
import pygame_shaders
import math
import random

random.seed(601)
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF)

display = pygame.Surface((400, 400))

img = pygame.Surface((400, 400))
for y in range(400):
    for x in range(400):
        if math.dist([x, y], [200, 200]) < 100:
            v = random.randrange(0, 255)
            img.set_at((x, y), (v, v, v))

shader_res = [img, img]
bg_shader = pygame_shaders.Shader(pygame_shaders.DEFAULT_VERTEX_SHADER, "frag.glsl", shader_res[0])

screen_shader = pygame_shaders.DefaultScreenShader(display)

running = True
dt = 1.0
i = 0
while running:
    display.fill((255, 255, 255))

    dt += .01

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    bg_shader.set_target_surface(shader_res[1 - i])
    
    new = bg_shader.render()
    shader_res[i] = new
    i = 1 - i

    display.blit(shader_res[1], (0, 0))
    
    screen_shader.render()
    pygame.display.flip()

    clock.tick(60)
    pygame.display.set_caption(f"{clock.get_fps()}")
