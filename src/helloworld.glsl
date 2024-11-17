uniform float Time;
uniform vec2 Resolution;

out vec4 FragColor;

void main() {
    vec2 uv = gl_FragCoord.xy / Resolution; 
	uv.x *= Resolution.x / Resolution.y;
    
	
    FragColor = vec4(uv.xy,0, 1.0);
}
