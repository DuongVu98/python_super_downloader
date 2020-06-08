from pyfiglet import Figlet
from PyInquirer import style_from_dict, prompt, Token, Separator
from api import commands


def display_trademark():
    figlet = Figlet(font="speed")
    print(figlet.renderText("Stupid Downloader"))


def other_main():
    display_trademark()
    commands.downloadManager()

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


def main():
    commands.downloadManager()


def draft():
    from service.DownloadFiles import DownloadFiles
    urls = [
        "http://quatest1.com.vn/images/PHP-DocumentFull.pdf",
        "http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf"
    ]
    destination = "downloaded"
    d = DownloadFiles(urls, destination)
    d.download()


if __name__ == "__main__":
    display_trademark()
    draft()
