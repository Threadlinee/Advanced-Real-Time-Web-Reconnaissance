import click
from utils.graph import draw_graph
import requests

@click.group()
def cli():
    pass

@cli.command()
def export():
    r = requests.get("http://localhost:5000/export")
    print(r.json())

@cli.command()
def graph():
    draw_graph()

if __name__ == "__main__":
    cli()
