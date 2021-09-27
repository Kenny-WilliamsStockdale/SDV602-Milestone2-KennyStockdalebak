"""
figure list controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import view.ChartExamples as ce

def accept( event, values, state):
    view = state['view']
    view.figure_list_draw(values)
    return True


