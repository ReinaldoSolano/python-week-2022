import typer

main = typer.Typer(help="Beer Management Application")

@main.command("add")
def add(name: str, style: str):
    """Adds a new beer to database."""
    print(name, style)

@main.command("list")
def list_beers(style: str):
    """Lists beers in database."""
    print(style)