from App import App
from utils.get_screen_size import get_screen_size


if __name__ == "__main__":
    app = App()
    h, w, ch = get_screen_size()
    while True:
        app.proccessing(h, w, ch)


