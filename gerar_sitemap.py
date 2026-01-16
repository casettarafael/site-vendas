import datetime
from gerar_paginas import locais, segmentos

# Configurações
BASE_URL = "https://www.cybernexinnovatech.com.br"

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

    # 2.1 Página de Cobertura
    xml_content += '  <url>\n'
    xml_content += f'    <loc>{BASE_URL}/cobertura.html</loc>\n'
    xml_content += f'    <lastmod>{hoje}</lastmod>\n'
    xml_content += '    <priority>0.80</priority>\n'
    xml_content += '  </url>\n'

    # 3. Páginas Locais Dinâmicas (Prioridade Média-Alta)
    # Aponta para as páginas estáticas geradas (Mais rápido e melhor SEO)
    for local in locais:
        slug = local['slug']
        url = f"{BASE_URL}/criacao-de-sites-em-{slug}.html"
        
        xml_content += '  <url>\n'
        xml_content += f'    <loc>{url}</loc>\n'
        xml_content += f'    <lastmod>{hoje}</lastmod>\n'
        xml_content += '    <priority>0.80</priority>\n'
        xml_content += '  </url>\n'
        
    # 4. Páginas de Segmentos (Prioridade Alta)
    for seg in segmentos:
        slug = seg['slug']
        url = f"{BASE_URL}/site-para-{slug}.html"
        xml_content += '  <url>\n'
        xml_content += f'    <loc>{url}</loc>\n'
        xml_content += f'    <lastmod>{hoje}</lastmod>\n'
        xml_content += '    <priority>0.90</priority>\n'
        xml_content += '  </url>\n'

    xml_content += '</urlset>'
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml_content)
        
    print(f"Sucesso! sitemap.xml gerado com {len(locais) + len(segmentos) + 3} URLs.")

if __name__ == "__main__":
    gerar_xml()