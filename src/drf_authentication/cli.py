"""Console script for drf_authentication."""
import drf_authentication

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for drf_authentication."""
    console.print("Replace this message by putting your code into "
               "drf_authentication.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
