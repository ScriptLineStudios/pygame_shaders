
import pygame
import pygame_shaders

pygame.init()

screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE)
display = pygame.Surface((600, 600))
display.set_colorkey((0, 0, 0))

shader = pygame_shaders.Shader(size=(600, 600), display=(600, 600), 
                        pos=(0, 0), vertex_path="shaders/vertex.txt", 
                        fragment_path="shaders/default_frag.txt")

while True:
    pygame_shaders.clear((100, 100, 100)) #Fill with the color you would like in the background
    display.fill((0, 0, 0)) #Fill with the color you set in the colorkey
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.draw.rect(display, (255, 0, 0), (20, 20, 20, 20)) #Draw a red rectangle to the display at (20, 20)
    
    shader.render(display) #Render the display onto the OpenGL display with the shaders!
    pygame.display.flip()