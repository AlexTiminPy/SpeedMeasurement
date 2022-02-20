import keyboard
from os import system
import time
from rich.panel import Panel
from rich.console import Console
from fuzzywuzzy import fuzz

perfect_text = "привет как дела что делаешь?"
text = ""

console = Console()


def log_target() -> None:
    """
    print target for write
    :return: None
    """
    print(f"вам нужно напечатать: \n{perfect_text}")
    console.rule("[bold red]Lets write!!!", align="left")


def calculate_result(fin_time) -> (int, int):
    """
    calculate sumbok per minute and accuracy of text
    :param fin_time: time if fin write
    """
    SPM = len(perfect_text) / fin_time * 60
    accuracy = fuzz.ratio(perfect_text, text)
    return SPM, accuracy


def get_color_for_accuracy(accuracy: int) -> str:
    """
    return color for border for accuracy
    :return: border coolor
    """
    if accuracy == 100:
        return "blue"
    if accuracy > 90:
        return "green"
    if accuracy > 60:
        return "yellow"
    return "red"


def print_pressed_keys(e):
    """
    asynс func for work with console write
    """
    global text

    def update_console() -> None:
        """
        update console after next letter
        """
        system("cls")
        log_target()
        print(f"text: {text}<")

    if e.event_type == "down":

        if len(e.name) == 1:
            text += e.name
            update_console()

        if e.name == "space":
            text += " "
            update_console()

        if e.name == 'backspace':
            text = text[:-1]
            update_console()


def main():
    log_target()

    start_time = time.time()

    keyboard.hook(print_pressed_keys)
    keyboard.wait("enter")

    fin_time = time.time() - start_time

    SPM, accuracy = calculate_result(fin_time)

    console.print(
        Panel.fit(
            f"time = {fin_time}\n"
            f"Symbol per second {SPM}\n"
            f"accuracy {accuracy}%",
            border_style=get_color_for_accuracy(accuracy)))

    print('press "enter" for exit')
    keyboard.wait("enter")

    system("cls")


if __name__ == '__main__':
    main()
