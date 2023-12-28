#version 330

//Provided by the pygame_shaders library. Do not modify...
in vec3 fragmentColor;
in vec2 fragmentTexCoord;
uniform sampler2D imageTexture;

//Color output of the shader
out vec4 color;

//Note: Add your custom uniforms and variables here.

void main() {
    color = texture(imageTexture, fragmentTexCoord) * 0.5 - fragmentTexCoord.x / 2;
}
