"""
Upload CSV button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

def accept( event, values, state):
    
    keep_going = True
    if event == 'Select Upload CSV':
       
        
        file_name = sg.PopupGetFile('Please select file to upload (the file to add to or merge in)', file_types=(("Comma separated value", "*.csv"),)) 
        if file_name != None :
            view = state['view']
            view.update_upload_file(file_name)

    return keep_going