import os
import sys
import subprocess
import time
import webbrowser
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

# --- 0. CONTEÚDO DE SEO_BOOSTER.PY (Estratégia Nacional & QA) ---
code_seo_booster = r'''import json
import os
import re

# --- Configurações do Site ---
BASE_URL = "https://www.cybernexinnovatech.com.br"
BUSINESS_NAME = "Cybernex Innovatech"
LOGO_URL = f"{BASE_URL}/logo.webp"
CONTACT_PHONE = "+5511976678655"

# --- Dados para JSON-LD ---
SERVICES = [
    "Criação de Sites Institucionais",
    "Landing Pages de Alta Conversão",
    "E-commerce e Lojas Virtuais",
    "Consultoria SEO Especializada",
    "Otimização de Performance (Core Web Vitals)"
]

FAQ_ITEMS = [
    {
        "question": "Quanto tempo demora para criar um site?",
        "answer": "Landing Pages levam de 5 a 7 dias úteis. Sites institucionais completos, cerca de 15 a 20 dias."
    },
    {
        "question": "O site é meu ou pago mensalidade?",
        "answer": "O site é 100% seu. Não cobramos aluguel. Você paga apenas uma vez pelo desenvolvimento."
    },
    {
        "question": "Vocês fazem otimização para o Google (SEO)?",
        "answer": "Sim! Todos os nossos sites são entregues com estrutura otimizada para SEO técnico e performance."
    }
]

def generate_json_ld():
    organization_schema = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": BUSINESS_NAME,
        "image": LOGO_URL,
        "@id": BASE_URL,
        "url": BASE_URL,
        "telephone": CONTACT_PHONE,
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "São Paulo",
            "addressRegion": "SP",
            "addressCountry": "BR"
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": -23.550520,
            "longitude": -46.633308
        },
        "areaServed": {
            "@type": "Country",
            "name": "Brasil"
        },
        "knowsAbout": [
            "Web Development", "SEO", "Digital Marketing", "E-commerce", "QA Automation", "Performance Tuning"
        ],
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "09:00",
            "closes": "18:00"
        },
        "sameAs": [
            "https://www.instagram.com/cybernexinnovatech",
            "https://www.linkedin.com/company/cybernex"
        ],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Serviços Web",
            "itemListElement": []
        }
    }
    for service in SERVICES:
        organization_schema["hasOfferCatalog"]["itemListElement"].append({
            "@type": "Offer", "itemOffered": { "@type": "Service", "name": service }
        })

    faq_schema = { "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [] }
    for item in FAQ_ITEMS:
        faq_schema["mainEntity"].append({
            "@type": "Question", "name": item["question"], "acceptedAnswer": { "@type": "Answer", "text": item["answer"] }
        })

    website_schema = {
        "@context": "https://schema.org", "@type": "WebSite", "name": BUSINESS_NAME, "url": BASE_URL,
        "potentialAction": { "@type": "SearchAction", "target": f"{BASE_URL}/search?q={{search_term_string}}", "query-input": "required name=search_term_string" }
    }

    return { "@context": "https://schema.org", "@graph": [organization_schema, faq_schema, website_schema] }

def inject_into_html(json_data):
    html_file = 'index.html'
    if not os.path.exists(html_file): return

    with open(html_file, 'r', encoding='utf-8') as f: content = f.read()

    # --- ATUALIZAÇÃO ESTRATÉGICA (QA & Performance) ---
    content = content.replace('<h3>Landing Pages</h3>', '<h3>LPs de Alta Performance</h3>')
    content = content.replace('<p>Páginas de alta conversão focadas em vender um produto ou serviço específico. Ideais para tráfego pago.</p>', '<p>Landing Pages para Infoprodutores e Lançamentos. Foco total em taxa de conversão e velocidade de carregamento.</p>')
    
    content = content.replace('<h3>Hospedagem & Manutenção</h3>', '<h3>Manutenção & QA (Quality Assurance)</h3>')
    content = content.replace('<p>Tranquilidade total. Mantenho seu site no ar, seguro e atualizado com planos mensais acessíveis.</p>', '<p>Inclui testes de regressão, auditoria de bugs e validação de performance mensal. Seu site sempre impecável.</p>')
    
    content = content.replace('<h3>CRM & Gestão Financeira</h3>', '<h3>Sistemas CRM Personalizados</h3>')
    content = content.replace('<p>Sistemas personalizados para gestão de clientes e controle financeiro. Visualize seus dados em tempo real.</p>', '<p>CRM sob medida superior aos de mercado. Gestão de clientes e financeiro com foco na sua regra de negócio.</p>')

    # Limpeza e Injeção JSON-LD
    content = re.sub(r'<!-- SEO AUTOMÁTICO: JSON-LD -->\s*', '', content)
    content = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', content, flags=re.DOTALL)
    content = content.replace('G-SEU_ID_AQUI', 'G-XQ3E4D0VRJ')

    json_string = json.dumps(json_data, indent=2, ensure_ascii=False)
    new_script = f'\n    <!-- SEO AUTOMÁTICO: JSON-LD -->\n    <script type="application/ld+json">\n{json_string}\n    </script>\n'
    
    if '</head>' in content:
        content = content.replace('</head>', f'{new_script}</head>')
        with open(html_file, 'w', encoding='utf-8') as f: f.write(content)

if __name__ == "__main__":
    inject_into_html(generate_json_ld())
'''

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
    # --- CAPITAIS ---
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
    # --- INTERIOR SP ---
    {"nome": "Guarulhos", "uf": "SP", "slug": "guarulhos"},
    {"nome": "Campinas", "uf": "SP", "slug": "campinas"},
    {"nome": "São Bernardo do Campo", "uf": "SP", "slug": "sao-bernardo-do-campo"},
    {"nome": "Santo André", "uf": "SP", "slug": "santo-andre"},
    {"nome": "São José dos Campos", "uf": "SP", "slug": "sao-jose-dos-campos"},
    {"nome": "Osasco", "uf": "SP", "slug": "osasco"},
    {"nome": "Ribeirão Preto", "uf": "SP", "slug": "ribeirao-preto"},
    {"nome": "Sorocaba", "uf": "SP", "slug": "sorocaba"},
    {"nome": "Mauá", "uf": "SP", "slug": "maua"},
    {"nome": "São José do Rio Preto", "uf": "SP", "slug": "sao-jose-do-rio-preto"},
    {"nome": "Santos", "uf": "SP", "slug": "santos"},
    {"nome": "Mogi das Cruzes", "uf": "SP", "slug": "mogi-das-cruzes"},
    {"nome": "Diadema", "uf": "SP", "slug": "diadema"},
    {"nome": "Jundiaí", "uf": "SP", "slug": "jundiai"},
    {"nome": "Carapicuíba", "uf": "SP", "slug": "carapicuiba"},
    {"nome": "Piracicaba", "uf": "SP", "slug": "piracicaba"},
    {"nome": "Bauru", "uf": "SP", "slug": "bauru"},
    {"nome": "São Vicente", "uf": "SP", "slug": "sao-vicente"},
    {"nome": "Itaquaquecetuba", "uf": "SP", "slug": "itaquaquecetuba"},
    {"nome": "Franca", "uf": "SP", "slug": "franca"},
    {"nome": "Guarujá", "uf": "SP", "slug": "guaruja"},
    {"nome": "Taubaté", "uf": "SP", "slug": "taubate"},
    {"nome": "Limeira", "uf": "SP", "slug": "limeira"},
    {"nome": "Praia Grande", "uf": "SP", "slug": "praia-grande"},
    {"nome": "Suzano", "uf": "SP", "slug": "suzano"},
    {"nome": "Taboão da Serra", "uf": "SP", "slug": "taboao-da-serra"},
    {"nome": "Sumaré", "uf": "SP", "slug": "sumare"},
    {"nome": "Barueri", "uf": "SP", "slug": "barueri"},
    {"nome": "Embu das Artes", "uf": "SP", "slug": "embu-das-artes"},
    {"nome": "São Carlos", "uf": "SP", "slug": "sao-carlos"},
    {"nome": "Marília", "uf": "SP", "slug": "marilia"},
    {"nome": "Americana", "uf": "SP", "slug": "americana"},
    {"nome": "Indaiatuba", "uf": "SP", "slug": "indaiatuba"},
    {"nome": "Cotia", "uf": "SP", "slug": "cotia"},
    {"nome": "Jacareí", "uf": "SP", "slug": "jacarei"},
    {"nome": "Araraquara", "uf": "SP", "slug": "araraquara"},
    {"nome": "Presidente Prudente", "uf": "SP", "slug": "presidente-prudente"},
    {"nome": "Itapevi", "uf": "SP", "slug": "itapevi"},
    {"nome": "Hortolândia", "uf": "SP", "slug": "hortolandia"},
    {"nome": "Rio Claro", "uf": "SP", "slug": "rio-claro"},
    {"nome": "Araçatuba", "uf": "SP", "slug": "aracatuba"},
    {"nome": "Santa Bárbara d'Oeste", "uf": "SP", "slug": "santa-barbara-doeste"},
    {"nome": "Ferraz de Vasconcelos", "uf": "SP", "slug": "ferraz-de-vasconcelos"},
    {"nome": "Francisco Morato", "uf": "SP", "slug": "francisco-morato"},
    {"nome": "Itapecerica da Serra", "uf": "SP", "slug": "itapecerica-da-serra"},
    {"nome": "Itu", "uf": "SP", "slug": "itu"},
    {"nome": "Bragança Paulista", "uf": "SP", "slug": "braganca-paulista"},
    {"nome": "Pindamonhangaba", "uf": "SP", "slug": "pindamonhangaba"},
    {"nome": "Itapetininga", "uf": "SP", "slug": "itapetininga"},
    {"nome": "São Caetano do Sul", "uf": "SP", "slug": "sao-caetano-do-sul"},
    {"nome": "Mogi Guaçu", "uf": "SP", "slug": "mogi-guacu"},
    {"nome": "Franco da Rocha", "uf": "SP", "slug": "franco-da-rocha"},
    {"nome": "Jaú", "uf": "SP", "slug": "jau"},
    {"nome": "Botucatu", "uf": "SP", "slug": "botucatu"},
    {"nome": "Atibaia", "uf": "SP", "slug": "atibaia"},
    {"nome": "Araras", "uf": "SP", "slug": "araras"},
    {"nome": "Cubatão", "uf": "SP", "slug": "cubatao"},
    {"nome": "Sertãozinho", "uf": "SP", "slug": "sertaozinho"},
    {"nome": "Valinhos", "uf": "SP", "slug": "valinhos"},
    {"nome": "Ribeirão Pires", "uf": "SP", "slug": "ribeirao-pires"},
    {"nome": "Barretos", "uf": "SP", "slug": "barretos"},
    {"nome": "Catanduva", "uf": "SP", "slug": "catanduva"},
    {"nome": "Jandira", "uf": "SP", "slug": "jandira"},
    {"nome": "Birigui", "uf": "SP", "slug": "birigui"},
    {"nome": "Guaratinguetá", "uf": "SP", "slug": "guaratingueta"},
    {"nome": "Votorantim", "uf": "SP", "slug": "votorantim"},
    {"nome": "Tatuí", "uf": "SP", "slug": "tatui"},
    {"nome": "Salto", "uf": "SP", "slug": "salto"},
    {"nome": "Poá", "uf": "SP", "slug": "poa"},
    {"nome": "Santana de Parnaíba", "uf": "SP", "slug": "santana-de-parnaiba"},
    {"nome": "Itatiba", "uf": "SP", "slug": "itatiba"},
    {"nome": "Ourinhos", "uf": "SP", "slug": "ourinhos"},
    {"nome": "Assis", "uf": "SP", "slug": "assis"},
    {"nome": "Leme", "uf": "SP", "slug": "leme"},
    {"nome": "Paulínia", "uf": "SP", "slug": "paulinia"},
    {"nome": "Caieiras", "uf": "SP", "slug": "caieiras"},
    {"nome": "Mairiporã", "uf": "SP", "slug": "mairipora"},
    {"nome": "Itanhaém", "uf": "SP", "slug": "itanhaem"},
    {"nome": "Caçapava", "uf": "SP", "slug": "cacapava"},
    {"nome": "Votuporanga", "uf": "SP", "slug": "votuporanga"},
    # --- RJ ---
    {"nome": "São Gonçalo", "uf": "RJ", "slug": "sao-goncalo"},
    {"nome": "Duque de Caxias", "uf": "RJ", "slug": "duque-de-caxias"},
    {"nome": "Nova Iguaçu", "uf": "RJ", "slug": "nova-iguacu"},
    {"nome": "Niterói", "uf": "RJ", "slug": "niteroi"},
    {"nome": "Belford Roxo", "uf": "RJ", "slug": "belford-roxo"},
    {"nome": "Campos dos Goytacazes", "uf": "RJ", "slug": "campos-dos-goytacazes"},
    {"nome": "São João de Meriti", "uf": "RJ", "slug": "sao-joao-de-meriti"},
    {"nome": "Petrópolis", "uf": "RJ", "slug": "petropolis"},
    {"nome": "Volta Redonda", "uf": "RJ", "slug": "volta-redonda"},
    {"nome": "Magé", "uf": "RJ", "slug": "mage"},
    {"nome": "Macaé", "uf": "RJ", "slug": "macae"},
    {"nome": "Itaboraí", "uf": "RJ", "slug": "itaborai"},
    {"nome": "Cabo Frio", "uf": "RJ", "slug": "cabo-frio"},
    {"nome": "Nova Friburgo", "uf": "RJ", "slug": "nova-friburgo"},
    {"nome": "Angra dos Reis", "uf": "RJ", "slug": "angra-dos-reis"},
    {"nome": "Barra Mansa", "uf": "RJ", "slug": "barra-mansa"},
    {"nome": "Teresópolis", "uf": "RJ", "slug": "teresopolis"},
    {"nome": "Mesquita", "uf": "RJ", "slug": "mesquita"},
    {"nome": "Nilópolis", "uf": "RJ", "slug": "nilopolis"},
    {"nome": "Maricá", "uf": "RJ", "slug": "marica"},
    # --- MG ---
    {"nome": "Uberlândia", "uf": "MG", "slug": "uberlandia"},
    {"nome": "Contagem", "uf": "MG", "slug": "contagem"},
    {"nome": "Juiz de Fora", "uf": "MG", "slug": "juiz-de-fora"},
    {"nome": "Betim", "uf": "MG", "slug": "betim"},
    # --- SC/PR/RS ---
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
    
    # CORREÇÃO H1: Usa o texto exato do index.html atual
    template = template.replace('>Criação de Sites<', '>Criação de Sites em [[CIDADE]]<')
    template = template.replace('data-text="Criação de Sites"', 'data-text="Criação de Sites em [[CIDADE]]"')
    
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

        # CORREÇÃO JSON-LD: Garante que substitui Brasil ou Brazil
        conteudo = conteudo.replace('"name": "Brasil"', f'"name": "{local["nome"]} - {local["uf"]}"')
        conteudo = conteudo.replace('"name": "Brazil"', f'"name": "{local["nome"]} - {local["uf"]}"')
        conteudo = conteudo.replace('"@type": "Country"', '"@type": "City"')
        
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
    template_seg = template_seg.replace('>Criação de Sites<', '>Sites para [[SEGMENTO_PLURAL]]<')
    template_seg = template_seg.replace('data-text="Criação de Sites"', 'data-text="Sites para [[SEGMENTO_PLURAL]]"')
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
    
    run_step("seo_booster.py") # Executa primeiro para atualizar o index.html
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
    
    # Reescreve seo_booster.py (Novo)
    with open('seo_booster.py', 'w', encoding='utf-8') as f:
        f.write(code_seo_booster)
    print("✅ seo_booster.py restaurado.")
    
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
