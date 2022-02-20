from rich.console import Console
from rich.panel import Panel


def get_message(name: str, surname: str) -> str:
    """
    :param name:    is your name
    :param surname: is your surname
    :rtype string
    """
    return f"{name=} {surname=}"


def get_alter_message(name: str, surname: str) -> str:
    """
    :param name:    is your name
    :param surname: is your surname
    :rtype string
    """
    return f"{surname=} {name=}"


console = Console(width=100, stderr=True)

console.rule("[bold red]Chapter 0")
console.print(f"{get_message('Алексей', 'Тимин')}", justify="center")

console.rule("[bold red]Chapter 1")

console.print(f"{get_alter_message('Алексей', 'Тимин')}", justify="center")
