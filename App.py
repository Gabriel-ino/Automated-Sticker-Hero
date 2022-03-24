from ppadb.client import Client
from PIL import Image
import numpy as np
from time import sleep


class App:
    def __init__(self):
        """
        This class will make all the computer vision processing and send the commands to the mobile device
        """
        self.client = Client()
        self.devices = self.client.devices()
        if len(self.devices) == 0:
            print("No devices found")
            quit()
        self.to_connect_device = self.devices[0]
        print(f"Connected to {self.to_connect_device}")
        self.screenshot = self.to_connect_device.screencap()
        with open("utils/screenshot.png", 'wb') as file:
            file.write(self.screenshot)

    def proccessing(self, h, w, ch):
        self.screenshot = self.to_connect_device.screencap()
        with open("utils/screenshot.png", "wb") as file:
            file.write(self.screenshot)
        img = Image.open("utils/screenshot.png")
        img = np.array(img, dtype=np.uint8)
        print(h, w)
        required_position = int( h / 1.1716)  # It will work on every mobile screen. It will take the specific position
        # on the screen where the black platforms begin

        pixels = [list(i[:3]) for i in img[required_position]]
        transitions = []
        ignore = True
        black = True

        for i, pixel in enumerate(pixels):
            r, g, b = [int(i) for i in pixel]
            if ignore and (r + g + b) != 0:
                continue
            ignore = False
            if black and (r + g + b) != 0:
                black = not black
                transitions.append(i)
                continue
            if not black and (r + g + b) == 0:
                black = not black
                transitions.append(i)
                continue
        start, target1, target2 = transitions
        gap = target1 - start
        target = target2 - target1
        distance = (gap + target / 2)
        print(distance)
        self.to_connect_device.shell(f"input touchscreen swipe 500 500 500 500 {int(distance)}") # Command to mobile device
        sleep(3)
