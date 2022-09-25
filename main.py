import pygame
import pygame_shaders

pygame.init()

screen = pygame.display.set_mode((600, 600), pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF)
display = pygame.Surface((100, 100))
display.set_colorkey((0,0,0))
clock = pygame.time.Clock()

bg_shader = pygame_shaders.Shader("shaders/vertex.txt", "shaders/fragment.txt")
screen_shader = pygame_shaders.Shader("shaders/vertex.txt", "shaders/default_frag.txt")

image = pygame.image.load("grass_0.png")
image.set_colorkey((0,0,0))

running = True
dt = 1.0

while running:
    pygame_shaders.clear()
    dt += .01
    pygame.display.set_caption(f"{clock.get_fps()}")
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    display.blit(image, (10, 10))

    bg_shader.send("time", [dt])
    bg_shader.send("resolution", [500.0, 500.0])
    bg_shader.send("alpha", [1])

    bg_shader.render()
    screen_shader.render(display)

    pygame.display.flip()
    clock.tick(60)