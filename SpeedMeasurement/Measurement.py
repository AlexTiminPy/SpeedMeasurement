import msvcrt
import sys
import time
from os import system
from rich.console import Console
import argparse


def update_console(console, text_, target_text_, start, SPM_):
    system("cls")

    console.print(f"{SPM_} {time.time() - start}")
    print_different_in_texts(console, text_, target_text_)


def print_different_in_texts(console, text, target_text):
    console.print(target_text)

    if not text:
        return

    for i, t in enumerate(text):
        try:
            if t == target_text[i]:
                console.print(f"[green]{t}", end="")
            else:
                console.print(f"[red]{t}", end="")
        except:
            console.print(f"[red]{t}", end="")


def calculate_SPM(target_text_, time_):
    SPM = len(target_text_) / max(time_, 1) * 60

    return SPM


def speed_measurement(console, target_text_):
    SPM_ = 0
    text_ = ''

    layout = \
        ("""!-()qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?
            йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,""")

    start = time.time()
    update_console(console, text_, target_text_, start, SPM_)

    while True:
        pressedKey = msvcrt.getwch()
        if pressedKey.encode("utf-8") == b'\x03':  # ctrl + c
            sys.exit()
        elif pressedKey.encode("utf-8") == b'\r':  # enter
            if target_text_ == text_:
                SPM_ = calculate_SPM(target_text_, time.time() - start)
                update_console(console, text_, target_text_, start, SPM_)
                break
        elif pressedKey.encode("utf-8") == b'\b':  # backspace
            text_ = text_[:-1]
            update_console(console, text_, target_text_, start, SPM_)
        else:
            if pressedKey in layout:
                text_ += pressedKey
                update_console(console, text_, target_text_, start, SPM_)


def pause(console):
    console.print("\npress ENTER for next set of words")
    while True:
        pressedKey = msvcrt.getwch()
        if pressedKey.encode("utf-8") == b'\r':  # enter
            break


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
    console = Console()

    for target_text_ in perfect_text_list:
        speed_measurement(console, target_text_[:-1])
        pause(console)


if __name__ == '__main__':
    main()
