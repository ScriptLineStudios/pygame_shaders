#version 330 core

in vec3 fragmentColor;
in vec2 fragmentTexCoord;
uniform sampler2D imageTexture;

vec2 res = vec2(50, 50);

void main() {
    vec3 col = texture2D(imageTexture, fragmentTexCoord).xyz;
    
    if (col.x > 0) {
        vec3 neighbour = texture(imageTexture, vec2(fragmentTexCoord.x + 0.1, fragmentTexCoord.y + 0.1));
        gl_FragColor = vec4((col + neighbour) / 2, 1.0);
    }
    else {
        gl_FragColor = vec4(col,1.0);
    }
}
