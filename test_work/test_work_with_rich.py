from rich import print as rprint
from rich import pretty
from rich.panel import Panel
from rich.console import Console

pretty.install()

rprint(Panel.fit("[bold yellow]Hi, I'm a Panel", border_style="red"))

rprint("[italic red]Hello[/italic red] World!", locals())

console = Console()
console.rule("[bold red]Chapter 2")

console = Console(width=20)

style = "bold white on blue"
console.print("Rich", style=style)
console.print("Rich", style=style, justify="left")
console.print("Rich", style=style, justify="center")
console.print("Rich", style=style, justify="right")

from typing import List
from rich.console import Console, OverflowMethod

console = Console(width=20)
supercali = "supercalifragilisticexpialidocious"

overflow_methods: List[OverflowMethod] = ["fold", "crop", "ellipsis"]
for overflow in overflow_methods:
    console.rule(overflow)
    console.print(supercali, overflow=overflow, style="bold blue")
    console.print()

from rich.console import Console

blue_console = Console(stderr=True, style="white on blue")
blue_console.print("I'm blue. Da ba dee da ba di.")

console = Console(record=True)

console.export_html()
