import re
from datetime import datetime

class Parser():
    @staticmethod
    def getParagraphs(text:str):
        return re.findall(r".+(?:\n(?!\n).+)*", text, flags=re.MULTILINE) # orra foi tempo pra pensar nesse regex, sou mtt burro
    
    @staticmethod
    def formatParagraphs(paragraphs:list):
        formatted_paragraphs = []
        for p in paragraphs:
            linhas = p.splitlines()
            
            linha_format = ''
            for linha in linhas:
                linha_format += f'        <p>{linha}</p>\n'
            linha_limpa = linha_format.rstrip('\n')
            
            formatted_paragraph = (
                '    <div class="paragraph">\n'
                f"{linha_limpa}\n"
                "    </div>\n"
            )
            
            formatted_paragraphs.append(formatted_paragraph)
        return formatted_paragraphs
    
    @staticmethod
    def save(blog_body:str, blog_title:str = f'BLOG {datetime.now().strftime('%d/%m/%Y')}', blog_date = f'{datetime.now().strftime('%d/%m/%Y')}', file_name:str='blog.html'):
        with open(f'tests/blog_base.html', 'r', encoding='utf-8') as file:
            blog_base = file.read()
        
        new_blog = re.sub(r'TÍTULO DO BLOG', blog_title, blog_base)
        new_blog = re.sub(r'DD\/MM\/YYYY', blog_date, new_blog)
        new_blog = re.sub(r'{{TEXTO}}', blog_body, new_blog)

        with open(f'{file_name}', 'w', encoding='utf-8') as file:
            file.write(new_blog)

# USANDO:
    
#with open('tests/texto2.txt', 'r', encoding='utf-8') as f:
#    texto = f.read()

#print(f'TEXTO: \n{texto}')

#paragrafos = Parser.getParagraphs(texto)
#f_par = Parser.formatParagraphs(paragrafos)

#Parser.save('\n'.join(f_par), blog_title='Blog sobre gerar blogs', file_name='blog.html')