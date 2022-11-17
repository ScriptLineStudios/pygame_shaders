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

screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE)
display = pygame.Surface((600, 600))
display.set_colorkey((0, 0, 0))

shader = pygame_shaders.Shader(size=(600, 600), display=(600, 600), 
                        pos=(0, 0), vertex_path="shaders/vertex.txt", 
                        fragment_path="shaders/default_frag.txt", target_texture=display)

clock = pygame.time.Clock()

while True:
    pygame_shaders.clear((100, 100, 100)) #Fill with the color you would like in the background
    display.fill((0, 0, 0)) #Fill with the color you set in the colorkey
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.draw.rect(display, (255, 0, 0), (20, 20, 20, 20)) #Draw a red rectangle to the display at (20, 20)
    
    shader.render(display) #Render the display onto the OpenGL display with the shaders!
    pygame.display.flip()
    clock.tick(60)
```

# Overview

```pygame_shaders.Shader``` -> Initializes a new shader.

```python
pygame_shaders.Shader(shader_size: Tuple[int], window_size: Tuple[int], position: Tuple[int], vertex_shader_path: str, fragment_shader_path: str, target_texture: pygame.Surface)
```


```pygame_shaders.Shader.render``` -> Renders a shader to the display. If a surface is passed the shader will be rendered onto that Surface before being rendered onto the main display.

```python
pygame_shaders.Shader.render(surface: Optional[pygame.Surface])
```


```pygame_shaders.Shader.send``` -> Allows for uniforms to be passed to a shader.

```python
pygame_shaders.Shader.send(variable_name: str, data: List[float])
```


```pygame_shaders.clear``` -> Clears the display with a color.

```python
pygame_shaders.clear(color: Tuple[int])
```


