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
import des3
import dataexplorerscreens as des
import build
matplotlib.use('TkAgg')

# ------------------------------- DATA EXPLORER SCREEN TWO START -------------------------------

def DataExplorerScreen():
    """interactive screen showing graphical data to user. Includes navigation and chatsystem

    Returns:
        Data Explorer Screens layout shared between multiple interfaces -PySimpleGUI 
    """
    # ---- MATPLOTLIB CODE HERE -----
    fig, ax = plt.subplots(figsize=(7, 5), subplot_kw=dict(aspect="equal"))

    recipe = ["375 g flour",
          "75 g sugar",
          "250 g butter",
          "300 g berries"]

    data = [float(x.split()[0]) for x in recipe]
    ingredients = [x.split()[-1] for x in recipe]


    def func(pct, allvals):
        absolute = int(round(pct/100.*np.sum(allvals)))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)


    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                    textprops=dict(color="w"))

    ax.legend(wedges, ingredients,
            title="Ingredients",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title("Matplotlib bakery: A pie")


    # ---- END OF MATPLOTLIB CODE ----
    build.show(des1, des3)
    # ---- Beginning of Matplotlib helper code ----

    # def draw_figure(canvas, figure):
    #     figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    #     figure_canvas_agg.draw()
    #     figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    #     return figure_canvas_agg

    # # ---- Beginning of GUI CODE ----

    # # define the window layout
    # layout = [[sg.Canvas(key='-CANVAS-')],
    #         #   [sg.Button('ZOOM +'), sg.Button('ZOOM -')],
    #           [sg.Multiline(default_text='Data Information Summary:', size=(
    #               35, 5)), sg.Multiline(default_text='Chat System:', size=(35, 5))],
    #           [sg.Button('Previous'), sg.Button('Next')],
    #           [sg.Button('Back'), sg.Button('Logout')]]

    # # create the form and show it without the plot
    # window = sg.Window('Current property status', layout, finalize=True,
    #                    element_justification='center', size=(800, 700))

    # # add the plot to the window
    # fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    # event, values = window.read()
    # print(event, values)

    # if event == None or event == 'Exit Application':
    #     window.close()
    # if event == 'Previous':
    #     window.close()
    #     des1.DataExplorerScreen1()
    # if event == 'Next':
    #     window.close()
    #     des3.DataExplorerScreen3()
    # if event == 'Back':
    #     window.close()
    #     datasourcenav.Data_source_page()
    # if event == 'Logout':
    #     window.close()
    #     login.login_main()
# ------------------------------- DATA EXPLORER SCREEN TWO END -------------------------------