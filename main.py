import pygame
import pygame_shaders
from OpenGL.GL import *

pygame.init()
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK,
                            pygame.GL_CONTEXT_PROFILE_CORE)

screen = pygame.display.set_mode((600, 600), pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF)
display = pygame.Surface((300, 300))
display.set_colorkey((0,0,0))
clock = pygame.time.Clock()

bg_shader = pygame_shaders.Shader("shaders/vertex.txt", "shaders/fragment.txt")
screen_shader = pygame_shaders.Shader("shaders/vertex.txt", "shaders/default_frag.txt")

image = pygame.image.load("grass_0.png")
image.set_colorkey((0,0,0))

running = True
dt = 1.0

while running:
    dt += .01
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    pygame.display.set_caption(f"{clock.get_fps()}")
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    display.blit(image, (10, 10))

    bg_shader.send("time", [dt])
    bg_shader.send("resolution", [500.0, 500.0])
    
    bg_shader.render()
    screen_shader.render(display)

    pygame.display.flip()
    clock.tick(60)