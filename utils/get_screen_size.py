import cv2


def get_screen_size():
    """
    This function will take the image's parameters based on first screenshot in init function of the App's class
    :return: Screen's height, screen's width, screen's channels
    """
    screenshot = cv2.imread("/home/bagriel/PycharmProjects/stick_hero_automation/utils/screenshot.png")
    print(screenshot)
    h, w, ch = screenshot.shape
    return h, w, ch

