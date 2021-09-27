"""
Exit button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg


def accept( event, values,state):
    
    keep_going = True
    if event in (sg.WIN_CLOSED, 'Exit'):   
        keep_going = False
        
        # this bit is a thought #
        #DES_View.current_des +=1 
        #DES_View.des_list.remove(state['view'])
    else:
        keep_going = True

    return keep_going 