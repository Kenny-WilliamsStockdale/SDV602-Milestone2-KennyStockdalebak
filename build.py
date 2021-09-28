import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')

# import des1
# import des2
# import des3 
# import datasourcenav
# import login

"""[Simple Data Explorer screen template 
    that can be used as a module for different displays of data]
"""

def show(nextScreen, previousScreen):
    # sg.theme('LightGreen')
    sg.set_options(element_padding=(5, 5))

    # ------ Menu Definition ------ #
    menu_def = [['&File', ['&Open Upload','&Logout', '&Exit']],
                ['&Navigation', ['&Property issue dates(DES1)', '&Types of ownership(DES2)', '&Number of property owners(DES3)']],
                ['&Help', '&About...'],
                ]

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
            
    fig = plt.figure(figsize=(10,4.2))


    # ------ GUI Defintion ------ #
    layout = [
        [sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
        # [sg.Text('Data Explorer Screen 1', font=('current 18'))],
        [sg.Canvas(key='-CANVAS-')],
        [sg.Multiline(default_text='Data Information Summary:', 
                     size=(55, 11), font=('current 12')),
        sg.Multiline(default_text='Chat System:', 
                     font=('current 12'), size=(55, 11))],
        [sg.Button('Previous', font=('current 20')), sg.Button('Next', font=('current 20'))]]

    window = sg.Window("Data Explorer Screen",
                       layout,
                       default_element_size=(12, 1),
                       default_button_element_size=(12, 1),
                       finalize=True,
                       element_justification='center',
                       size=(1000, 700))
    
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    # ------ Loop & Process button menu choices ------ #
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        print(event, values)
        # ------ Process menu choices ------ #
        if event == 'About...':
            # window.disappear()
            sg.popup('About this program', 'Version 1.0',
                     'PySimpleGUI Version', sg.version,  grab_anywhere=True)
            # window.reappear()
        if event == 'Previous':
            window.close()
            previousScreen.DataExplorerScreen()
        if event == 'Next':
            window.close()
            nextScreen.DataExplorerScreen()
            window.close()
        # if event == 'Back':
        #     window.close()
        #     datasourcenav.Data_source_page()
        # if event == 'Logout':
        #     window.close()
        #     login.login_main()
            
    
# if __name__ == "__main__":
#     test_menus()
#     pass