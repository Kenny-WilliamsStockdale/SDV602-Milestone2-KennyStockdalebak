"""
OpenCSV button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
from model.model import Model

def accept( event, values, state):
    
    keep_going = True
    if event == 'Open CSV':
       
        
        file_name = sg.PopupGetFile('Please select file to open', file_types=(("Comma separated value", "*.csv"),)) 
        if file_name != None :
            view = state['view']
            view.update_data_from_csv(values,file_name)
    return keep_going