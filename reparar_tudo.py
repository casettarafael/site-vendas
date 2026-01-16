import os
import sys
import subprocess
import time
import webbrowser
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

# --- 1. CONTEÚDO LIMPO DE GERAR_PAGINAS.PY ---
# Usamos raw strings e concatenação para evitar erros de aspas
code_paginas = r'''import os
import re
import random

# Configurações
SOURCE_FILE = 'index.html'
OUTPUT_PREFIX = 'criacao-de-sites-em-'

# Lista de Capitais e Estados
locais = [
    {"nome": "Rio Branco", "uf": "AC", "slug": "rio-branco"},
    {"nome": "Maceió", "uf": "AL", "slug": "maceio"},
    {"nome": "Macapá", "uf": "AP", "slug": "macapa"},
    {"nome": "Manaus", "uf": "AM", "slug": "manaus"},
    {"nome": "Salvador", "uf": "BA", "slug": "salvador"},
    {"nome": "Fortaleza", "uf": "CE", "slug": "fortaleza"},
    {"nome": "Brasília", "uf": "DF", "slug": "brasilia"},
    {"nome": "Vitória", "uf": "ES", "slug": "vitoria"},
    {"nome": "Goiânia", "uf": "GO", "slug": "goiania"},
    {"nome": "São Luís", "uf": "MA", "slug": "sao-luis"},
    {"nome": "Cuiabá", "uf": "MT", "slug": "cuiaba"},
    {"nome": "Campo Grande", "uf": "MS", "slug": "campo-grande"},
    {"nome": "Belo Horizonte", "uf": "MG", "slug": "belo-horizonte"},
    {"nome": "Belém", "uf": "PA", "slug": "belem"},
    {"nome": "João Pessoa", "uf": "PB", "slug": "joao-pessoa"},
    {"nome": "Curitiba", "uf": "PR", "slug": "curitiba"},
    {"nome": "Recife", "uf": "PE", "slug": "recife"},
    {"nome": "Teresina", "uf": "PI", "slug": "teresina"},
    {"nome": "Rio de Janeiro", "uf": "RJ", "slug": "rio-de-janeiro"},
    {"nome": "Natal", "uf": "RN", "slug": "natal"},
    {"nome": "Porto Alegre", "uf": "RS", "slug": "porto-alegre"},
    {"nome": "Porto Velho", "uf": "RO", "slug": "porto-velho"},
    {"nome": "Boa Vista", "uf": "RR", "slug": "boa-vista"},
    {"nome": "Florianópolis", "uf": "SC", "slug": "florianopolis"},
    {"nome": "São Paulo", "uf": "SP", "slug": "sao-paulo"},
    {"nome": "Aracaju", "uf": "SE", "slug": "aracaju"},
    {"nome": "Palmas", "uf": "TO", "slug": "palmas"},
    {"nome": "Campinas", "uf": "SP", "slug": "campinas"},
    {"nome": "São José dos Campos", "uf": "SP", "slug": "sao-jose-dos-campos"},
    {"nome": "Ribeirão Preto", "uf": "SP", "slug": "ribeirao-preto"},
    {"nome": "Sorocaba", "uf": "SP", "slug": "sorocaba"},
    {"nome": "Santos", "uf": "SP", "slug": "santos"},
    {"nome": "Guarulhos", "uf": "SP", "slug": "guarulhos"},
    {"nome": "Niterói", "uf": "RJ", "slug": "niteroi"},
    {"nome": "São Gonçalo", "uf": "RJ", "slug": "sao-goncalo"},
    {"nome": "Uberlândia", "uf": "MG", "slug": "uberlandia"},
    {"nome": "Contagem", "uf": "MG", "slug": "contagem"},
    {"nome": "Joinville", "uf": "SC", "slug": "joinville"},
    {"nome": "Londrina", "uf": "PR", "slug": "londrina"},
    {"nome": "Caxias do Sul", "uf": "RS", "slug": "caxias-do-sul"}
]

segmentos = [
    {"nome": "Advogados", "slug": "advogado", "singular": "Advogado"},
    {"nome": "Clínicas", "slug": "clinica", "singular": "Clínica"},
    {"nome": "Médicos", "slug": "medico", "singular": "Médico"},
    {"nome": "Engenheiros", "slug": "engenheiro", "singular": "Engenheiro"},
    {"nome": "Dentistas", "slug": "dentista", "singular": "Dentista"},
    {"nome": "Arquitetos", "slug": "arquiteto", "singular": "Arquiteto"},
    {"nome": "Contadores", "slug": "contador", "singular": "Contador"},
    {"nome": "Imobiliárias", "slug": "imobiliaria", "singular": "Imobiliária"},
    {"nome": "Restaurantes", "slug": "restaurante", "singular": "Restaurante"},
    {"nome": "Delivery", "slug": "delivery", "singular": "Delivery"},
    {"nome": "Academias", "slug": "academia", "singular": "Academia"},
    {"nome": "Psicólogos", "slug": "psicologo", "singular": "Psicólogo"},
    {"nome": "Nutricionistas", "slug": "nutricionista", "singular": "Nutricionista"},
    {"nome": "Oficinas Mecânicas", "slug": "oficina-mecanica", "singular": "Oficina Mecânica"},
    {"nome": "Construtoras", "slug": "construtora", "singular": "Construtora"}
]

ddds_por_estado = {
    "AC": "68", "AL": "82", "AP": "96", "AM": "92", "BA": "71", "CE": "85", "DF": "61", "ES": "27",
    "GO": "62", "MA": "98", "MT": "65", "MS": "67", "MG": "31", "PA": "91", "PB": "83", "PR": "41",
    "PE": "81", "PI": "86", "RJ": "21", "RN": "84", "RS": "51", "RO": "69", "RR": "95", "SC": "48", "SP": "11", "SE": "79", "TO": "63"
}

def gerar_paginas():
    if not os.path.exists(SOURCE_FILE):
        print(f"Erro: {SOURCE_FILE} não encontrado.")
        return

    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        html_base = f.read()
    
    html_base = re.sub(r'local\.html\?geo=([a-z0-9-]+)', r'criacao-de-sites-em-\1.html', html_base)

    template = html_base.replace('Criação de Sites para Todo o Brasil', 'Criação de Sites em [[CIDADE]]')
    template = template.replace('Atendemos empresas de todos os estados do Brasil', 'Atendemos empresas de [[CIDADE]]')
    template = template.replace('empresas de todo o Brasil', 'empresas de [[CIDADE]]')
    template = template.replace('Atendimento em todo o território nacional', 'Atendimento especializado em [[CIDADE]]')
    template = template.replace('>Sites que transformam<', '>Criação de Sites em [[CIDADE]]<')
    template = template.replace('data-text="Sites que transformam"', 'data-text="Criação de Sites em [[CIDADE]]"')
    template = template.replace('Vocês atendem minha cidade?', 'Vocês atendem em [[CIDADE]]?')
    template = template.replace('Atendemos empresas de todos os estados do Brasil de forma 100% remota', 'Sim! Atendemos empresas de [[CIDADE]] de forma 100% remota')
    template = re.sub(r'<link\s+rel=["\']canonical["\']\s+href=["\']https://www\.cybernexinnovatech\.com\.br/?["\']\s*/?>', '<link rel="canonical" href="https://www.cybernexinnovatech.com.br/[[FILENAME]]">', template)

    print(f"Gerando {len(locais)} páginas de cidades...")

    variacoes_hero = [
        "Design profissional e código otimizado para empresas de [[CIDADE]] que buscam o próximo nível de faturamento.",
        "Desenvolvimento de sites de alta performance para negócios em [[CIDADE]] que desejam crescer na internet.",
        "Soluções web estratégicas para empresas de [[CIDADE]]. Sites rápidos e seguros.",
        "Criação de sites modernos e otimizados para o Google para empresas de [[CIDADE]]."
    ]
    
    variacoes_cta = ["Quero um Site Profissional", "Solicitar Orçamento Agora", "Aumentar Minhas Vendas", "Falar com Especialista"]
    variacoes_atendimento = ["Atendimento especializado em [[CIDADE]]", "Suporte dedicado para empresas de [[CIDADE]]", "Soluções digitais em [[CIDADE]]"]
    
    variacoes_titulo_extra = ["Por que sua empresa em [[CIDADE]] precisa de um site?", "Destaque-se no mercado de [[CIDADE]]", "Aumente suas vendas em [[CIDADE]]"]
    variacoes_texto_extra = [
        "O mercado em <strong>[[CIDADE]]</strong> está cada vez mais digital. Ter um site otimizado garante que sua empresa seja encontrada.",
        "Não deixe seu negócio fora do mapa digital de <strong>[[CIDADE]]</strong> (DDD [[DDD]]). A internet é sua maior vitrine.",
        "Empresas de <strong>[[CIDADE]]</strong> que não estão na internet estão perdendo dinheiro. Um site rápido é a chave para captar novos clientes."
    ]

    template_secao_extra = """
    <section class="local-market-section" style="background-color: #f8fafc; padding: 60px 0; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <h2 class="section-title">[[TITULO_EXTRA]]</h2>
            <p style="text-align: center; max-width: 800px; margin: 0 auto; color: #475569; font-size: 1.1rem; line-height: 1.8;">
                [[TEXTO_EXTRA]]
            </p>
            <div style="margin-top: 30px; text-align: center;">
                <p style="font-size: 0.9rem; color: #64748b; margin-bottom: 10px;">Atendemos também nas cidades vizinhas:</p>
                <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px;">
                    [[LINKS_VIZINHOS]]
                </div>
            </div>
        </div>
    </section>
    """

    for local in locais:
        filename = f"{OUTPUT_PREFIX}{local['slug']}.html"
        conteudo = template
        
        texto_padrao = "Design profissional e código otimizado para empresas de [[CIDADE]] que buscam o próximo nível de faturamento e autoridade digital."
        if texto_padrao in conteudo:
            conteudo = conteudo.replace(texto_padrao, random.choice(variacoes_hero))
            
        conteudo = conteudo.replace("Quero um Site Profissional", random.choice(variacoes_cta))
        conteudo = conteudo.replace("Atendimento especializado em [[CIDADE]]", random.choice(variacoes_atendimento))

        cidades_mesmo_estado = [l for l in locais if l['uf'] == local['uf'] and l['slug'] != local['slug']]
        vizinhos = random.sample(cidades_mesmo_estado, min(len(cidades_mesmo_estado), 4))
        links_vizinhos = "".join([f'<a href="{OUTPUT_PREFIX}{v["slug"]}.html" style="color: #2563eb; text-decoration: none; background: #e0e7ff; padding: 5px 10px; border-radius: 15px; font-size: 0.85rem;">{v["nome"]}</a>' for v in vizinhos])

        ddd = ddds_por_estado.get(local['uf'], "XX")
        secao = template_secao_extra.replace('[[TITULO_EXTRA]]', random.choice(variacoes_titulo_extra))
        secao = secao.replace('[[TEXTO_EXTRA]]', random.choice(variacoes_texto_extra))
        secao = secao.replace('[[DDD]]', ddd).replace('[[LINKS_VIZINHOS]]', links_vizinhos)
        
        if '<section id="faq">' in conteudo:
            conteudo = conteudo.replace('<section id="faq">', secao + '\n<section id="faq">')

        conteudo = conteudo.replace('"name": "Brazil"', f'"name": "{local["nome"]} - {local["uf"]}"').replace('"@type": "Country"', '"@type": "City"')
        conteudo = conteudo.replace('[[CIDADE]]', local['nome']).replace('[[UF]]', local['uf']).replace('[[FILENAME]]', filename)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
    print("Gerando página de Cobertura...")
    template_cob = html_base
    template_cob = template_cob.replace('Criação de Sites para Todo o Brasil', 'Área de Cobertura')
    template_cob = template_cob.replace('Sites que transformam', 'Área de Cobertura')
    template_cob = template_cob.replace('data-text="Sites que transformam"', 'data-text="Área de Cobertura"')
    template_cob = re.sub(r'<link\s+rel=["\']canonical["\']\s+href=["\']https://www\.cybernexinnovatech\.com\.br/?["\']\s*/?>', '<link rel="canonical" href="https://www.cybernexinnovatech.com.br/cobertura.html">', template_cob)
    
    lista_html = '<section style="padding: 60px 0;"><div class="container"><h2 class="section-title">Cidades Atendidas</h2><div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px;">'
    for local in sorted(locais, key=lambda x: (x['uf'], x['nome'])):
        lista_html += f'<a href="{OUTPUT_PREFIX}{local["slug"]}.html" style="text-decoration: none; color: #334155; padding: 10px; background: #f8fafc; border-radius: 5px; border: 1px solid #e2e8f0; display: block;">{local["nome"]} - {local["uf"]}</a>'
    lista_html += '</div></div></section>'

    if '<section class="stats-section">' in template_cob:
        template_cob = template_cob.replace('<section class="stats-section">', lista_html + '<div style="display:none;">')
        template_cob = template_cob.replace('<footer>', '</div><footer>')

    with open('cobertura.html', 'w', encoding='utf-8') as f:
        f.write(template_cob)

    print("Gerando segmentos...")
    template_seg = html_base
    template_seg = template_seg.replace('Criação de Sites para Todo o Brasil', 'Criação de Sites para [[SEGMENTO_PLURAL]]')
    template_seg = template_seg.replace('Atendemos empresas de todos os estados do Brasil', 'Especialistas em Sites para [[SEGMENTO_PLURAL]]')
    template_seg = template_seg.replace('>Sites que transformam<', '>Sites para [[SEGMENTO_PLURAL]]<')
    template_seg = template_seg.replace('data-text="Sites que transformam"', 'data-text="Sites para [[SEGMENTO_PLURAL]]"')
    template_seg = re.sub(r'<link\s+rel=["\']canonical["\']\s+href=["\']https://www\.cybernexinnovatech\.com\.br/?["\']\s*/?>', '<link rel="canonical" href="https://www.cybernexinnovatech.com.br/[[FILENAME]]">', template_seg)

    for seg in segmentos:
        filename = f"site-para-{seg['slug']}.html"
        conteudo = template_seg.replace('[[SEGMENTO_SINGULAR]]', seg['singular']).replace('[[SEGMENTO_PLURAL]]', seg['nome']).replace('[[FILENAME]]', filename)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(conteudo)

if __name__ == "__main__":
    gerar_paginas()
'''

# --- 2. CONTEÚDO DE GERAR_BLOG.PY ---
code_blog = r"""import os

TEMPLATE_FILE = 'artigo.html'

artigos = [
    {
        "slug": "artigo-seo-basico",
        "titulo": "5 Dicas de SEO para Iniciantes",
        "categoria": "SEO",
        "data": "12 Out 2023",
        "tempo": "5 min leitura",
        "imagem": "https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a?auto=format&fit=crop&w=800&q=80",
        "conteudo": "<p class='lead'>Se você quer que seu site seja encontrado no Google, precisa entender o básico de SEO.</p><h2>1. Palavras-chave</h2><p>Pesquise o que seu cliente busca.</p><h2>2. Títulos</h2><p>O H1 é fundamental.</p>"
    },
    {
        "slug": "artigo-performance-web",
        "titulo": "Por que seu site está lento?",
        "categoria": "Performance",
        "data": "15 Out 2023",
        "tempo": "4 min leitura",
        "imagem": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
        "conteudo": "<p class='lead'>A velocidade impacta vendas.</p><h2>Imagens Pesadas</h2><p>Use WebP.</p>"
    },
    {
        "slug": "artigo-landing-vs-institucional",
        "titulo": "Landing Page vs Site Institucional",
        "categoria": "Estratégia",
        "data": "20 Out 2023",
        "tempo": "6 min leitura",
        "imagem": "https://images.unsplash.com/photo-1533750349088-cd871a92f312?auto=format&fit=crop&w=800&q=80",
        "conteudo": "<p class='lead'>Escolha o tipo certo.</p><h2>Landing Page</h2><p>Foco em conversão.</p>"
    },
    {
        "slug": "artigo-design-trends-2024",
        "titulo": "Tendências de Web Design 2024",
        "categoria": "Design",
        "data": "25 Out 2023",
        "tempo": "3 min leitura",
        "imagem": "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?auto=format&fit=crop&w=800&q=80",
        "conteudo": "<p class='lead'>O que está em alta?</p><h2>Bento Grids</h2><p>Layouts modulares.</p>"
    },
    {
        "slug": "artigo-ga4-guia",
        "titulo": "Entendendo o Google Analytics 4",
        "categoria": "Dados",
        "data": "28 Out 2023",
        "tempo": "8 min leitura",
        "imagem": "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?auto=format&fit=crop&w=800&q=80",
        "conteudo": "<p class='lead'>O Universal Analytics morreu.</p><h2>Eventos</h2><p>Tudo é evento no GA4.</p>"
    },
    {
        "slug": "artigo-email-marketing",
        "titulo": "Email Marketing ainda funciona?",
        "categoria": "Marketing",
        "data": "01 Nov 2023",
        "tempo": "5 min leitura",
        "imagem": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=800&q=80",
        "conteudo": "<p class='lead'>O email tem alto ROI.</p><h2>Segmentação</h2><p>Envie a mensagem certa.</p>"
    }
]

def gerar_blog():
    if not os.path.exists(TEMPLATE_FILE):
        print(f"Erro: {TEMPLATE_FILE} não encontrado.")
        return

    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template_base = f.read()

    print(f"Gerando {len(artigos)} páginas de blog...")

    for post in artigos:
        filename = f"{post['slug']}.html"
        html = template_base
        html = html.replace('Blog Cybernex - Carregando Artigo...', f"{post['titulo']} - Blog Cybernex")
        html = html.replace('<link rel="canonical" href="https://www.cybernexinnovatech.com.br/">', f'<link rel="canonical" href="https://www.cybernexinnovatech.com.br/{filename}">')
        html = html.replace('<h1 id="article-title">Carregando artigo...</h1>', f'<h1>{post["titulo"]}</h1>')
        html = html.replace('<span id="article-category" class="blog-category"></span>', f'<span class="blog-category">{post["categoria"]}</span>')
        html = html.replace('<span id="article-date"></span>', post['data'])
        html = html.replace('<span id="article-read-time"></span>', post['tempo'])
        html = html.replace('<img id="article-img" src="" alt="">', f'<img src="{post["imagem"]}" alt="{post["titulo"]}" width="800" height="400" style="width:100%; height:auto;">')
        html = html.replace('<div id="article-body" class="article-content">', f'<div class="article-content">{post["conteudo"]}')
        html = html.replace('<div class="spinner" style="margin: 50px auto;"></div>', '') 
        html = html.replace('<script src="dados-blog.js" defer></script>', '')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
            
    print("Sucesso! Páginas de blog geradas.")

if __name__ == "__main__":
    gerar_blog()
"""

# --- 3. CONTEÚDO DE GERAR_TUDO.PY ---
code_tudo = r"""import os
import subprocess
import time
import webbrowser
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

def run_step(script_name):
    print(f"🔄 Executando {script_name}...")
    if os.path.exists(script_name):
        try:
            subprocess.run([sys.executable, script_name], check=True)
            print("✅ OK.")
        except Exception as e:
            print(f"❌ Erro: {e}")
    else:
        print(f"⚠️ {script_name} não encontrado.")

def main():
    print("--- 🚀 AUTO-BUILD & SERVER ---")
    
    run_step("gerar_paginas.py")
    run_step("gerar_blog.py")
    run_step("gerar_sitemap.py")
    run_step("gerar_rss.py")
    run_step("gerar_robots.py")
    run_step("seo_booster.py")

    print("\\n✨ Site gerado! Iniciando servidor em http://localhost:8000")
    
    def open_browser():
        time.sleep(2)
        webbrowser.open("http://localhost:8000")
    
    threading.Thread(target=open_browser).start()

    server_address = ('', 8000)
    try:
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        httpd.serve_forever()
    except Exception as e:
        print(f"Erro no servidor: {e}")

if __name__ == "__main__":
    main()
"""

def reparar():
    print("--- 🛠️ Reparando arquivos do sistema... ---")
    
    # Reescreve gerar_paginas.py (Limpo)
    with open('gerar_paginas.py', 'w', encoding='utf-8') as f:
        f.write(code_paginas)
    print("✅ gerar_paginas.py restaurado.")

    # Reescreve gerar_blog.py
    with open('gerar_blog.py', 'w', encoding='utf-8') as f:
        f.write(code_blog)
    print("✅ gerar_blog.py restaurado.")

    # Reescreve gerar_tudo.py
    with open('gerar_tudo.py', 'w', encoding='utf-8') as f:
        f.write(code_tudo)
    print("✅ gerar_tudo.py restaurado.")

    print("\n--- 🚀 Iniciando execução... ---")
    try:
        subprocess.run([sys.executable, 'gerar_tudo.py'], check=True)
    except Exception as e:
        print(f"Erro ao rodar: {e}")

if __name__ == "__main__":
    reparar()
