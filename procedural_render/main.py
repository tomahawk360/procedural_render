import glfw

class Window:
    def __init__(self, width, height, title):
        if not glfw.init():
            raise Exception("glfw no puede inicializar")

        self._win = glfw.create_window(width, height, title, None, None)

        if not self._win:
            glfw.terminate()
            raise Exception("glfw window no puede crearse")

        glfw.set_window_pos(self._win, 400, 200)
        glfw.make_context_current(self._win)

    def main_loop(self):
        while not glfw.window_should_close(self._win):
            glfw.poll_events()
            glfw.swap_buffers(self._win)

        glfw.terminate()



if __name__ == "__main__":
    win = Window(1000, 500, "My OpenGL window")
    win.main_loop()