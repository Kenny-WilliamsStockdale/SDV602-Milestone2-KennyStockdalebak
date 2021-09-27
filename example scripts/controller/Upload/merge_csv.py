"""
Merge CSV button controller
"""
import sys
import os
sys.dont_write_bytecode = True
import PySimpleGUI as sg
from model.model import Model

def accept( event, values, state):
    
    keep_going = True
    if event == 'Merge CSV':
       
        view = state['view']
        upload_file = os.path.basename(view.upload_file_path)
        target_file = os.path.basename(view.target_file_path)
        response = sg.PopupOKCancel(f'Merge {upload_file}\n into {target_file}?') 
        if response == "OK" :
            # Ask a Model to merge the two files
            a_model = Model()
            try:
                a_model.merge(view.upload_file_path,view.target_file_path )
                explorer_view = view.explorer_view
                explorer_view.update_data_from_csv(view.explorer_values,view.target_file_path )
            except Exception as e: # Here to use a "View" from the controller ?
                sg.Popup(f"Exception merging {upload_file} into {target_file} \n {e}")
            
            

    return keep_going