"""
    Navigation of datasource interface
"""

import PySimpleGUI as sg
import login
import dataexplorerscreens as des
import uploadnewdata
import des1
import des2
import des3
# ------------------------------- DATA SOURCE PAGE START-------------------------------

def Data_source_page():
    """
        function allows user to navigation to data explorer screens 
    """    
    layout = [
        [sg.Button('Property issue dates'),
         sg.Button('Current property status')],
        [sg.Button('Number of property owners'), sg.Button('Upload new data')],
        [sg.Button('Logout')]]
    window = sg.Window('Data Source Page', layout, finalize=True,
                       size=(500, 150), element_justification='c')

    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Property issue dates':
        window.close()
        des1.DataExplorerScreen1()
    if event == 'Current property status':
        window.close()
        des2.DataExplorerScreen2()
    if event == 'Number of property owners':
        window.close()
        des3.DataExplorerScreen3()
    if event == 'Upload new data':
        window.close()
        uploadnewdata.Upload_new_data_page()
    if event == 'Logout':
        window.close()
        login.login_main()
# ------------------------------- DATA SOURCE PAGE END -------------------------------
# Invoking start script/function for user to begin the proccess of using the application.  
if __name__ == "__main__":
    # def function here
    login.login_main()
    pass