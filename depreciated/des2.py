""" interactive screen showing graphical data to user.

    Returns:
        Data Explorer Screens layout shared between multiple interfaces -PySimpleGUI 
"""

import PySimpleGUI as sg
import view.login as login
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import view.des1 as des1
import view.des3 as des3
import view.build as build
matplotlib.use('TkAgg')

# ------------------------------- DATA EXPLORER SCREEN TWO START -------------------------------

def DataExplorerScreen():
    """interactive screen showing graphical data to user. Includes navigation and chatsystem

    Returns:
        Data Explorer Screens layout shared between multiple interfaces -PySimpleGUI 
    """
    # ---- MATPLOTLIB CODE HERE -----
    # ---- END OF MATPLOTLIB CODE ----
    # build.show(des1, des3)
