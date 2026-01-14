import datetime

# Configurações
BASE_URL = "https://www.cybernex.com.br"

# Lista de Locais (Mesma do seu site)
locais = [
    "rio-branco", "maceio", "macapa", "manaus", "salvador", "fortaleza", 
    "brasilia", "vitoria", "goiania", "sao-luis", "cuiaba", "campo-grande", 
    "belo-horizonte", "belem", "joao-pessoa", "curitiba", "recife", "teresina", 
    "rio-de-janeiro", "natal", "porto-alegre", "porto-velho", "boa-vista", 
    "florianopolis", "sao-paulo", "aracaju", "palmas",
    # Interior de SP
    "campinas", "sao-jose-dos-campos", "ribeirao-preto", "sorocaba", "sao-jose-do-rio-preto"
]

def gerar_xml():
    print("Gerando sitemap.xml...")
    
    # Data de hoje para lastmod
    hoje = datetime.date.today().isoformat()
    
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # 1. Página Inicial (Prioridade Alta)
    xml_content += '  <url>\n'
    xml_content += f'    <loc>{BASE_URL}/</loc>\n'
    xml_content += f'    <lastmod>{hoje}</lastmod>\n'
    xml_content += '    <priority>1.00</priority>\n'
    xml_content += '  </url>\n'

    # 2. Página de Artigo (Exemplo genérico ou lista de artigos se tiver)
    # Se quiser listar artigos específicos, adicione aqui
    xml_content += '  <url>\n'
    xml_content += f'    <loc>{BASE_URL}/artigo.html</loc>\n'
    xml_content += f'    <lastmod>{hoje}</lastmod>\n'
    xml_content += '    <priority>0.80</priority>\n'
    xml_content += '  </url>\n'

    # 3. Páginas Locais Dinâmicas (Prioridade Média-Alta)
    # O Google indexa parâmetros de URL se estiverem no sitemap
    for slug in locais:
        # Nota: O caractere & deve ser escapado como &amp; em XML, 
        # mas aqui usamos ?geo= que é seguro.
        url = f"{BASE_URL}/local.html?geo={slug}"
        
        xml_content += '  <url>\n'
        xml_content += f'    <loc>{url}</loc>\n'
        xml_content += f'    <lastmod>{hoje}</lastmod>\n'
        xml_content += '    <priority>0.80</priority>\n'
        xml_content += '  </url>\n'

    xml_content += '</urlset>'
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml_content)
        
    print(f"Sucesso! sitemap.xml gerado com {len(locais) + 2} URLs.")

if __name__ == "__main__":
    gerar_xml()