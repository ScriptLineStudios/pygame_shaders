import OpenGL
OpenGL.USE_ACCELERATE = True
from OpenGL.GL import *
import texture
import screen_rect
import shader_utils

def clear():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

class Shader:
    def __init__(self, vertex_path, fragment_path):
        self.render_rect = screen_rect.ScreenRect()

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        self.shader_data = {}
        self.shader = shader_utils.create_shader(vertex_path, fragment_path)
        

    def send(self, name, data):
        if name in self.shader_data:
            if [float(x) for x in data] == self.shader_data[name]:
                return
        self.shader_data[name] = [float(x) for x in data]

    def render(self, surface=None):
        if surface is not None:
            screen_texture = texture.Texture(surface)
            screen_texture.use()

        glUseProgram(self.shader)
        for key in self.shader_data.keys():
            data = self.shader_data[key]
            loc = glGetUniformLocation(self.shader, key)
            if len(data) == 1:
                glUniform1f(loc, data[0]) 
            elif len(data) == 2:
                glUniform2f(loc, data[0], data[1])

        glBindVertexArray(self.render_rect.vao)
        glDrawArrays(GL_TRIANGLES, 0, self.render_rect.vertex_count)