""" interactive screen showing graphical data to user.

    Returns:
        Data Explorer Screens layout shared between multiple interfaces -PySimpleGUI 
"""

import PySimpleGUI as sg
import datasourcenav
import login
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import des1
import des2
import dataexplorerscreens as des
matplotlib.use('TkAgg')

# ------------------------------- DATA EXPLORER SCREEN THREE START -------------------------------

def DataExplorerScreen3():
    """interactive screen showing graphical data to user. Includes navigation and chatsystem

    Returns:
        Data Explorer Screens layout shared between multiple interfaces -PySimpleGUI 
    """
    # ---- MATPLOTLIB CODE HERE -----
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
        title='About as simple as it gets, folks')
    ax.grid()


    # ---- END OF MATPLOTLIB CODE ----

    # ---- Beginning of Matplotlib helper code ----

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    # ---- Beginning of GUI CODE ----

    # define the window layout
    layout = [[sg.Canvas(key='-CANVAS-')],
            #   [sg.Button('ZOOM +'), sg.Button('ZOOM -')],
              [sg.Multiline(default_text='Data Information Summary:', size=(
                  35, 5)), sg.Multiline(default_text='Chat System:', size=(35, 5))],
              [sg.Button('Previous'), sg.Button('Next')],
              [sg.Button('Back'), sg.Button('Logout')]]

    # create the form and show it without the plot
    window = sg.Window('Number of property owners', layout,
                       finalize=True, element_justification='center', size=(800, 700))

    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Previous':
        window.close()
        des2.DataExplorerScreen2()
    if event == 'Next':
        window.close()
        des1.DataExplorerScreen1()
    if event == 'Back':
        window.close()
        datasourcenav.Data_source_page()
    if event == 'Logout':
        window.close()
        login.login_main()
# ------------------------------- DATA EXPLORER SCREEN THREE END -------------------------------