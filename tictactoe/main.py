from click import prompt
import TicTacToe as ttt  
import PySimpleGUI as psg
import sys


# game layout
field = [
    [psg.Button("", key="-00-", size=(2, 1)), psg.Button("", key="-10-", size=(2, 1)), psg.Button("", key="-20-", size=(2, 1))],
    [psg.Button("", key="-01-", size=(2, 1)), psg.Button("", key="-11-", size=(2, 1)), psg.Button("", key="-21-", size=(2, 1))],
    [psg.Button("", key="-02-", size=(2, 1)), psg.Button("", key="-12-", size=(2, 1)), psg.Button("", key="-22-", size=(2, 1))]
]

layout_game = [
     [psg.Text("", key="-STATUSTEXT-")],
     [psg.Column(field, justification="center")]
]

# menu layout
layout_menu = [
    [psg.Button(button_text="Start", key="-START-")],
    [psg.Button(button_text="Exit", key="-EXIT-")]
]

# main layout
layout = [
    [psg.Column(layout_menu, key="-MENU-", visible=True), psg.Column(layout_game, key="-GAME-", visible=False)]
]

window = psg.Window(title="TicTacToe", layout=layout)
if __name__ == "__main__":
    while True:
        event, value = window.read()
        match event:
            case None:
                break

            case "-EXIT-":
                break

            case "-START-":
                window["-MENU-"].update(visible=False)
                window["-GAME-"].update(visible=True)

                # create TicTacToe object
                ticcy = ttt.TicTacToe(x_start=True)
                
                # setup the game window
                window["-STATUSTEXT-"].update("X is the next one" if ticcy.x_turn() else "O ist the next one")

                # update Buttons
                for y_num, y_layer in enumerate(ticcy.get_field()):
                    for x_num, x_element in enumerate(y_layer):
                        window[f"-{x_num}{y_num}-"](x_element)
            
            case _:
                # make a set on the TicTacToe object
                ticcy.set(x=int(event[1]), y = int(event[2]))
                
                # update Buttons
                for y_num, y_layer in enumerate(ticcy.get_field()):
                    for x_num, x_element in enumerate(y_layer):
                        window[f"-{x_num}{y_num}-"](x_element)
                
                # set the statusbar
                window["-STATUSTEXT-"].update("X is the next one" if ticcy.x_turn() else "O ist the next one")

                # check for win
                if ticcy.is_won()[0]:
                    # won message
                    psg.popup_ok("WINNING!!!", f"{'X' if ticcy.is_won()[1] == 'x' else 'O'} won the Game!")
                    
                    # get back to menu
                    window["-MENU-"].update(visible=True)
                    window["-GAME-"].update(visible=False)
