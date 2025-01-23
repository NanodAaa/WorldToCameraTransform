# W2CTransform.py

import gui
import tkinter as tk

FITTING_FUNC_COEFS = (-1.876641E-10, 
                        -7.446742E-09,
                        -2.181705E-06,
                        -3.051775E-06,
                        1.049506E-01,
                        -8.559749E-06 ) # Fitting function coefficients X^6 (x6 -> x1)

SENSOR_RESOLUTIONS = (1920, 1080)
PIXEL_SIZE = 3.00E-03 # (mm)
WORLD_CORDINATES = ()

if __name__ == '__main__':
    mygui = gui.myGUI('root')
    mygui.start()
    
    exit()