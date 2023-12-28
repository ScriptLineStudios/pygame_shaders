import pygame
import pygame_shaders
import glm

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF)

display = pygame.Surface((600, 600))

screen_shader = pygame_shaders.DefaultScreenShader(display) # <- Here we supply our default display, it's this display which will be displayed onto the opengl context via the screen_shader

target_surface = pygame.Surface((200, 200))
target_surface.blit(pygame.image.load("../../docs/assets/pfp.png"), (0, 0))

shader = pygame_shaders.Shader(pygame_shaders.DEFAULT_VERTEX_SHADER, "default_frag.glsl", target_surface) #<- give it to our shader

t = 0
while True:
    display.fill((255, 255, 255))
    t += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.rect(display, (255, 0, 0), (200, 200, 20, 20))
    
    shader.send("time", t)
    target_shader = shader.render() 

    display.blit(target_shader, (0, 0))

    screen_shader.render() 

    pygame.display.flip()
    clock.tick(60)
