import pygame_shaders.texture as texture
import pygame_shaders.screen_rect as screen_rect
import pygame_shaders.shader_utils as shader_utils

import moderngl
import pygame

ctx = None

def clear(color):
    ctx.clear(color=(color[0]/255, color[1]/255, color[2]/255))

class Shader:
    def __init__(self, size, display, pos, vertex_path, fragment_path, target_texture=None):
        global ctx
        if ctx is None:
            ctx = moderngl.create_context()

        self.ctx = ctx
        ctx.enable(moderngl.BLEND)
        ctx.blend_func = ctx.SRC_ALPHA, ctx.ONE_MINUS_SRC_ALPHA
        
        self.shader_data = {}
        self.shader = shader_utils.create_shader(vertex_path, fragment_path, self.ctx)
        self.render_rect = screen_rect.ScreenRect(size, display, pos, self.ctx, self.shader)

        if target_texture is not None:
            s = pygame.Surface(target_texture.get_size())
            self.screen_texture = texture.Texture(s, self.ctx)
        
    def send(self, name, data):
        if name in self.shader_data:
            if [float(x) for x in data] == self.shader_data[name]:
                return
        self.shader_data[name] = [float(x) for x in data]

    def render(self, surface=None):
        if surface is not None:
            self.screen_texture.update(surface)
            self.screen_texture.use()

        for key in self.shader_data.keys():
            data = self.shader_data[key]
            if len(data) == 1:
                self.shader[key].value = data[0]

            elif len(data) == 2:
                self.shader[key].value = (data[0], data[1])

        self.render_rect.vao.render()
