# Pygame Shaders

## Easily intergrate shaders into your new or existing pygame projects

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
    
    screen_shader.render(display) #Render the display onto the OpenGL display with the shaders!
    pygame.display.flip()
```

# Overview

```pygame_shaders.Shader``` -> Initializes a new shader.
```python
pygame_shaders.Shader(shader_size: Tuple[int], window_size: Tuple[int], position: Tuple[int], vertex_shader_path: str, fragment_shader_path: str)
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

# Tutorial

## Installation
Guide coming soon!

## Your First Shader
Once you have pygame_shaders installed, creating a shader is simple:
```python
shader = pygame_shaders.Shader(shader_size: Tuple[int], window_size: Tuple[int], position: Tuple[int], vertex_shader_path: str, fragment_shader_path: str)
```

However before we can create any shaders. We must create our Pygame display. For this tutorial I will create a (600, 600) display. It is important for this display to contain the pygame.OPENGL, pygame.DOUBLEBUF and pygame.HWSURFACE flags. As this will allow us to render to the display using OpenGL. 
```python
screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE)
```

Now that this display has been marked as an OpenGL display, we will no longer be able to use any of Pygame's rendering functionality on this display. So lets create a regular Pygame surface. We will use this for all of our games rendering. For this tutorial ill keep the Surface the same size as the display but you could make it smaller or larger if you like.

```python
display = pygame.Surface((600, 600))
```

Note: When using pygame_shaders. Its good practice to set a transparent color for the surface so we can apply a background shader later. To do this I will set the color key to black.

```python
display.set_colorkey((0, 0, 0))
```

Finally! Lets create our shader. For this tutorial our shader will simpily take our Surface we created above and render it to the OpenGL display. The vertex and fragment shader will look like this.

vertex.glsl:
```glsl
#version 330 core

layout (location=0) in vec3 vertexPos;
layout (location=1) in vec2 vertexTexCoord;

out vec3 fragmentColor;
out vec2 fragmentTexCoord;

void main()
{
    gl_Position = vec4(vertexPos, 1.0);
    fragmentColor = vertexColor;
    fragmentTexCoord = vertexTexCoord;
}
```

fragment.glsl:
```glsl
#version 330 core

in vec3 fragmentColor;
in vec2 fragmentTexCoord;

out vec4 color;

uniform sampler2D imageTexture;

void main() {
    color = texture(imageTexture, fragmentTexCoord);
}
```

Note: All vertex shaders require ```layout (location=0) in vec3 vertexPos;``` and ```layout (location=1) in vec3 vertexTexCoord;``` if you would like to access texture coordinates.

Now lets create our Pygame shader! Ill give it a size the same as our display (600, 600) and a position of (0, 0) Note: (0, 0) in a shader = middle of the screen.

```python
shader = pygame_shaders.Shader((600, 600), (600, 600), (0, 0), "vertex.glsl", "fragment.glsl")
```

Congrats! You have created your first shader using pygame_shaders!

## Using the shader

Now that you have created your shader. Its time to use it. Right now our code looks something like this:
```python
import pygame
import pygame_shaders

screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE)
display = pygame.Surface((600, 600))
display.set_colorkey((0, 0, 0))

shader = pygame_shaders.Shader((600, 600), (600, 600), (0, 0), "vertex.glsl", "fragment.glsl")
```

This is all the setup the shader requires. Now you can continue with your Pygame project as normal. With the exception of a few things. A typical project using pygame_shaders looks like this:

```python
import pygame
import pygame_shaders

pygame.init()

screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE)
display = pygame.Surface((600, 600))
display.set_colorkey((0, 0, 0))

shader = pygame_shaders.Shader((600, 600), (600, 600), (0, 0), "shaders/vertex.txt", "shaders/default_frag.txt")

while True:
    pygame_shaders.clear((100, 100, 100)) #Fill with the color you would like in the background
    display.fill((0, 0, 0)) #Fill with the color you set in the colorkey
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.draw.rect(display, (255, 0, 0), (20, 20, 20, 20)) #Draw a red rectangle to the display at (20, 20)
    
    shader.render(display) #Render the display onto the OpenGL display with the shaders!
    pygame.display.flip()
```

Congratulations! You have created your first shader using pygame_shaders!


