import numpy as np
import pygame
from OpenGL.GL import *
import ctypes

class ScreenRect:
    def __init__(self):
        self.vertices = (
            -1.0,  1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0,
             1.0,  1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0,
            -1.0, -1.0, 0.0,1.0, 0.0, 0.0, 0.0, 0.0,

           -1.0, -1.0, 0.0,1.0, 0.0, 0.0, 0.0, 0.0,
           1.0,  1.0, 0.0,1.0, 0.0, 0.0, 1.0, 1.0,
           1.0, -1.0, 0.0,1.0, 0.0, 0.0, 1.0, 0.0,
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