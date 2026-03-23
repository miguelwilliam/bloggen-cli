import click
from datetime import datetime
from parser import Parser

@click.command()
@click.option('--filename-out', prompt='Nome do arquivo de saída' ,default=f'Blog {datetime.now().strftime("%d/%m/%Y")}', help='Especificar o nome do arquivo HTML de saída.')
@click.option('--filename-in', prompt='Nome do arquivo .txt', help='Nome (caminho) do arquivo que você tá tentando abrir (incluindo o .txt)')
@click.option('--blog-title', prompt='Título do blog')
def bloggen(filename_out, filename_in, blog_title):
    click.echo('BLOGGEN')
    if filename_out[-5:] != '.html':
        filename_out += '.html'

    if filename_in[-4:] != '.txt':
        filename_in += '.txt'
        
    try:
        with open(filename_in, 'r', encoding='utf-8') as f:
            texto = f.read()
        
    except:
        click.echo(f"ERRO: não conseguimos encontrar o arquivo de caminho '{filename_in}'.")
        return
    
    paragrafos = Parser.getParagraphs(texto)
    f_par = Parser.formatParagraphs(paragrafos)

    Parser.save('\n'.join(f_par), blog_title=blog_title, file_name=f'{filename_out}.html')
    click.echo(f"Seu arquivo de texto {filename_in} foi convertido para HTML, no arquivo '{filename_out}.html'")
    

if __name__ == '__main__':
    bloggen()