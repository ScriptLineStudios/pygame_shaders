Compute Shaders
=================

Compute shaders are great for arbitray calculations which can benifit from being computed on the GPU in parallel. pygame_shaders provides an easy API to spin up your first compute shader in no time.

Lets start in a new python file:

.. code-block:: python

    import pygame
    import pygame_shaders

    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF)

    display = pygame.Surface((600, 600))

    screen_shader = pygame_shaders.DefaultScreenShader(display)
    compute_shader = pygame_shaders.ComputeShader("compute.glsl")

    surf = pygame.Surface((600, 600))

    texture = pygame_shaders.Texture(surf, compute_shader.ctx)
    dt = 0
    while True:
        display.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        texture.bind(0)    
        compute_shader.dispatch(600, 600, 1)

        display.blit(texture.as_surface(), (0, 0))

        screen_shader.render()
        
        pygame.display.flip()

        clock.tick()


We start with the usual pygame/pygame_shaders setup. Create an OpenGL pygame display, a surface to render onto, and screen shader to display it. We then create a 2 things, a ComputeShader and a Texture. The ComputeShader object will be responsible for dispatching our compute shader when the time is right, 
and the texture will be used to hold the result of the compute shader. Speaking of the compute shader, here it is:

.. code-block:: glsl

    #version 460 core
    layout(local_size_x = 8, local_size_y = 4, local_size_z = 1) in;
    layout(rgba32f, binding = 0) uniform image2D screen;
    void main()
    {
        vec4 pixel = vec4(1.0, 0.0, 0.0, 1.0);
        ivec2 pixel_coords = ivec2(gl_GlobalInvocationID.xy);

        imageStore(screen, pixel_coords, pixel);
    }

Essetially what this shader is doing, is receiving an image which is bound to the GPU via slot 0. We are then calculating 
the current pixel based on the coordinates of the current global invocation. And we are setting the color of that pixel to a brigh red. Not the most interseting usage for a compute shader, but good enough for a simple use case example.

Back in the python code, in our game loop we first bind our texture to the same binding slot we specified in the compute shader (0 in this case) we then dispatch our compute shader with the dimensions, 600, 600, 1 these are the same dimensions as 
the surface which we are using for our Texture. Once we have dispatched and the compute shader has run, we can take our texture, convert it to a pygame Surface and blit it onto our display. This gives the desired result!