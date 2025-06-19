# Pygame Shaders
[![wakatime](https://wakatime.com/badge/github/ScriptLineStudios/pygame_shaders.svg)](https://wakatime.com/badge/github/ScriptLineStudios/pygame_shaders)
![Lines of code](https://img.shields.io/tokei/lines/github/ScriptLineStudios/pygame_shaders)

[![Downloads](https://pepy.tech/badge/pygame-shaders)](https://pepy.tech/project/pygame-shaders)
![PyPI](https://img.shields.io/pypi/v/pygame_shaders)
![PyPI - Format](https://img.shields.io/pypi/format/pygame_shaders)
[![Downloads](https://pepy.tech/badge/pygame-shaders/month)](https://pepy.tech/project/pygame-shaders)

## Easily integrate shaders into your new or existing pygame projects

This project allows for GLSL shaders to easily be intergrated with either your new or existing Pygame projects without having to touch OpenGL.

```python
import pygame
import pygame_shaders

pygame.init()

clock = pygame.time.Clock()

#Create an opengl pygame Surface, this will act as our opengl context.  
screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF)

#This is our main display we will do all of our standard pygame rendering on.
display = pygame.Surface((600, 600))

#The shader we are using to communicate with the opengl context (standard pygame drawing functionality does not work on opengl displays)
screen_shader = pygame_shaders.DefaultScreenShader(display) # <- Here we supply our default display, it's this display which will be displayed onto the opengl context via the screen_shader

#This is our shader object which we can use to render the given shaders onto the screen in various ways. 
shader = pygame_shaders.Shader(pygame_shaders.DEFAULT_VERTEX_SHADER, "fragment.glsl", screen) #<- Because we plan on using this shader for direct rendering (we supply the surface on which we plan to do said direct rendering in this case, screen) 

while True:
    #Fill the display with white
    display.fill((255, 255, 255))
    
    #Standard pygame event stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Render a rect onto the display using the standard pygame method for drawing rects.
    pygame.draw.rect(display, (255, 0, 0), (200, 200, 20, 20))
    
    #Render the contents of "display" (main surface) onto the opengl screen.
    screen_shader.render() 

    #Render the shader directly onto the display.
    shader.render_direct(pygame.Rect(0, 0, 100, 100)) 

    #Update the opengl context
    pygame.display.flip()
    clock.tick(60)
```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ScriptLineStudios/pygame_shaders&type=Date)](https://www.star-history.com/#ScriptLineStudios/pygame_shaders&Date)
