#version 330 core
uniform sampler2D image;

out vec4 color;
in vec2 fragmentTexCoord;

void main() {
    vec2 center = vec2(0.5, 0.5);
    vec2 off_center = fragmentTexCoord - center;

    off_center *= 1.0 + 8.8 * pow(abs(off_center.yx), vec2(5.5));

    vec2 v_text2 = center+off_center;

    if (v_text2.x > 1.0 || v_text2.x < 0.0 || v_text2.y > 1.0 || v_text2.y < 0.0)
        color = vec4(0.0, 0.0, 0.0, 1.0);
    else 
        color = vec4(texture(image, v_text2).rgb, 1.0);
}