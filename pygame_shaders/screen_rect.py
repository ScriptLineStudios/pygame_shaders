import numpy as np
from OpenGL.GL import *
import ctypes

class ScreenRect:
    def __init__(self, size, win_size, offset):
        self.size = size
        offset = (offset[0]/win_size[0], offset[1]/win_size[1])

        self.current_w, self.current_h = win_size
        
        x = self.size[0] / self.current_w
        y = self.size[1] / self.current_h

        self.vertices = (
            -x + offset[0],  y + offset[1],    0.0, 1.0, 0.0, 0.0,    0.0, 1.0,
             x + offset[0],  y + offset[1],    0.0, 1.0, 0.0, 0.0,    1.0, 1.0,
            -x + offset[0], -y + offset[1],    0.0,1.0, 0.0, 0.0,     0.0, 0.0,

           -x + offset[0], -y + offset[1],     0.0,1.0, 0.0, 0.0,      0.0, 0.0,
           x + offset[0],  y + offset[1],      0.0,1.0, 0.0, 0.0,       1.0, 1.0,
           x + offset[0], -y + offset[1],      0.0,1.0, 0.0, 0.0,       1.0, 0.0,
        )

        self.vertices = np.array(self.vertices, dtype=np.float32)

        self.vertex_count = 6

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))
        
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(24))