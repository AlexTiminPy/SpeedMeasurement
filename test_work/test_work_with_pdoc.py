from rich import print as rprint
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


console = Console(width=50, stderr=True, style="black on white")
console.print(get_message("Алексей", "Тимин"))
console.print(Panel.fit(f"{get_alter_message('Алексей', 'Тимин')}", border_style="red"))
console.rule("[bold red]Chapter 2")
