import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
import glfw


def compile_shader(shader_code, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, shader_code)
    glCompileShader(shader)
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(shader).decode()
        raise RuntimeError(f"Shader compilation failed: {error}")
    return shader


def create_shader_program(vertex_shader_code, fragment_shader_code):
    vertex_shader = compile_shader(vertex_shader_code, GL_VERTEX_SHADER)
    fragment_shader = compile_shader(fragment_shader_code, GL_FRAGMENT_SHADER)
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)
    if not glGetProgramiv(program, GL_LINK_STATUS):
        error = glGetProgramInfoLog(program).decode()
        raise RuntimeError(f"Shader linking failed: {error}")
    return program


def display_shader(shader_path, x=800 , y=800):
    with open(shader_path, 'r') as file:
        shader_code = file.read()

    vertex_shader_code = """
    #version 330 core
    layout(location = 0) in vec3 position;
    out vec2 uv;
    void main() {
        uv = (position.xy + vec2(1.0, 1.0)) * 0.5;
        gl_Position = vec4(position, 1.0);
    }
    """
    try:
        glfw.init()
        glfw.window_hint(glfw.RESIZABLE, glfw.FALSE)
        window = glfw.create_window(x, y, "Shader Display", None, None)
        glfw.make_context_current(window)

        program = create_shader_program(vertex_shader_code, shader_code)
        glUseProgram(program)

        # Full-screen quad (two triangles)
        vertices = [
            -1.0, -1.0, 0.0,  # Bottom-left
             1.0, -1.0, 0.0,  # Bottom-right
            -1.0,  1.0, 0.0,  # Top-left
            -1.0,  1.0, 0.0,  # Top-left
             1.0, -1.0, 0.0,  # Bottom-right
             1.0,  1.0, 0.0   # Top-right
        ]
        vertices = (GLfloat * len(vertices))(*vertices)

        vao = glGenVertexArrays(1)
        vbo = glGenBuffers(1)

        glBindVertexArray(vao)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(0)

        time_location = glGetUniformLocation(program, "Time")
        resolution_location = glGetUniformLocation(program, "Resolution")
        # Inside your render loop
        glUniform2f(resolution_location, float(x), float(y))



        while not glfw.window_should_close(window):
            current_time = glfw.get_time()  # Time in seconds
            glUniform1f(time_location, current_time)


            glClear(GL_COLOR_BUFFER_BIT)
            glDrawArrays(GL_TRIANGLES, 0, 6)  # Draw 6 vertices (two triangles)
            glfw.swap_buffers(window)
            glfw.poll_events()

        glfw.terminate()

    except Exception as e:
        print(e)
        glfw.terminate()


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 2:
        display_shader(sys.argv[1])
    elif len(sys.argv) == 4:
        print(f'window size {int(sys.argv[2])}x{int(sys.argv[3])}')
        display_shader(sys.argv[1], x=int(sys.argv[2]), y=int(sys.argv[3]))
    else:
        print('invalid args')
