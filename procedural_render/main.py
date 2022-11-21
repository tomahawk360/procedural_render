from xml.dom.expatbuilder import theDOMImplementation
import numpy as np
from glumpy import app, gloo, gl, glm

vertex = open("./shaders/vertex_shader.glsl", "r").read()
fragment = open("./shaders/fragment_shader.glsl", "r").read()

window = app.Window(width=900, height=900)

@window.event
def on_draw(dt):
    global phi, theta
    window.clear()

    cube.draw(gl.GL_TRIANGLES, I)

    theta += 1.0
    phi += -1.0
    model = np.eye(4, dtype=np.float32)
    glm.rotate(model, theta, 0, 0, 1)
    glm.rotate(model, phi, 0, 1, 0)
    cube["model"] = model

@window.event
def on_resize(width, height):
    cube["projection"] = glm.perspective(45.0, width/float(height), 2.0, 100.0)

@window.event
def on_init():
    gl.glEnable(gl.GL_DEPTH_TEST)

V = np.zeros(8, [("position", np.float32, 3), ("color", np.float32, 4)])
V["position"] = [[1,1,1], [-1,1,1], [-1,-1,1], [1,-1,1], [1,-1,-1], [1,1,-1], [-1,1,-1], [-1,-1,-1]]
V["color"] = [[0,1,1,1], [0,0,1,1], [0,0,0,1], [0,1,0,1], [1,1,0,1], [1,1,1,1], [1,0,1,1], [1,0,0,1]]

I = np.array([0,1,2, 0,2,3, 0,3,4, 0,4,5, 0,5,6, 0,6,1, 1,6,7, 1,7,2, 7,4,3, 7,3,2, 4,7,6, 4,6,5], dtype=np.uint32)

V = V.view(gloo.VertexBuffer)
I = I.view(gloo.IndexBuffer)

cube = gloo.Program(vertex, fragment)
cube.bind(V)

cube["model"] = np.eye(4, dtype=np.float32)
cube["view"] = glm.translation(0, 0, -5)
phi, theta = 40, 30

view = np.eye(4, dtype=np.float32)


if __name__ == '__main__':
    app.run(framerate = 60, framecount = 360)
