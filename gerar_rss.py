import datetime
import html

# Configurações do Feed
BASE_URL = "https://www.cybernex.com.br"
BLOG_URL = f"{BASE_URL}/artigo.html"
TITLE = "Blog Cybernex Innovatech"
DESCRIPTION = "Dicas de SEO, Performance Web e Marketing Digital para alavancar seu negócio."
LANGUAGE = "pt-br"

# Dados dos Posts (Sincronizado com seu blog atual)
posts = {
    "seo-basico": {
        "title": "5 Dicas de SEO para Iniciantes",
        "description": "Se você quer que seu site seja encontrado no Google, precisa entender o básico de SEO (Search Engine Optimization).",
        "date": "12 Out 2023"
    },
    "performance-web": {
        "title": "Por que seu site está lento?",
        "description": "A velocidade do site impacta diretamente suas vendas e seu posicionamento no Google.",
        "date": "15 Out 2023"
    },
    "landing-vs-institucional": {
        "title": "Landing Page vs Site Institucional",
        "description": "Escolher o tipo certo de site é fundamental para atingir seus objetivos de negócio.",
        "date": "20 Out 2023"
    },
    "design-trends-2024": {
        "title": "Tendências de Web Design 2024",
        "description": "O web design está em constante evolução. Veja o que está em alta para 2024.",
        "date": "25 Out 2023"
    },
    "ga4-guia": {
        "title": "Entendendo o Google Analytics 4",
        "description": "O Universal Analytics morreu. O GA4 é o novo padrão e foca em eventos, não em sessões.",
        "date": "28 Out 2023"
    },
    "email-marketing": {
        "title": "Email Marketing ainda funciona?",
        "description": "Com tantas redes sociais, o email parece velho. Mas é o canal com maior ROI (Retorno sobre Investimento).",
        "date": "01 Nov 2023"
    }
}

def gerar_rss():
    print("Gerando rss.xml...")
    
    # Data de hoje para indicar a última atualização do feed
    now = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
    
    # Cabeçalho do RSS
    rss_content = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    rss_content += '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
    rss_content += '<channel>\n'
    rss_content += f'  <title>{TITLE}</title>\n'
    rss_content += f'  <link>{BASE_URL}</link>\n'
    rss_content += f'  <description>{DESCRIPTION}</description>\n'
    rss_content += f'  <language>{LANGUAGE}</language>\n'
    rss_content += f'  <lastBuildDate>{now}</lastBuildDate>\n'
    rss_content += f'  <atom:link href="{BASE_URL}/rss.xml" rel="self" type="application/rss+xml" />\n'
    
    # Mapeamento de meses para conversão de data
    meses = {
        "Jan": 1, "Fev": 2, "Mar": 3, "Abr": 4, "Mai": 5, "Jun": 6,
        "Jul": 7, "Ago": 8, "Set": 9, "Out": 10, "Nov": 11, "Dez": 12
    }

    for slug, post in posts.items():
        link = f"{BLOG_URL}?id={slug}"
        
        # Converter data (Ex: "12 Out 2023") para formato padrão RSS (RFC 822)
        dia, mes_str, ano = post['date'].split()
        mes = meses.get(mes_str, 1)
        dt = datetime.datetime(int(ano), mes, int(dia))
        pubDate = dt.strftime("%a, %d %b %Y 00:00:00 GMT")
        
        rss_content += '  <item>\n'
        rss_content += f'    <title>{html.escape(post["title"])}</title>\n'
        rss_content += f'    <link>{link}</link>\n'
        rss_content += f'    <guid isPermaLink="true">{link}</guid>\n'
        rss_content += f'    <description>{html.escape(post["description"])}</description>\n'
        rss_content += f'    <pubDate>{pubDate}</pubDate>\n'
        rss_content += '  </item>\n'

    rss_content += '</channel>\n'
    rss_content += '</rss>'
    
    with open('rss.xml', 'w', encoding='utf-8') as f:
        f.write(rss_content)
        
    print(f"Sucesso! rss.xml gerado com {len(posts)} artigos.")

if __name__ == "__main__":
    gerar_rss()