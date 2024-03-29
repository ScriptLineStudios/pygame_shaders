import pygame
import pygame_shaders
import glm

pygame.init()

clock = pygame.time.Clock()

#Create an opengl pygame Surface, this will act as our opengl context.  
screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF)

#This is our main display we will do all of our standard pygame rendering on.
display = pygame.Surface((600, 600))

#The shader we are using to communicate with the opengl context (standard pygame drawing functionality does not work on opengl displays)
screen_shader = pygame_shaders.Shader(pygame_shaders.DEFAULT_VERTEX_SHADER, "screen_frag.glsl", display) # <- Here we supply our default display, it's this display which will be displayed onto the opengl context via the screen_shader

while True:
    #Fill the display with white
    display.fill((40, 60, 100))
    
    #Standard pygame event stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Render a rect onto the display using the standard pygame method for drawing rects.
    pygame.draw.rect(display, (255, 0, 0), (200, 200, 20, 20))
    
    #Render the contents of "display" (main surface) onto the opengl screen.
    screen_shader.render_direct(pygame.Rect(0, 0, 600, 600)) 

    #Update the opengl context
    pygame.display.flip()
    clock.tick(60)
