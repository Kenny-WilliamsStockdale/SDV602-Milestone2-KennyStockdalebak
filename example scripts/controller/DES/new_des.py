"""
New DES button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg


def accept( event, values, state):
    from view.data_explorer_view import DES_View
    
    keep_going = True
    if event == 'New DES':
        des_obj = DES_View()
        des_obj.set_up_layout()
        des_obj.render()
        des_obj.accept_input()
    return keep_going 