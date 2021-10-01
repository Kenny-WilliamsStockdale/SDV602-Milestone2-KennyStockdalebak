""" interactive screen showing graphical data to user.

    Returns:
        Data Explorer Screens build shared between multiple interfaces -PySimpleGUI 
"""
import view.build as build
import view.graph_view as gv
import model.datafilters as df
import matplotlib.pyplot as plt
# ------------------------------- DATA EXPLORER SCREEN ONE START -------------------------------

class DataExplorerScreen():
    """interactive screen showing graphical data to user. Includes navigation and chatsystem

    Returns:
        Data Explorer Screens build shared between multiple interfaces -PySimpleGUI 
    """    
    # ---- MATPLOTLIB CODE HERE -----
    # ---- END OF MATPLOTLIB CODE ----
    def __init__(self, des_name,des_dataFunction) -> None:
        self.nextScreen = None
        self.previousScreen = None
        self.des_name = des_name
        self.data = []
        self.dataFunction = des_dataFunction
        
    def set_next_previous(self,nextscreen, previousscreen):
        self.nextScreen = nextscreen
        self.previousScreen = previousscreen
        
    def show(self):
        # build.show(self.previousScreen, self.nextScreen)
        build.show_des(self)
        
    
    
    def getfigure(self): 
         
        labels, values = df.sizeFish()
        fig1, ax1 = plt.subplots(figsize=(10,4.2))
        ax1.pie(values, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=0)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Size of Angler Fish in mm')
        # labels here from example
        # #       ax.plot(x_values, y_values)
        # #       ax.set(xlabel=x_label,
        # #       ylabel=y_label,
        # #       title=title_label)
        #         #plt.show()
        return plt.gcf() 
            # self.update_component_text('data_file_name',the_file_name)

        # self.figure_agg = self.draw_figure(self.window['-CANVAS-'].TKCanvas, fig)  # draw the figure
      
        
des1 = DataExplorerScreen(build.explorer_screen_name, df.sizeFish)
des2 = DataExplorerScreen(build.explorer_screen_name, df.sizeFish)
des3 = DataExplorerScreen(build.explorer_screen_name, df.sizeFish)

des1.set_next_previous(des2,des3)
des2.set_next_previous(des3,des1)
des3.set_next_previous(des1,des2)
