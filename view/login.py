"""
    This presents the user with a login page to create a username and password 
    to access the application.    
"""

import PySimpleGUI as sg
# import view.des1 as des1
import view.des as des

# ------------------------------- LOGIN MAIN PAGE START -------------------------------
def login_main():   
    """
       Function allows user to create or enter an existing password to login to the application
    """    
    layout = [
        [sg.Text('Username:')],
        [sg.InputText('')],
        [sg.Text('Password:')],
        [sg.InputText('')],
        [sg.Button('Login')],
        [sg.Button('Exit Application')]]
    window = sg.Window('Property Titles Login Page', layout, finalize=True)
    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Login':
        window.close()
        des.des1.show()
    if event == 'Exit Application':
        window.close()
# ------------------------------- LOGIN MAIN PAGE END -------------------------------

# ------------------------------- LOGIN WELCOME PAGE START -------------------------------

def login_main_Welcome():
    """
        function opens welcome login page. Navigation to available
    """    
    layout = [
        [sg.Text('Welcome')],
        [sg.Text('Username')],
        [sg.Button('View Data')],
        [sg.Button('Logout')]]
    window = sg.Window('Property Titles Login Page', layout,
                       finalize=True, size=(350, 150), element_justification='c')
    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'View Data':
        window.close()
        des1.DataExplorerScreen()
    if event == 'Exit Application':
        window.close()
# ------------------------------- LOGIN WELCOME PAGE END -------------------------------

# ------------------------------- LOGIN ERROR PAGE START -------------------------------

def login_main_Unsuccessful():
    """
        function gives error message of user credentials
    """    
    layout = [
        [sg.Text('The entered password and or username is incorrect.\nPlease enter your correct username and password')],
        [sg.Button('Login')]]
    window = sg.Window('Property Titles Login Page', layout,
                       finalize=True, size=(350, 150), element_justification='c')
    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Login':
        window.close()
        login_main()
# ------------------------------- LOGIN ERROR PAGE END -------------------------------