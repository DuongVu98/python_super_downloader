from pyfiglet import Figlet
from PyInquirer import style_from_dict, prompt, Token, Separator
from api import commands as cmds


def display_trademark():
    figlet = Figlet(font="speed")
    print(figlet.renderText("Stupid Downloader"))


def main():
    display_trademark()
    cmds.downloadManager()

    style = style_from_dict({
        Token.Separator: "#fff",
        Token.QuestionMark: "#000",
        Token.Selected: "#00BFFF",
        Token.Pointer: "#FFF",
        Token.Instructor: "#FFF",
        Token.Answer: "#008000 bold",
        Token.Question: "#FF7F50"
    })

    questions = [
        {
            "type": "list",
            "name": "Mathematic",
            "message": "2+3=?",
            "choices": ["5", "6", "7", "8"]
        }
    ]

    # answer = prompt(questions, style=style)
    # print(answer)


def other_main():
    cmds.downloadManager()


if __name__ == "__main__":
    main()
