import os
import click

@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
@click.option('--food', prompt='Type of food', default='cakes', help='Type of food')
@click.option('--count', prompt='Amount eaten', default=1, help='Number of food items.')
def hello(count, name, food):
    """Example to show choices and using them."""
    for x in range(count):
        click.echo('%s ate %s %s!' % (name, x,food))
    click.echo('%s projectile vomited - too many %s!' % (name, food))

if __name__ == '__main__':
    hello()
