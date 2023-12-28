import pygame_shaders.texture as texture
import pygame_shaders.screen_rect as screen_rect
import pygame_shaders.shader_utils as shader_utils

import moderngl
import pygame
import typing

DEFAULT_VERTEX_SHADER = """
#version 330 core

layout (location = 0) in vec3 vertexPos;
layout (location = 1) in vec2 vertexTexCoord;

out vec2 fragmentTexCoord;

void main()
{
    fragmentTexCoord = vertexTexCoord;
    gl_Position = vec4(vertexPos, 1.0);
}
"""

DEFAULT_FRAGMENT_SHADER = """
#version 330 core

in vec3 fragmentColor;
in vec2 fragmentTexCoord;

out vec4 color;

uniform sampler2D imageTexture;

void main() {
    color = texture(imageTexture, fragmentTexCoord);
}
"""

class Shader:
    """
    Main shader class responsibe for creating a shader object based on a given vertex and fragment shader. 
    Takes a path to a glsl vertex shader, fragment shader as well as a target surface. This target surface will
    act as the texture to which the shader will be applied.
    """
    
    @staticmethod
    def create_vertfrag_shader(ctx: moderngl.Context, vertex_filepath: str, fragment_filepath: str) -> moderngl.Program:
        """
        Create a moderngl shader program containing the shaders at the given filepaths.
        """
        
        if vertex_filepath != DEFAULT_VERTEX_SHADER:
            with open(vertex_filepath,'r') as f:
                vertex_src = f.read()
        else:
            vertex_src = DEFAULT_VERTEX_SHADER
        if fragment_filepath != DEFAULT_FRAGMENT_SHADER:
            with open(fragment_filepath,'r') as f:
                fragment_src = f.read()
        else:
            fragment_src = DEFAULT_FRAGMENT_SHADER

        shader = ctx.program(vertex_shader=vertex_src, fragment_shader=fragment_src)
        return shader

    def __init__(self, vertex_path: str, fragment_path: str, target_surface: pygame.Surface) -> None:
        self.ctx = moderngl.create_context()
        self.ctx.enable(moderngl.BLEND)
        self.ctx.blend_func = self.ctx.SRC_ALPHA, self.ctx.ONE_MINUS_SRC_ALPHA
        
        self.target_surface = target_surface
        
        self.shader_data = {}
        self.shader = Shader.create_vertfrag_shader(self.ctx, vertex_path, fragment_path)
        self.render_rect = screen_rect.ScreenRect(self.target_surface.get_size(),self.target_surface.get_size(), (0, 0), self.ctx, self.shader)
        
        self.screen_texture = texture.Texture(pygame.Surface(self.target_surface.get_size()), self.ctx)
        self.framebuffer = self.ctx.simple_framebuffer(size=self.target_surface.get_size(), components=4)
        self.scope = self.ctx.scope(self.framebuffer) 

        self.window_size = pygame.display.get_surface().get_size()

    def clear(self, color: typing.Union[pygame.Color, typing.Tuple[int]]) -> None:
        """
        Clears the shader and provided 
        """

        self.target_surface.fill(color)
        self.ctx.clear(color=(color[0]/255, color[1]/255, color[2]/255))

    def send(self, name: str, data: typing.Any) -> None:
        """
        Used to send uniform data to the shader 
        """
        self.shader[name] = data

    def set_target_surface(self, surface: pygame.Surface) -> None:
        """
        Update the current shader texture object with a new pygame Surface object
        """

        # self.screen_texture.texture.release()
        self.target_surface = surface
        # self.screen_texture = texture.Texture(pygame.Surface(self.target_surface.get_size()), self.ctx)

    def set_target_texture(self, texture: texture.Texture) -> None:
        """
        Set the target texture object
        """

        self.screen_texture = texture

    def __upload_uniforms(self) -> None:
        for key in self.shader_data.keys():
            data = self.shader_data[key]
            if len(data) == 1:
                self.shader[key].value = data[0]

            elif len(data) == 2:
                self.shader[key].value = (data[0], data[1])

    def render_direct(self, rect: pygame.Rect, update_surface: bool=True, autoscale: bool=False) -> None:
        """
        Render the shader directly onto the opengl context. Instead of rendering onto the shader 
        onto a surface which we can then perform standard pygame functionality on, we instead render
        straight onto the opengl context.  
        """
        #this rect is in the pygame coordinate system, our goal is to convert it into our custom coordinate systems
        #(0,0);pygame -> (-600, 600) in ours
        if autoscale:
            size = (self.target_surface.get_width(), self.target_surface.get_height())
        else:
            size = self.window_size

        rect = screen_rect.ScreenRect.pygame_rect_to_screen_rect(rect, self.target_surface, size)

        # self.__upload_uniforms()
        self.render_rect = screen_rect.ScreenRect((rect.w, rect.h), size, (rect.x, rect.y), self.ctx, self.shader)

        if update_surface:
            self.screen_texture.update(self.target_surface)

        self.screen_texture.use()
        self.render_rect.vao.render()

    def render(self, update_surface: bool=True) -> pygame.Surface:
        """
        Render the shader onto a pygame Surface making use of the target surface provided.
        """

        # self.upload_uniforms()

        if update_surface:
            self.screen_texture.update(self.target_surface)
        self.screen_texture.use()

        with self.scope:
            self.framebuffer.use()
            self.render_rect.vao.render()
            surf = pygame.image.frombuffer(self.framebuffer.read(), self.target_surface.get_size(), "RGB")
        return pygame.transform.flip(surf, False, True)

class ComputeShader:
    """
    Shader class responsible for handling a GLSL compute shader.
    """

    @staticmethod
    def create_compute_shader(ctx: moderngl.Context, compute_shader_path: str) -> moderngl.ComputeShader:
        """
        Returns a moderngl compute shader object
        """

        with open(compute_shader_path) as f:
            return ctx.compute_shader(f.read())

    def __init__(self, computer_shader_path: str) -> None:
        self.ctx = moderngl.create_context(require=430)
        
        self.path = computer_shader_path
        self.program = ComputeShader.create_compute_shader(self.ctx, self.path)

    def dispatch(self, x: int, y: int, z: int) -> None:
        """
        Run the compute shader with the given dimensions.
        """

        self.program.run(x, y, z)

class DefaultScreenShader(Shader):
    """
    A convinience class used to quickly create a screen shader which can take the contents of a pygame Surface and display it on an OpenGL context display.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(DEFAULT_VERTEX_SHADER, DEFAULT_FRAGMENT_SHADER, screen)
    
    def render(self) -> None:
        """
        Render the display onto the OpenGL context
        """

        super().render_direct(pygame.Rect(0, 0, self.target_surface.get_width(), self.target_surface.get_height()), autoscale=True)
