from pynput.mouse import Button, Controller
import pyautogui
import time

AMELIORATION_CONSECUTIVE = None
AMELIORATION_CONSECUTIVE_5 = None
AMELIORATION_CONSECUTIVE_BUTTON = None
AMELIORER = None
MAX_EVEIL_BUTTON = None
CLOSE_BUTTON, CLOSE_PANNEL_BUTTON, EVEIL_BUTTON, EVEIL_BUTTON_C = None, None, None, None

mouse = Controller()


# print("Current position: " + str(mouse.position))

# mouse.position = (500,500)

def get__middle_of_image_couple(image):
    return image.left + image.width / 2, image.top + image.height / 2


def mouse_move_click_then_reset_position(position, click_type= Button.left, nb_click= 1, reset_position = True):
    mouse.position = position
    mouse.click(click_type, nb_click)
    if reset_position:
        mouse.position = (0, 0)


def init_amelioration_consecutive_5():
    global AMELIORATION_CONSECUTIVE_5
    confiance = 1
    while AMELIORATION_CONSECUTIVE_5 is None and confiance >= 0.5:
        AMELIORATION_CONSECUTIVE_5 = pyautogui.locateOnScreen('images/amelioration_consecutive_5.png',
                                                              confidence=confiance)
        confiance -= 0.1
    print('Impossible de charger le bouton %s', AMELIORATION_CONSECUTIVE_5)


def init_ameliorer():
    global AMELIORER
    confiance = 1
    while AMELIORER is None and confiance >= 0.5:
        AMELIORER = pyautogui.locateOnScreen('images/ameliorer.png',
                                             confidence=confiance)
        confiance -= 0.1
    print('Impossible de charger le bouton %s', AMELIORER)


def init_amelioration_consecutive_button():
    global AMELIORATION_CONSECUTIVE_BUTTON
    confiance = 1
    while AMELIORATION_CONSECUTIVE_BUTTON is None and confiance >= 0.5:
        AMELIORATION_CONSECUTIVE_BUTTON = pyautogui.locateOnScreen('images/amelioration_consecutive_button.png',
                                             confidence=confiance)
        confiance -= 0.1
    print('Impossible de charger le bouton %s', AMELIORATION_CONSECUTIVE_BUTTON)

def init_amelioration_consecutive():
    global AMELIORATION_CONSECUTIVE
    confiance = 1
    while AMELIORATION_CONSECUTIVE is None and confiance >= 0.5:
        AMELIORATION_CONSECUTIVE = pyautogui.locateOnScreen('images/amelioration_consecutive.png',
                                             confidence=confiance)
        confiance -= 0.1
    print('Impossible de charger le bouton %s', AMELIORATION_CONSECUTIVE)

def init_eveil_button():
    global EVEIL_BUTTON
    confiance = 1
    while EVEIL_BUTTON is None and confiance >= 0.5:
        EVEIL_BUTTON = pyautogui.locateOnScreen('images/eveiller_button.png',
                                                            confidence=confiance)
        confiance -= 0.1
    print('Impossible de charger le bouton %s', EVEIL_BUTTON)

def init_eveil_button_c():
    global EVEIL_BUTTON_C
    confiance = 1
    while EVEIL_BUTTON_C is None and confiance >= 0.5:
        EVEIL_BUTTON_C = pyautogui.locateOnScreen('images/eveiller_button_cost_C.png',
                                                            confidence=confiance)
        confiance -= 0.1
    print('Impossible de charger le bouton %s', EVEIL_BUTTON_C)

def init_close_button_panel():
    global CLOSE_PANNEL_BUTTON
    confiance = 1
    while CLOSE_PANNEL_BUTTON is None and confiance >= 0.5:
        CLOSE_PANNEL_BUTTON = pyautogui.locateOnScreen('images/close_pannel_button.png',
                                                            confidence=confiance)
        confiance -= 0.1
    print('Impossible de charger le bouton %s', CLOSE_PANNEL_BUTTON)


def init_close_button():
    global CLOSE_BUTTON
    confiance = 1
    while CLOSE_BUTTON is None and confiance >= 0.5:
        CLOSE_BUTTON = pyautogui.locateOnScreen('images/close_button.png',
                                                       confidence=confiance)
        confiance -= 0.1

    if CLOSE_BUTTON is None:
        print('Impossible de charger le bouton %s', CLOSE_BUTTON)

def init_max_eveil_button():
    global MAX_EVEIL_BUTTON
    confiance = 1
    while MAX_EVEIL_BUTTON is None and confiance >= 0.5:
        MAX_EVEIL_BUTTON = pyautogui.locateOnScreen('images/chance_succes_10.png',
                                                       confidence=confiance)
        confiance -= 0.1

    if CLOSE_BUTTON is None:
        print('Impossible de charger le bouton %s', MAX_EVEIL_BUTTON)

def attend_amelioration_max():
    while pyautogui.locateOnScreen('images/amelioration_max_atteinte.png') is None:
        time.sleep(0.2)



if __name__ == '__main__':
    while MAX_EVEIL_BUTTON is None:
        if AMELIORER is None:
            init_ameliorer()
        mouse_move_click_then_reset_position(get__middle_of_image_couple(AMELIORER))
        time.sleep(1.5)

        if AMELIORATION_CONSECUTIVE is None:
            init_amelioration_consecutive()
        mouse_move_click_then_reset_position(get__middle_of_image_couple(AMELIORATION_CONSECUTIVE))
        time.sleep(1.5)

        if AMELIORATION_CONSECUTIVE_5 is None:
            init_amelioration_consecutive_5()
        mouse_move_click_then_reset_position(get__middle_of_image_couple(AMELIORATION_CONSECUTIVE_5))
        time.sleep(1.5)

        if AMELIORATION_CONSECUTIVE_BUTTON is None:
            init_amelioration_consecutive_button()
        mouse_move_click_then_reset_position(get__middle_of_image_couple(AMELIORATION_CONSECUTIVE_BUTTON))
        time.sleep(1.5)

        attend_amelioration_max()

        if CLOSE_BUTTON is None:
            init_close_button()
        mouse_move_click_then_reset_position(get__middle_of_image_couple(CLOSE_BUTTON))
        time.sleep(1.5)

        if EVEIL_BUTTON is None:
            init_eveil_button()
        mouse_move_click_then_reset_position(get__middle_of_image_couple(EVEIL_BUTTON))
        time.sleep(1.5)

        if EVEIL_BUTTON_C is None:
            init_eveil_button_c()
        mouse_move_click_then_reset_position(get__middle_of_image_couple(EVEIL_BUTTON_C))
        time.sleep(5)

        if CLOSE_PANNEL_BUTTON is None:
            init_close_button_panel()
        mouse_move_click_then_reset_position(get__middle_of_image_couple(CLOSE_PANNEL_BUTTON))
        time.sleep(1.5)




