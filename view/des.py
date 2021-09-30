""" interactive screen showing graphical data to user.

    Returns:
        Data Explorer Screens build shared between multiple interfaces -PySimpleGUI 
"""
import view.build as build


# ------------------------------- DATA EXPLORER SCREEN ONE START -------------------------------

class DataExplorerScreen():
    """interactive screen showing graphical data to user. Includes navigation and chatsystem

    Returns:
        Data Explorer Screens build shared between multiple interfaces -PySimpleGUI 
    """    
    # ---- MATPLOTLIB CODE HERE -----
    # ---- END OF MATPLOTLIB CODE ----
    def __init__(self, des_name) -> None:
        self.nextScreen = None
        self.previousScreen = None
        self.des_name = des_name
        self.data = []
        
    def set_next_previous(self,nextscreen, previousscreen):
        self.nextScreen = nextscreen
        self.previousScreen = previousscreen
        
    def show(self):
        # build.show(self.previousScreen, self.nextScreen)
        build.show_des(self)
        
        
    # self.update_component_text('data_file_name',the_file_name)
            
    # self.figure_agg = self.draw_figure(self.window['-CANVAS-'].TKCanvas, fig)  # draw the figure
        
        
        
des1 = DataExplorerScreen("DES1")
des2 = DataExplorerScreen("DES2")
des3 = DataExplorerScreen("DES3")

des1.set_next_previous(des2,des3)
des2.set_next_previous(des3,des1)
des3.set_next_previous(des1,des2)