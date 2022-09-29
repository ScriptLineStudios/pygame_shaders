from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram,compileShader

def create_shader(vertex_filepath, fragment_filepath, ctx):
    with open(vertex_filepath,'r') as f:
        vertex_src = f.read()

    with open(fragment_filepath,'r') as f:
        fragment_src = f.read()
    
    shader = ctx.program(vertex_shader=vertex_src, fragment_shader=fragment_src)
    
    return shader