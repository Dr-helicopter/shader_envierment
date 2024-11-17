uniform float Time;
uniform vec2 Resolution;


out vec4 FragColor;




float sdCircle( vec2 p, float r )
{
    return length(p) - r;
}


vec3 palette( in float t){
	vec3 a = vec3(0.378, -0.052, 0.848);
	vec3 b = vec3(0.500, 1.018, 1.148);
	vec3 c = vec3(1.398, 0.928, 1.018);
	vec3 d = vec3(0.888, 1.098, 0.333);

    return a + b*cos( 6.283185*(c*t+d) );
}

void main() {
	vec2 uv = gl_FragCoord.xy / Resolution; 
	uv.x *= Resolution.x / Resolution.y;
	vec3 finalCol;

	vec2 uv2 = uv * 2;
	for (int i = 1; i <= 3; i++){
		uv2 = fract(uv2 * 1.5);
		uv2 -= 0.5;


		float d = sdCircle(uv2, 0.5 - i/8) * exp(-length(uv * 2 - 1));

		vec3 col = palette(length(uv * 2 - 1) + Time * 0.5 - i * 2);
		

		d = sin(d*8.0 + Time * 0.75);
		d = abs(d);
		d = 0.02/d;
		d = smoothstep(0.0 ,0.4, d);

		col *= d;
		finalCol += col;
	}
 	FragColor = vec4(finalCol, 1.0);
}
