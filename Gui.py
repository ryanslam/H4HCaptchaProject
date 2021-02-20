import PySimpleGUI as sg
import cv2
import numpy as np


def 

def main():
    sg.theme('Black')

    # define the window layout
    layout = [[sg.Text('H4H Visual Verification', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image', size=(40, 20))],]

    # create the window and show it without the plot
    window = sg.Window('H4H Visual Verification', layout, location=(200, 200))

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    cap = cv2.VideoCapture(0)
    recording = False

    while True:
        event, values = window.read(timeout=20)
        if event == sg.WIN_CLOSED:
            return

        # elif event == 'Record':
        #     recording = True

        # elif event == 'Stop':
        #     recording = False
        #     img = np.full((480, 640), 255)
        #     # this is faster, shorter and needs less includes
        #     imgbytes = cv2.imencode('.png', img)[1].tobytes()
        #     window['image'].update(data=imgbytes)

        if True:
            ret, frame = cap.read()
            imgbytes = cv2.imencode('.png', frame)[1].tobytes()  # ditto
            window['image'].update(data=imgbytes)


main()