# pygame_shaders

## a library to easily intergrate shaders into your new or existing pygame projects

This project allows for GLSL shaders to easily be intergrated with either your new or existing Pygame projects without having to touch OpenGL.

```python
import pygame
import pygame_shaders

pygame.init()

screen = pygame.display.set_mode((600, 600), pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF) #Create the main Python display
display = pygame.Surface((100, 100)) #Create a pygame surface, this is where you will do all your pygame rendering 
display.set_colorkey((0,0,0))

screen_shader = pygame_shaders.Shader("shaders/vertex.txt", "shaders/default_frag.txt")

while True:
    pygame_shaders.clear()

    #your pygame code

    screen_shader.render(display) #Render the display onto the OpenGL display with the shader!

    pygame.display.flip()
    clock.tick(60)
```
