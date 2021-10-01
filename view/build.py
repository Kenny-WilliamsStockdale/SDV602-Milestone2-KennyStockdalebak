import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import view.des as des
import view.graph_view as gv

matplotlib.use('TkAgg')
explorer_screen_name = "DES Explorer Screen"
current_des = None
"""[Simple Data Explorer screen template 
    that can be used as a module for different displays of data]
"""
def show_des(p_des):
    global explorer_screen_name
    global current_des
    current_des = p_des
    explorer_screen_name = p_des.des_name
    show(current_des.nextScreen,current_des.previousScreen)
    
def show(nextScreen, previousScreen):
    import view.login as login
    # import view.des1 as des1
    # import view.des2 as des2
    # import view.des3 as des3
    sg.set_options(element_padding=(5, 5))
    global explorer_screen_name
    global current_des
    # ------ ANCHOR MENU SECTION ------ #
    menu_def = [['&File', ['&Open Upload','&Logout', '&Exit']],
                ['&Navigation', ['&Property issue dates(DES1)', '&Types of ownership(DES2)', '&Number of property owners(DES3)']],
                ['&Help', '&About...'],
                ]

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
            
    fig = current_des.getfigure()


    # ------ ANCHOR GUI/LAYOUT SECTION ------ #
    layout = [
        [sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
        [sg.Canvas(key='-CANVAS-')],
        [sg.Multiline(default_text='Data Information Summary:', 
                     size=(55, 11), font=('current 12')),
        sg.Multiline(default_text='Chat System:', 
                     font=('current 12'), size=(55, 11))],
        [sg.Button('Previous', font=('current 20')), sg.Button('Next', font=('current 20'))]]

    window = sg.Window(current_des.des_name,
                       layout,
                       default_element_size=(12, 1),
                       default_button_element_size=(12, 1),
                       finalize=True,
                       element_justification='center',
                       size=(1000, 700))
    
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    # ------ ANCHOR LOOP & PROCESS BUTTON & MENU CHOICES ------ #
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        print(event, values)
        # ------ Process button choices ------ #
        if event == 'Previous':
            window.close()
            current_des.previousScreen.show()
        if event == 'Next':
            window.close()
            current_des.nextScreen.show()
            window.close()
            
        # ------ Process menu choices ------ #
        if event == 'About...':
            sg.popup('About this program', 'Version 1.0',
                     'PySimpleGUI Version', sg.version,  grab_anywhere=True,)
        if event == 'Property issue dates(DES1)':
            window.close()
            des.des1.show()
            window.close()    
        if event == 'Types of ownership(DES2)':
            window.close()
            des.des2.show()
            window.close()
        if event == 'Number of property owners(DES3)':
            window.close()
            des.des3.show()
            window.close()
        if event == 'Logout':
            window.close()
            login.login_main()
            
            
# template empty until parsed in data

# class DataExplorerScreen()