import re
import os

# Configurações
TEMPLATE_FILE = 'artigo.html'

# Dados dos Artigos
artigos = [
    {
        "slug": "artigo-seo-basico",
        "titulo": "5 Dicas de SEO para Iniciantes",
        "categoria": "SEO",
        "data": "12 Out 2023",
        "tempo": "5 min leitura",
        "imagem": "https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a?auto=format&fit=crop&w=800&q=80",
        "conteudo": """
            <p class="lead">Se você quer que seu site seja encontrado no Google, precisa entender o básico de SEO (Search Engine Optimization).</p>
            <h2>1. Palavras-chave são a base</h2>
            <p>Antes de escrever, pesquise o que seu cliente busca. Ferramentas como Google Trends e Ubersuggest ajudam a encontrar termos com bom volume de busca.</p>
            <h2>2. Títulos e Meta Descrições</h2>
            <p>O título (H1) é o fator on-page mais importante. A meta descrição funciona como um anúncio para atrair o clique nos resultados da pesquisa.</p>
            <h2>3. Velocidade de Carregamento</h2>
            <p>Sites lentos perdem posições. Otimize imagens e use cache. O Google prioriza a experiência do usuário (Core Web Vitals).</p>
            <h2>4. Conteúdo de Qualidade</h2>
            <p>O Google ficou inteligente. Não adianta repetir a palavra-chave 50 vezes. Escreva conteúdo que realmente resolva a dúvida do usuário.</p>
            <h2>5. Mobile First</h2>
            <p>A maioria das buscas hoje é feita pelo celular. Se seu site não funciona bem no mobile, você praticamente não existe para o Google.</p>
        """
    },
    {
        "slug": "artigo-performance-web",
        "titulo": "Por que seu site está lento?",
        "categoria": "Performance",
        "data": "15 Out 2023",
        "tempo": "4 min leitura",
        "imagem": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
        "conteudo": """
            <p class="lead">A velocidade do site impacta diretamente suas vendas e seu posicionamento no Google.</p>
            <h2>Imagens Pesadas</h2>
            <p>O erro mais comum. Imagens de 5MB direto da câmera travam o carregamento. Use formatos modernos como WebP e comprima os arquivos.</p>
            <h2>Muitos Scripts</h2>
            <p>Plugins de chat, analytics, pixels de rastreamento... tudo isso pesa. Carregue apenas o essencial ou use 'defer' para adiar o carregamento.</p>
            <h2>Hospedagem Ruim</h2>
            <p>Se o servidor demora para responder (TTFB), não há otimização de código que salve. Invista em uma hospedagem de qualidade.</p>
        """
    },
    {
        "slug": "artigo-landing-vs-institucional",
        "titulo": "Landing Page vs Site Institucional",
        "categoria": "Estratégia",
        "data": "20 Out 2023",
        "tempo": "6 min leitura",
        "imagem": "https://images.unsplash.com/photo-1533750349088-cd871a92f312?auto=format&fit=crop&w=800&q=80",
        "conteudo": """
            <p class="lead">Escolher o tipo certo de site é fundamental para atingir seus objetivos de negócio.</p>
            <h2>Site Institucional</h2>
            <p>Focado em construção de marca e autoridade. Tem várias páginas (Sobre, Serviços, Blog, Contato). Ideal para empresas que vendem serviços complexos ou B2B.</p>
            <h2>Landing Page</h2>
            <p>Focada em UMA única ação: conversão. Geralmente usada em campanhas de tráfego pago. Não tem menu de navegação para não distrair o usuário.</p>
            <h2>Qual escolher?</h2>
            <p>Se você quer vender um produto específico agora, vá de Landing Page. Se quer construir presença digital a longo prazo, comece pelo Institucional.</p>
        """
    },
    {
        "slug": "artigo-design-trends-2024",
        "titulo": "Tendências de Web Design 2024",
        "categoria": "Design",
        "data": "25 Out 2023",
        "tempo": "3 min leitura",
        "imagem": "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?auto=format&fit=crop&w=800&q=80",
        "conteudo": """
            <p class="lead">O web design está em constante evolução. Veja o que está em alta.</p>
            <h2>Bento Grids</h2>
            <p>Inspirado nas marmitas japonesas e popularizado pela Apple, esse layout em grade modular organiza o conteúdo de forma visualmente interessante e responsiva.</p>
            <h2>Tipografia Gigante</h2>
            <p>Títulos enormes que ocupam a tela toda estão substituindo imagens de herói tradicionais. A mensagem textual ganha destaque total.</p>
            <h2>Micro-interações</h2>
            <p>Pequenas animações ao passar o mouse ou clicar tornam a navegação mais viva e intuitiva, sem pesar o site.</p>
        """
    },
    {
        "slug": "artigo-ga4-guia",
        "titulo": "Entendendo o Google Analytics 4",
        "categoria": "Dados",
        "data": "28 Out 2023",
        "tempo": "8 min leitura",
        "imagem": "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?auto=format&fit=crop&w=800&q=80",
        "conteudo": """
            <p class="lead">O Universal Analytics morreu. O GA4 é o novo padrão e foca em eventos, não em sessões.</p>
            <h2>Tudo é um Evento</h2>
            <p>No GA4, visualizar uma página é um evento. Clicar é um evento. Rolar a página é um evento. Isso dá muito mais flexibilidade para medir interações.</p>
            <h2>Privacidade</h2>
            <p>O GA4 foi construído pensando em um mundo sem cookies, usando inteligência artificial para preencher lacunas de dados.</p>
            <h2>Engajamento</h2>
            <p>A métrica 'Taxa de Rejeição' foi substituída por 'Taxa de Engajamento', que é muito mais útil para entender se o usuário realmente consumiu o conteúdo.</p>
        """
    },
    {
        "slug": "artigo-email-marketing",
        "titulo": "Email Marketing ainda funciona?",
        "categoria": "Marketing",
        "data": "01 Nov 2023",
        "tempo": "5 min leitura",
        "imagem": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=800&q=80",
        "conteudo": """
            <p class="lead">Com tantas redes sociais, o email parece velho. Mas é o canal com maior ROI.</p>
            <h2>Terreno Próprio</h2>
            <p>Nas redes sociais, o algoritmo decide quem vê seu post. No email, a lista é sua e a entrega é garantida (se você tiver uma boa reputação).</p>
            <h2>Segmentação</h2>
            <p>Você pode enviar ofertas diferentes para quem comprou o produto A e para quem comprou o produto B. Isso aumenta drasticamente a conversão.</p>
            <h2>Automação</h2>
            <p>Configure uma sequência de boas-vindas e venda no piloto automático enquanto você dorme.</p>
        """
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
        
        # Substituições no Template
        html = html.replace('Blog Cybernex - Carregando Artigo...', f"{post['titulo']} - Blog Cybernex")
        html = html.replace('content="Aprenda as melhores estratégias de SEO para colocar seu site no topo do Google."', f'content="{post["titulo"]} - Leia mais no Blog da Cybernex."')
        html = re.sub(r'<link\s+rel=["\']canonical["\'].*?>', f'<link rel="canonical" href="https://www.cybernexinnovatech.com.br/{filename}">', html)
        
        # Conteúdo Visível
        html = html.replace('<h1 id="article-title">Carregando artigo...</h1>', f'<h1>{post["titulo"]}</h1>')
        html = html.replace('<span id="article-category" class="blog-category"></span>', f'<span class="blog-category">{post["categoria"]}</span>')
        html = html.replace('<span id="article-date"></span>', post['data'])
        html = html.replace('<span id="article-read-time"></span>', post['tempo'])
        html = html.replace('<img id="article-img" src="" alt="">', f'<img src="{post["imagem"]}" alt="{post["titulo"]}" width="800" height="400" style="width:100%; height:auto;">')
        
        # Corpo do Texto
        html = html.replace('<div id="article-body" class="article-content">', f'<div class="article-content">\n{post["conteudo"]}')
        html = html.replace('<div class="spinner" style="margin: 50px auto;"></div>', '') 

        # Remove script JS desnecessário para página estática
        html = html.replace('<script src="dados-blog.js" defer></script>', '')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
            
    print("Sucesso! Páginas de blog geradas.")

if __name__ == "__main__":
    gerar_blog()
