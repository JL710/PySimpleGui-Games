import PySimpleGUI as psg  
import Hangman
import sys


def main():
    word = psg.popup_get_text("Word")
    if word == None:
        sys.exit()

    hangman = Hangman.Hangman(word, 8)
    
    layout = [
        [psg.Text("".join([x if x != "" else "#" for x in hangman.get_uncompleted_word()]), key="word", expand_x=True, justification="center", font="bold")],
        [psg.In(key="entry", enable_events=False), psg.Button("Guess Letter", key="button_guess_letter")],
        [psg.Image(source="0.png", key="image", expand_x=True)],
        [psg.Listbox(values=[], key="letters", size=(1, 5), expand_x=True)]
    ]
    window = psg.Window(title="Hangman", layout=layout)
    while True:
        event, values = window.read()
        match event:
            case None:
                sys.exit()
                break
            
            case "button_guess_letter":
                if values["entry"] != "" and len(values["entry"]) == 1:
                    hangman.guess_letter(values["entry"])
                    uncompleted_word = "".join([x if x != "" else "#" for x in hangman.get_uncompleted_word()])
                    window["word"](uncompleted_word)
                    window["image"](f"{hangman.get_number_of_wrong_guessed_letters()}.png")
                    window["letters"](hangman.get_guessed_letters())
                    # check if won
                    if hangman.is_finished():
                        psg.popup_error(f"You Lose. The Correct word was {hangman.get_word()}")
                        break
                    if hangman.is_won():
                        psg.popup_ok(f"You Won! {hangman.get_word()}")
                        break
                window["entry"]("")

if __name__ == "__main__":
    psg.theme("DarkAmber")
    while True:
        main()
