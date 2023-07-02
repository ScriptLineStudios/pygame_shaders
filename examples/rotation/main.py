import pygame
import pygame_shaders
import glm

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF)

display = pygame.Surface((600, 600))

screen_shader = pygame_shaders.Shader("rotate.glsl", 
pygame_shaders.DEFAULT_FRAGMENT_SHADER, display) 

img = pygame.transform.flip(pygame.image.load("../../docs/assets/pfp.png"), False, True)

target_surface = pygame.Surface((200, 200))
target_surface.blit(img, (0, 0))

shader = pygame_shaders.Shader("rotate.glsl", pygame_shaders.DEFAULT_FRAGMENT_SHADER, target_surface) #<- give it to our shader
rotation = glm.mat4()
dt = 0

while True:
    shader.clear((0, 0, 0))
    display.fill((10, 20, 30))

    target_surface.blit(img, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    dt += 0.05

    rotation = glm.mat4()
    rotation = glm.rotate(rotation, dt, glm.vec3(1, 1, 1))
    shader.send("rotation", [*rotation[0], *rotation[1], *rotation[2], *rotation[3]])

    rotation = glm.mat4()
    rotation = glm.rotate(rotation, dt, glm.vec3(-2, -2, -2))
    screen_shader.send("rotation", [*rotation[0], *rotation[1], *rotation[2], *rotation[3]])

    screen_shader.render_direct(pygame.Rect(0, 0, 600, 600)) 
    shader.render_direct(pygame.Rect(0, 0, 100, 100)) 

    pygame.display.flip()
    clock.tick(60)
