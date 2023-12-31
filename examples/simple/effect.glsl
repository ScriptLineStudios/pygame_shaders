#version 330 core

//Provided by the pygame_shaders library. Do not modify...
in vec3 fragmentColor;
in vec2 fragmentTexCoord;
uniform sampler2D imageTexture;

//Color output of the shader
out vec4 color;

//Note: Add your custom uniforms and variables here.

uniform float time;

vec2 res = vec2(1000, 800);

void main() {
    vec2 cPos = (-1.0 + 2.0 * gl_FragCoord.xy / res.xy);
    float cLength = length(cPos);

    vec2 uv = gl_FragCoord.xy/res.xy+(cPos/cLength)*cos(cLength*12.0-time*4.0)*0.003;
    vec3 col = texture2D(imageTexture, uv).xyz;

    gl_FragColor = vec4(col,1.0);
}
