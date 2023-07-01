import pygame_shaders

def create_shader(vertex_filepath, fragment_filepath, ctx):
    if vertex_filepath != pygame_shaders.DEFAULT_VERTEX_SHADER:
        with open(vertex_filepath,'r') as f:
            vertex_src = f.read()
    else:
        vertex_src = pygame_shaders.DEFAULT_VERTEX_SHADER
    if fragment_filepath != pygame_shaders.DEFAULT_FRAGMENT_SHADER:
        with open(fragment_filepath,'r') as f:
            fragment_src = f.read()
    else:
        fragment_src = pygame_shaders.DEFAULT_FRAGMENT_SHADER

    shader = ctx.program(vertex_shader=vertex_src, fragment_shader=fragment_src)
    return shader