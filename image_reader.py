import numpy as np
import pyautogui
from PIL import Image
import pytesseract
import cv2
import os

def get_text_from_image(filename, blur=False, thresh=False):
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if blur:
        gray = cv2.medianBlur(gray, 3)
    elif thresh:
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    return text

def take_screen_shot():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("in_memory_to_disk.png", image)


if __name__=='__main__':
    # print(get_text_from_image("example_02.png"))
    take_screen_shot()
