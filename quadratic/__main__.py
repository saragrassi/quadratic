# quadratic/__main__.py
import click
from . import Quadratic


@click.command()
@click.option("-a", required=True, type=float)
@click.option("-b", required=True, type=float)
@click.option("-c", required=True, type=float)
def main(a, b, c):
    """Solve the quadratic equation."""
    q = Quadratic(a, b, c)
    r1, r2 = q.solve()
    print(f"r1 = {r1}, r2 = {r2}")


if __name__ == "__main__":
    main()
