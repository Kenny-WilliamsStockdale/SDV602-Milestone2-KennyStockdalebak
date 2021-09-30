""" interactive screen showing graphical data to user.

    Returns:
        Data Explorer Screens build shared between multiple interfaces -PySimpleGUI 
"""

import PySimpleGUI as sg
import view.login as login
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import view.des2 as des2
import view.des3 as des3
import view.build as build
matplotlib.use('TkAgg')


# ------------------------------- DATA EXPLORER SCREEN ONE START -------------------------------

def DataExplorerScreen():
    """interactive screen showing graphical data to user. Includes navigation and chatsystem

    Returns:
        Data Explorer Screens build shared between multiple interfaces -PySimpleGUI 
    """    
    # ---- MATPLOTLIB CODE HERE -----
    # ---- END OF MATPLOTLIB CODE ----
    # build.show(des2, des3)