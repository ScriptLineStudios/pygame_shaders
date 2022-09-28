import pygame
import pygame_shaders

pygame.init()

screen = pygame.display.set_mode(
    (600, 600), pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF
)
display = pygame.Surface((100, 100))
display.set_colorkey((0, 0, 0))
clock = pygame.time.Clock()

bg_shader = pygame_shaders.Shader(
    (400, 400), (600, 600), (0, 0), "shaders/vertex.txt", "shaders/fragment.txt"
)
screen_shader = pygame_shaders.Shader(
    (600, 600), (600, 600), (0, 0), "shaders/vertex.txt", "shaders/default_frag.txt"
)

running = True
dt = 1.0

x, y = 10, 10
pygame.display.set_caption(f"Shaders!")

img = pygame.image.load("assets/water.png").convert_alpha()


while running:
    pygame_shaders.clear((0, 0, 0))
    display.fill((0, 0, 0))
    pygame.display.set_caption(f"{clock.get_fps()}")

    dt += 0.01

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    if clock.get_fps() < 30 and dt > 10:
        break

    x += pygame.key.get_pressed()[pygame.K_d] * 1
    x -= pygame.key.get_pressed()[pygame.K_a] * 1

    bg_shader.send("tx", [dt])
    bg_shader.send("ty", [dt])


    bg_shader.render(img)
    screen_shader.render(display)

    pygame.display.flip()
    clock.tick(60)
