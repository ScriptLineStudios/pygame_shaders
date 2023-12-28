import pygame
import pygame_shaders
import math
import random

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF)

display = pygame.Surface((600, 600))

img = pygame.Surface((100, 100))
for y in range(100):  
    for x in range(100):
        img.set_at((x, y), (255, 255, 255))
        if (x == 0 or x == 100 - 1 or y == 0 or y == 100 - 1):
            img.set_at((x, y), (255, 255, 255))
        else:
            if random.randrange(0, 100) < 50:
                img.set_at((x, y), (0, 0, 0))

shader_res = [img, img]

bg_shader = pygame_shaders.Shader(pygame_shaders.DEFAULT_VERTEX_SHADER, "frag.glsl", shader_res[0])
screen_shader = pygame_shaders.DefaultScreenShader(display)

running = True
i = 0
count = 0
while running:
    display.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    #Set the target surface of the shader to the flipped version of i
    bg_shader.set_target_surface(shader_res[1 - i])
    
    #Peform the rendering of the shader onto the surface set above 
    new = bg_shader.render()

    #Set the index i to the new surface
    shader_res[i] = new

    #If i = 0 then we set surface 1 as the target, perfom the shader render and store the resulting surface in slot 0 we then flip i (i = 1) and blit the new i onto display. 

    #Flip i
    i = 1 - i
    count += 1

    #display the outputted shader onto the display
    display.blit(pygame.transform.scale(shader_res[1], (600, 600)), (0, 0))
    # pygame.draw.rect(display, (255, 0, 0), (0, 0, 600, 600))
    
    #Render the contents of display onto the opengl display
    screen_shader.render()

    #Update the opengl display
    pygame.display.flip()
    
    #Tick the clock
    clock.tick()
    pygame.display.set_caption(f"{clock.get_fps()}")