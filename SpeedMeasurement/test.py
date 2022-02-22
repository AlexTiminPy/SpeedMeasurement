import keyboard
from os import system
import time
from rich.panel import Panel
from rich.console import Console
from fuzzywuzzy import fuzz
import argparse

console = Console()
target_text_ = ""
inp_text_ = ""
accuracy_ = []
SPM_ = []
Time_ = []


def update_console(target_text, inp_text) -> None:
    """
    update console after next letter
    """
    system("cls")
    console.print(f"Accuracy = {int(sum(accuracy_) / len(accuracy_)) if len(accuracy_) > 0 else 0}")
    console.print(f"{Time_=}")
    console.print(f"Symbol per minute = "
                  f"{int(sum(SPM_) / len(SPM_)) if len(SPM_) > 0 else 0}")
    console.rule("[bold red]Lets write!!!", align="left")
    console.print(f"[green]Вам нужно напечатать: \n[bold red]{target_text}[bold red]")
    print(f"{inp_text}<")


def calculate_symbol_per_minute(text, fin_time) -> int:
    """
    calculate symbol per minute and accuracy of text
    :param fin_time: time if fin write
    """
    SPM = len(text) / max(fin_time, 1) * 60

    return SPM


def calculate_accuracy(target_text, inp_text) -> int:
    """
    calculate accuracy of text
    """
    accuracy = fuzz.ratio(target_text, inp_text)
    return accuracy


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


def add_pressed_keys_to_text(e):
    """
    asynс func for work with console write
    """

    global target_text_, inp_text_

    if e.event_type == "down":

        if len(e.name) == 1:
            inp_text_ += e.name
            update_console(target_text_, inp_text_)

        elif e.name == "space":
            inp_text_ += " "
            update_console(target_text_, inp_text_)

        elif e.name == 'backspace':
            inp_text_ = inp_text_[:-1]
            update_console(target_text_, inp_text_)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', default="text.txt")
    parser.add_argument('-p', '--path',
                        default=r"C:\Users\1080176\PrintSpeedMeasurement\SpeedMeasurement\\"[:-1])

    return parser


def load_text_from_file(namespace) -> list:
    with open(str(namespace.path) + str(namespace.name), "r", encoding="utf-8") as file:
        text = file.readlines()
        file.close()

    return text


def main():
    parser = create_parser()
    perfect_text_list = load_text_from_file(parser.parse_args())
    keyboard.hook(add_pressed_keys_to_text)

    global target_text_, inp_text_

    for target_text in perfect_text_list:
        target_text = target_text[:-1]

        update_console(target_text, inp_text_)

        start_time = time.time()
        target_text_ = target_text

        a = input()
        # keyboard.wait("enter")

        fin_time = time.time() - start_time

        SPM = calculate_symbol_per_minute(inp_text_, fin_time)
        accuracy = calculate_accuracy(target_text, inp_text_)

        accuracy_.append(accuracy)
        SPM_.append(SPM)
        Time_.append(fin_time)

        # console.print(
        #     Panel.fit(
        #         f"time = {fin_time}\n"
        #         f"Symbol per second {SPM}\n"
        #         f"accuracy {accuracy}%",
        #         border_style=get_color_for_accuracy(accuracy)))

        inp_text_ = ""

        print('press "enter" for exit')
        # keyboard.wait("enter")

        system("cls")


if __name__ == '__main__':
    main()