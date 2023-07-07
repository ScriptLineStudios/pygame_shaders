import numpy as np
import moderngl
import pygame

class ScreenRect:
    @staticmethod 
    def pygame_rect_to_screen_rect(rect: pygame.Rect, target_surface: pygame.Surface) -> pygame.Rect:
        size = pygame.display.get_surface().get_size()
        w = size[0]
        h = size[1]

        return pygame.Rect(((rect.x*2) - w) + rect.w, ((rect.y*2) + h) - rect.h, rect.w, rect.h)        

    def __init__(self, size, win_size, offset, ctx, program):
        self.size = size
        offset = (offset[0]/win_size[0], offset[1]/win_size[1])
        self.current_w, self.current_h = win_size
        
        x = self.size[0] / self.current_w
        y = self.size[1] / self.current_h
        self.vertices = [
            (-x + offset[0],  y + offset[1]),
             (x + offset[0],  y + offset[1]),
            (-x + offset[0], -y + offset[1]),

           (-x + offset[0], -y + offset[1]),
           (x + offset[0],  y + offset[1]),
           (x + offset[0], -y + offset[1]),
        ]
        self.tex_coords = [
           (0.0, 1.0),
           (1.0, 1.0),
           (0.0, 0.0),

           (0.0, 0.0),
           (1.0, 1.0),
           (1.0, 0.0),
        ]

        self.vertices = np.array(self.vertices, dtype=np.float32)
        self.tex_coords = np.array(self.tex_coords, dtype=np.float32)
        self.data = np.hstack([self.vertices, self.tex_coords])

        self.vertex_count = 6

        self.vbo = ctx.buffer(self.data)

        try:
            self.vao = ctx.vertex_array(program, [
                (self.vbo, '2f 2f', 'vertexPos', 'vertexTexCoord'),
            ])
        except moderngl.error.Error:
            self.vbo = ctx.buffer(self.vertices)
            self.vao = ctx.vertex_array(program, [
                (self.vbo, '2f', 'vertexPos'),
            ])

        self.program = program