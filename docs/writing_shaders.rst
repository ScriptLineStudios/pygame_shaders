Writing Shaders
=================

pygame_shaders provides support for the integartion of GLSL vertex, fragment and compute shaders into pygame projects. Typically GLSL shaders will end in the extenison ``.glsl`` In the case of pygame_shaders, the typical starting point of your shaders will look like this:

vertex.glsl:

.. code-block:: glsl

    #version 330 core //version 

    /* 
    pygame_shaders provides a vec3 which repesents the current vertex positon and a vec2 
    representing the current texture coordinate on layout location 0 and 1 respectively.
    */
    layout (location = 0) in vec3 vertexPos;
    layout (location = 1) in vec2 vertexTexCoord;

    // the vertex shader outputs a fragment texture coordinate.
    out vec2 fragmentTexCoord;

    //add your own variables here.

    void main()
    {
        fragmentTexCoord = vertexTexCoord; //set the fragment tex coord to the texture coordinate
        gl_Position = vec4(vertexPos, 1.0); //position the vertex at the vertex position.
    } 

fragment.glsl:

.. code-block:: glsl

    #version 330 core //version

    in vec3 fragmentColor; // The color of the current coordinate/
    in vec2 fragmentTexCoord; // The texture coordinate which we will use in the sampler2D lookup.

    out vec4 color; // The color we are outputting.

    uniform sampler2D imageTexture; // The texture which the shader is provided.

    void main() {
        color = texture(imageTexture, fragmentTexCoord); //Peform the above desribed lookup and output it to the color.
    }

While the names of library provided variables are up to you to decide. pygame_shaders provides a DEFAULT_VERTEX_SHADER and DEFAULT_FRAGMENT_SHADER, if one of these default shaders is in use, you will have to adhere to the above naming. 

A default compute shader is slightly more flexible:

compute.glsl:

.. code-block:: glsl

    #version 460 core //compute shaders always need version 46o over above
    layout(local_size_x = 8, local_size_y = 4, local_size_z = 1) in; // The number of threads you want to invoke. (Can be changed to suit the needs of your computations)
    
    layout(rgba32f, binding = 0) uniform image2D screen; // Typically a compute shader will take in an image via a binding as input (once again, not required can be modified based on your needs)
    
    void main() {
        // Whatever you like :D
    }