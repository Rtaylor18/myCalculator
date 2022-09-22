import PySimpleGUI as sg

#variables for layout
sg.theme('Python')
button_size = (6,3)
font_s = 'Ubuntu 11'

layout = [[sg.Text('8008135',font='Ubuntu 14',justification='right',expand_x=True,pad=(10,20), key = '-OUTPUT-')],
          [sg.Button(7,font=font_s, size=button_size),sg.Button(8,font=font_s,size=button_size),sg.Button(9,font=font_s,size=button_size)],
          [sg.Button(4,font=font_s,size=button_size),sg.Button(5,font=font_s,size=button_size),sg.Button(6,font=font_s,size=button_size)],
          [sg.Button(1,font=font_s,size=button_size),sg.Button(2,font=font_s,size=button_size),sg.Button(3,font=font_s,size=button_size)],
          [sg.Button(0,font=font_s,size=button_size),sg.Button('-',font=font_s,size=button_size),sg.Button('+',font=font_s,size=button_size)],
          [sg.Button('.',font=font_s,size=button_size),sg.Button('/',font=font_s,size=button_size),sg.Button('*',font=font_s,size=button_size)],
          [sg.Button('Reset', font=font_s,expand_x=True), sg.Button('Enter',font=font_s, expand_x=True)]]

window = sg.Window('Calculator', layout)

#variables for calc
current_num = []
operation = []

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Reset':
        current_num = ['']
        window['-OUTPUT-'].update('') 

    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        
        window['-OUTPUT-'].update(num_string)

    if event in ['+','-','/','*']:
        operation.append(''.join(current_num))
        current_num = []
        operation.append(event)
        window['-OUTPUT-'].update(event)

    if event == 'Enter':
        operation.append(''.join(current_num))
        result = eval(' '.join(operation))
        window['-OUTPUT-'].update(result)
        operation = []

window.close()


          