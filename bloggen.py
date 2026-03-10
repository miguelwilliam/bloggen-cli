import click
from datetime import datetime

@click.command()
@click.option('--filename-out', default=f'Blog {datetime.now().strftime("%d/%m/%Y")}', help='Especificar o nome do arquivo HTML de saída.')
@click.argument('filename-in')
def bloggen(filename_out, filename_in):
    click.echo('BLOGGEN')
    click.echo(f"Seu arquivo de texto {filename_in} foi convertido para HTML, no arquivo '{filename_out}.html'")
    

if __name__ == '__main__':
    bloggen()