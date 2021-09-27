"""
Select Target CSV button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

def accept( event, values, state):
    
    keep_going = True
    if event == 'Select Target CSV':
       
        
        file_name = sg.PopupGetFile('Please select file to update (the target)', file_types=(("Comma separated value", "*.csv"),)) 
        if file_name != None :
            view = state['view']
            view.update_target_file(file_name)

    return keep_going