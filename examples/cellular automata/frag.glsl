#version 330 core

in vec3 fragmentColor;
in vec2 fragmentTexCoord;

out vec4 color;

uniform sampler2D imageTexture;

vec2 res = vec2(100, 100);

float grid(float x, float y)
{
    float tx = x/res.x;
    float ty = y/res.y;
    vec4 t = texture(imageTexture, vec2(tx, ty));
    if (t.y > 0.5) {
        return 1.0;
    } 
    else {
        return 0.0;
    }
}
int birth_limit = 4;

void main() {
    float cx = fragmentTexCoord.x*res.x;
    float cy = (1 - fragmentTexCoord.y)*res.y;

    float alive_cells = 0;

    for (float x = cx - 1; x <= cx + 1; x++) {
        for (float y = cy - 1; y <= cy + 1; y++) {
            if (x >= 0 && x < res.x && y >= 0 && y < res.y) {
                alive_cells += grid(x, y);
            }
            else {
                alive_cells++;
            }
        }
    }
    if (alive_cells > 4) {
        color = vec4(0, 0.8, 0, 1); //alive
    }
    else if (alive_cells < 4) {
        color = vec4(0, 0, 0.5, 1); //dead
    }
}