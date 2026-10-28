init python:
    renpy.register_shader("rgb_jitter",
        variables="""
            uniform float u_intensity;
            uniform sampler2D tex0;
            varying vec2 v_tex_coord;
        """, vertex_300="""
            v_tex_coord = a_tex_coord;
            gl_Position = u_transform * a_position;
        """, fragment_300="""
            // Calculate base offset
            float offset = u_intensity * 0.02;

            // Create a pseudo-random twist based on texture coordinates
            float twist = sin(v_tex_coord.x * 12.5663 + v_tex_coord.y * 8.3775) * 0.5 + 0.5;
            float angle = twist * 6.28318 * u_intensity; // Full rotation at max intensity

            // Calculate directional offsets with rotation
            float cosA = cos(angle);
            float sinA = sin(angle);

            // Red channel - twisted left/up
            vec2 r_offset = vec2(-offset * cosA, -offset * sinA);
            // Blue channel - twisted right/down  
            vec2 b_offset = vec2(offset * cosA, offset * sinA);

            // Add slight perpendicular offset for more chaos
            float perpOffset = offset * 0.3;
            r_offset += vec2(-sinA * perpOffset, cosA * perpOffset);
            b_offset += vec2(sinA * perpOffset, -cosA * perpOffset);

            // Sample each color channel
            float r = texture2D(tex0, v_tex_coord + r_offset).r;
            float g = texture2D(tex0, v_tex_coord).g;
            float b = texture2D(tex0, v_tex_coord + b_offset).b;
            float a = texture2D(tex0, v_tex_coord).a;

            gl_FragColor = vec4(r, g, b, a);
        """)