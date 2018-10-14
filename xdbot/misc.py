import os
import pyautogui as auto
from .constants import Constants

def module_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_resource(file):
    
    respath = os.path.join("res", Params.LANG)

    if os.path.isdir(os.path.join(module_path(), respath)):
        return os.path.join(module_path(), respath, file)
    else:
        return os.path.join(respath, file)


def locate_on_screen(image, minSearchTime=1):
    if not os.path.isfile(image):
        image = get_resource(image)
    print("LOCATING: %s" % image)
    res = auto.locateCenterOnScreen(image, minSearchTime=minSearchTime)
    print("Found: " + str(res))
    return res
