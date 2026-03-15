import re

class Regex():
    @staticmethod
    def getParagraphs(text:str):
        return re.findall(r".+(?:\n(?!\n).+)*", text, flags=re.MULTILINE) # orra foi tempo pra pensar nesse regex, sou mtt burro
    
    @staticmethod
    def formatParagraphs(paragraphs:list):
        formatted_paragraphs = []
        for p in paragraphs:
            #linhas = p.splitlines()
            p = f'''<div class="paragraph">
    <p>{p}</p>
</div>
'''
            formatted_paragraphs.append(p)
        return formatted_paragraphs
    
    @staticmethod
    def save(text:str, file_name:str='blog.html'):
        with open(f'tests/{file_name}', 'w', encoding='utf-8') as file:
            file.write(text)
    

with open('tests/texto1.txt', 'r', encoding='utf-8') as f:
    texto = f.read()

print(f'TEXTO: \n{texto}')

paragrafos = Regex.getParagraphs(texto)
f_par = Regex.formatParagraphs(paragrafos)

Regex.save('\n'.join(f_par))