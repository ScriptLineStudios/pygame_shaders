import pygame
import pygame_shaders

pygame.init()

display = pygame.display.set_mode((1000, 800), pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()

display = pygame.Surface((1000, 800))
shader = pygame_shaders.Shader(pygame_shaders.DEFAULT_VERTEX_SHADER, "effect.glsl", display)

image = pygame.image.load("../../docs/assets/pfp.png")

font = pygame.font.SysFont("Arial", 32)

time = 0
while True:
    time += 1
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

    text = font.render("Hello World! - This font is being modified by a shader", False, "white")
    display.blit(text, (40 + time, 600))

    display.blit(image, (100, 100))

    shader.send("time", time)

    shader.render_direct(pygame.Rect(0, 0, 1000, 800))
    pygame.display.flip()
    clock.tick()