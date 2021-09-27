import sys
sys.dont_write_bytecode = True
from typing import Dict
import view.ChartExamples as ce 
import controller.DES.exit_button as exit_button
import controller.DES.figure_list_select as figure_list_select
import controller.DES.new_des as new_des
import controller.DES.open_csv as open_csv
import controller.Upload.uploader as uploader
import PySimpleGUI as sg
import inspect
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np
import matplotlib.pyplot as plt

class DES_View(object):
    des_list = []
    current_des = 0
    
    def __init__(self):
        
        self.window = None
        self.figure_agg = None
        self.layout = []
        self.components = {"has_components":False}
        self.controls = []
        self.my_lastfig = None
        self.fig_dict = {'Line Plot':(ce.line_plot,{}),'Plot Dots(discrete plot)':(ce.discrete_plot,{}),
    'Name and Label':(ce.names_labels,{}),'Plot many Lines':(ce.multiple_plots,{}),
    'Bar Chart':(ce.bar_chart,{}),'Histogram':(ce.histogram,{'title':'Our Histogram Name'}),
    'Scatter Plots':(ce.scatter_plots,{}),'Stack Plot':(ce.stack_plot,{}),
    'Pie Chart 1':(ce.pie_chart1,{}),
    'Pie Chart 2':(ce.pie_chart2,{})}
        DES_View.current_des +=1 
        DES_View.des_list += [self]

    def have_selected_graph(self,values):
        return len(values['-LISTBOX-']) > 0
  
    def update_component_text(self,component_name, text):
        if component_name in self.components:
            self.components[component_name].update(text)

    def update_data_from_csv(self,values,file_name):
        from model.model import Model
        model = Model(data_source = file_name)
        fin_liabilities = model.get_column('    D3. Total interest payments as a percentage of household disposable income')
        stats_months = model.get_column('Year')
        self.update_current_data(values,file_name,data=fin_liabilities,x_values=stats_months,y_values=fin_liabilities,
                                    x_label='Year Month',y_label='Interest %',title_label='Interest payments % of disposable income')

    def update_current_data(self,values,file_name=None, **kwargs):
        if self.have_selected_graph(values) : 
            the_file_name = file_name
            choice = values['-LISTBOX-'][0] 
            (func,args) = self.fig_dict[choice]
            for arg_name in kwargs:
                args[arg_name] = kwargs[arg_name]
            
            if 'file_name' in args :
                the_file_name = args['file_name']
            if the_file_name != None :
                args['file_name'] = the_file_name
            else:
                the_file_name = "No data"
            self.update_component_text('data_file_name',the_file_name)
            self.fig_dict[choice] = (func,args)
            self.figure_list_draw(values)



        
    def draw_figure(self,canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    def delete_figure_agg(self,figure_agg):
        
        if self.figure_agg:
            self.figure_agg.get_tk_widget().forget()
        plt.close('all')



    def figure_list_draw(self,values):
        
        if self.have_selected_graph(values) :
            choice = values['-LISTBOX-'][0]                 # get first listbox item chosen (returned as a list)
            func_tuple = self.fig_dict[choice]                         # get function to call from the dictionary
            kwargs = func_tuple[1]
            
            func = func_tuple[0]
            
            
            self.window['-MULTILINE-'].update(inspect.getsource(func))  # show source code to function in multiline
            
            fig = func(**kwargs)                                    # call function to get the figure
            
            # ** IMPORTANT ** Clean up previous drawing before drawing again
            self.delete_figure_agg(self.figure_agg)


            the_file_name = "No Data"
            if 'file_name' in kwargs:
                the_file_name = kwargs['file_name']
            self.update_component_text('data_file_name',the_file_name)
            
            self.figure_agg = self.draw_figure(self.window['-CANVAS-'].TKCanvas, fig)  # draw the figure
    



    def set_up_layout(self,**kwargs):

        sg.theme('LightGreen')
        figure_w, figure_h = 550, 550
        # define the form layout
        listbox_values = list(self.fig_dict)
        print(f"GOT List box {listbox_values}")
        # one variable per call to sg 
        # if there is a control / input with it add the name to the controls list
        self.components['figures_list'] =  sg.Listbox(values=listbox_values, enable_events=True, size=(28, len(listbox_values)), key='-LISTBOX-')
        self.controls += [figure_list_select.accept]

        self.components['text_spacer'] = sg.Text(' ' * 12)

        self.components['uploader'] = sg.Button(button_text="Open Uploader",size=(10, 2))
        self.controls += [uploader.accept]
        self.components['new_des'] = sg.Button(button_text="New DES",size=(10, 2))
        self.controls += [new_des.accept]
        self.components['data_file_name'] = sg.Text('No data')
        self.components['select_file'] = sg.Button(button_text="Open CSV",size=(10, 2))
        self.controls += [open_csv.accept]

        self.components['exit_button'] = sg.Exit(size=(5, 2))        
        self.controls += [exit_button.accept]

        col_listbox = [
                        [self.components['figures_list']],
                        [self.components['text_spacer'],self.components['uploader'],self.components['new_des'],self.components['select_file'],self.components['exit_button'] ]
                    ]
        self.components['header'] =   sg.Text('Matplotlib Plot Test', font=('current 18'))
        self.components['list_box_padding'] =  sg.Col(col_listbox, pad=(5, (3, 330))) 
        self.components['canvas']   =   sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-') 
        self.components['MLine']    =  sg.MLine(size=(70, 35), pad=(5, (3, 90)), key='-MULTILINE-')   
        self.layout = [
                [self.components['header']],[self.components['data_file_name']],
                [self.components['list_box_padding'],self.components['canvas'],
                self.components['MLine']]
                ]

    def render(self):

        # create the form and show it without the plot
        if self.layout != [] :
            self.window =sg.Window('Our Demo Application with - Embedding Matplotlib In PySimpleGUI with **kwargs', self.layout, grab_anywhere=False, finalize=True)
            

    def accept_input(self):
 
            if self.window != None :
                keep_going = True
                
                while keep_going == True:
                    event, values = self.window.read()
                    for accept_control in self.controls:
                        keep_going = accept_control(event,values,{'view':self})
                self.window.close()

       
