#version 330 core

in vec2 fragmentTexCoord;
uniform float time;
uniform sampler2D imageTexture;

struct Material {
    vec3 color;
    vec3 emission_color;
};

struct HitInfo {
    bool did_hit;
    vec3 hit;
    float distance;
    vec3 normal;
    Material material;
};

HitInfo hit_sphere(vec3 center, float radius, Material mat, vec3 origin, vec3 dir) {
    vec3 pos = origin - center;
    float a = dot(dir, dir);
    float b = 2.0 * dot(pos, dir);
    float c = dot(pos, pos) - radius * radius;
    float disc = b * b - 4 * a * c;
    
    HitInfo info;
    info.did_hit = disc > 0;
    info.hit = origin + dir * ((-b - sqrt(disc)) / (2.0 * a));
    info.normal = normalize(info.hit - center);
    info.distance = ((-b - sqrt(disc)) / (2.0 * a));
    info.material = mat;

    return info;
}

struct Sphere {
    vec3 pos;
    float radius;
    Material material;
};

HitInfo hit_spheres(Sphere spheres[3], vec3 origin, vec3 dir) {
    HitInfo closest;
    closest.distance = 1000000000;

    for (int i = 0; i < 3; i++) {
        Sphere sphere = spheres[i];
        HitInfo info = hit_sphere(sphere.pos, sphere.radius, sphere.material, origin, dir);
        
        if (info.did_hit && info.distance < closest.distance) {
            closest = info;
        }
    }

    return closest;
}

float random(inout vec2 st) {
    st += vec2(1, 1);
    return fract(sin(dot(st.xy,vec2(12.9898,78.233)))*43758.5453123);
}

vec3 random_point_in_sphere(inout vec2 seed) {
    for (;;) {
        float x = random(seed) * 2 - 1;
        float y = random(seed) * 2 - 1;
        float z = random(seed) * 2 - 1;

        vec3 cube = vec3(x, y, z);
        
        if (dot(cube, cube) <= 1) {
            return cube;
        }
    }
    return vec3(0, 0, 0);
}

vec3 random_direction_in_hemisphere(vec3 normal, inout vec2 seed) {
    vec3 dir = random_point_in_sphere(seed);
    return dir * sign(dot(normal, dir));
}

vec3 Trace(Sphere spheres[3], vec3 origin, vec3 dir, inout vec2 seed, int depth) {
    vec3 light = vec3(0, 0, 0);
    vec3 color = vec3(1, 1, 1);

    for (int i = 0; i < 4; i++) {
        HitInfo hit = hit_spheres(spheres, origin, dir);

        if (hit.did_hit) {
            origin = hit.hit + hit.normal * 0.6;
            dir = normalize(hit.normal + random_point_in_sphere(seed));

            light += hit.material.emission_color * color;
            color *= hit.material.color;               
        }
        else {
            break;
        }
    }

    return light;
}

void main() {
    vec2 seed = fragmentTexCoord;
    
    Sphere spheres[3] = Sphere[3](
        Sphere(vec3(0.0, 0.0, -1), 0.3, Material(vec3(1.0, 0.0, 0.0), vec3(0.0, 0.0, 0.0))),
        Sphere(vec3(0.0, 0.5, -0.6), 0.1, Material(vec3(0.0, 0.0, 0.0), vec3(1.0, 1.0, 1.0))),
        Sphere(vec3(0.0, -4.0, -1), 3.6, Material(vec3(0.62, 0.12, 0.91), vec3(0.0, 0.0, 0.0)))
    );

    vec3 origin = vec3(0.0, 0.0, 0.0);
    vec3 dir = vec3((fragmentTexCoord.x * 2 - 1) * 600/600, (fragmentTexCoord.y * 2 - 1), -1);

    vec3 avg = vec3(0, 0, 0);
    for (int i = 0; i < 2; i++) {
        seed += vec2(i, i);
        avg += Trace(spheres, origin, dir, seed, 2).xyz;
    }
    vec3 pixel = avg / 2;
    vec3 prev = texture(imageTexture, fragmentTexCoord).xyz;
    gl_FragColor = vec4(mix(pixel, prev, 0.5), 1.0);
}