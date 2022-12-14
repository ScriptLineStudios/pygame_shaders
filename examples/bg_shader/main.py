import pygame
import pygame_shaders

pygame.init()

screen = pygame.display.set_mode((600, 600), pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF)
display = pygame.Surface((100, 100))
display.set_colorkey((0,0,0))
clock = pygame.time.Clock()

bg_shader = pygame_shaders.Shader((400, 400), (600, 600), (0, 0), "shaders/vertex.txt", "shaders/fragment.txt", display)
screen_shader = pygame_shaders.Shader((600, 600), (600, 600), (0, 0), "shaders/default_vertex.txt", "shaders/default_frag.txt", display)

running = True
dt = 1.0

x, y = 10, 10


while running:
    pygame_shaders.clear((100, 100, 100))
    display.fill((0, 0, 0))
    dt += .01
    pygame.display.set_caption(f"{clock.get_fps()}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False


    x += pygame.key.get_pressed()[pygame.K_d]
    x -= pygame.key.get_pressed()[pygame.K_a]

    pygame.draw.rect(display, (0, 0, 255), (x, y, 10, 10))

    bg_shader.send("time", [dt])
    bg_shader.send("resolution", [500.0, 500.0])
    bg_shader.send("alpha", [1])

    bg_shader.render(display)
    screen_shader.render(display)

    pygame.display.flip()
    clock.tick(60)
