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
import json
import datetime

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
    # --- SÃO PAULO (SP) ---
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
    {"nome": "Itapeva", "uf": "SP", "slug": "itapeva"},
    {"nome": "Mogi Mirim", "uf": "SP", "slug": "mogi-mirim"},
    {"nome": "São João da Boa Vista", "uf": "SP", "slug": "sao-joao-da-boa-vista"},
    {"nome": "Avaré", "uf": "SP", "slug": "avare"},
    {"nome": "Lorena", "uf": "SP", "slug": "lorena"},
    {"nome": "Ubatuba", "uf": "SP", "slug": "ubatuba"},
    {"nome": "Cajamar", "uf": "SP", "slug": "cajamar"},
    {"nome": "São Sebastião", "uf": "SP", "slug": "sao-sebastiao"},
    {"nome": "Arujá", "uf": "SP", "slug": "aruja"},
    {"nome": "Campo Limpo Paulista", "uf": "SP", "slug": "campo-limpo-paulista"},
    {"nome": "Bebedouro", "uf": "SP", "slug": "bebedouro"},
    {"nome": "São Roque", "uf": "SP", "slug": "sao-roque"},
    {"nome": "Cruzeiro", "uf": "SP", "slug": "cruzeiro"},
    {"nome": "Lins", "uf": "SP", "slug": "lins"},
    {"nome": "Jaboticabal", "uf": "SP", "slug": "jaboticabal"},
    {"nome": "Pirassununga", "uf": "SP", "slug": "pirassununga"},
    {"nome": "Vinhedo", "uf": "SP", "slug": "vinhedo"},
    {"nome": "Itapira", "uf": "SP", "slug": "itapira"},
    {"nome": "Amparo", "uf": "SP", "slug": "amparo"},
    {"nome": "Mococa", "uf": "SP", "slug": "mococa"},
    {"nome": "Fernandópolis", "uf": "SP", "slug": "fernandopolis"},
    {"nome": "Lençóis Paulista", "uf": "SP", "slug": "lencois-paulista"},
    {"nome": "Peruíbe", "uf": "SP", "slug": "peruibe"},
    {"nome": "Ibitinga", "uf": "SP", "slug": "ibitinga"},
    {"nome": "Registro", "uf": "SP", "slug": "registro"},
    {"nome": "Batatais", "uf": "SP", "slug": "batatais"},
    {"nome": "Bertioga", "uf": "SP", "slug": "bertioga"},
    {"nome": "Olímpia", "uf": "SP", "slug": "olimpia"},
    {"nome": "Andradina", "uf": "SP", "slug": "andradina"},
    {"nome": "Porto Ferreira", "uf": "SP", "slug": "porto-ferreira"},
    {"nome": "Capivari", "uf": "SP", "slug": "capivari"},
    {"nome": "Piedade", "uf": "SP", "slug": "piedade"},
    {"nome": "São José do Rio Pardo", "uf": "SP", "slug": "sao-jose-do-rio-pardo"},
    {"nome": "Jaguariúna", "uf": "SP", "slug": "jaguariuna"},
    {"nome": "Mongaguá", "uf": "SP", "slug": "mongagua"},
    {"nome": "Campos do Jordão", "uf": "SP", "slug": "campos-do-jordao"},
    {"nome": "Artur Nogueira", "uf": "SP", "slug": "artur-nogueira"},
    {"nome": "Itararé", "uf": "SP", "slug": "itarare"},
    {"nome": "Vargem Grande Paulista", "uf": "SP", "slug": "vargem-grande-paulista"},
    {"nome": "Rio Grande da Serra", "uf": "SP", "slug": "rio-grande-da-serra"},
    {"nome": "Serrana", "uf": "SP", "slug": "serrana"},
    {"nome": "Pontal", "uf": "SP", "slug": "pontal"},
    {"nome": "Jardinópolis", "uf": "SP", "slug": "jardinopolis"},
    {"nome": "Santa Cruz do Rio Pardo", "uf": "SP", "slug": "santa-cruz-do-rio-pardo"},
    {"nome": "Capão Bonito", "uf": "SP", "slug": "capao-bonito"},
    {"nome": "Dracena", "uf": "SP", "slug": "dracena"},
    {"nome": "Tremembé", "uf": "SP", "slug": "tremembe"},
    {"nome": "Pederneiras", "uf": "SP", "slug": "pederneiras"},
    {"nome": "Mairinque", "uf": "SP", "slug": "mairinque"},
    {"nome": "Salto de Pirapora", "uf": "SP", "slug": "salto-de-pirapora"},
    {"nome": "Pedreira", "uf": "SP", "slug": "pedreira"},
    {"nome": "Paraguaçu Paulista", "uf": "SP", "slug": "paraguacu-paulista"},
    {"nome": "Espírito Santo do Pinhal", "uf": "SP", "slug": "espirito-santo-do-pinhal"},
    {"nome": "Garça", "uf": "SP", "slug": "garca"},
    {"nome": "Presidente Epitácio", "uf": "SP", "slug": "presidente-epitacio"},
    {"nome": "Orlândia", "uf": "SP", "slug": "orlandia"},
    {"nome": "Itápolis", "uf": "SP", "slug": "itapolis"},
    {"nome": "Várzea Paulista", "uf": "SP", "slug": "varzea-paulista"},
    {"nome": "Tietê", "uf": "SP", "slug": "tiete"},
    {"nome": "Ituverava", "uf": "SP", "slug": "ituverava"},
    {"nome": "Novo Horizonte", "uf": "SP", "slug": "novo-horizonte"},
    {"nome": "São Manuel", "uf": "SP", "slug": "sao-manuel"},
    {"nome": "Guaíra", "uf": "SP", "slug": "guaira"},
    {"nome": "Promissão", "uf": "SP", "slug": "promissao"},
    {"nome": "Guararapes", "uf": "SP", "slug": "guararapes"},
    {"nome": "Presidente Venceslau", "uf": "SP", "slug": "presidente-venceslau"},
    {"nome": "Agudos", "uf": "SP", "slug": "agudos"},
    {"nome": "Adamantina", "uf": "SP", "slug": "adamantina"},
    {"nome": "Barra Bonita", "uf": "SP", "slug": "barra-bonita"},
    {"nome": "José Bonifácio", "uf": "SP", "slug": "jose-bonifacio"},
    {"nome": "Aparecida", "uf": "SP", "slug": "aparecida"},
    {"nome": "Cravinhos", "uf": "SP", "slug": "cravinhos"},
    {"nome": "São Pedro", "uf": "SP", "slug": "sao-pedro"},
    {"nome": "Descalvado", "uf": "SP", "slug": "descalvado"},
    {"nome": "Santa Rita do Passa Quatro", "uf": "SP", "slug": "santa-rita-do-passa-quatro"},
    {"nome": "Guariba", "uf": "SP", "slug": "guariba"},
    {"nome": "Iperó", "uf": "SP", "slug": "ipero"},
    {"nome": "São Joaquim da Barra", "uf": "SP", "slug": "sao-joaquim-da-barra"},
    {"nome": "Osvaldo Cruz", "uf": "SP", "slug": "osvaldo-cruz"},
    {"nome": "Santa Fé do Sul", "uf": "SP", "slug": "santa-fe-do-sul"},
    # --- RIO DE JANEIRO (RJ) ---
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
    {"nome": "Queimados", "uf": "RJ", "slug": "queimados"},
    {"nome": "Resende", "uf": "RJ", "slug": "resende"},
    {"nome": "Rio das Ostras", "uf": "RJ", "slug": "rio-das-ostras"},
    {"nome": "Araruama", "uf": "RJ", "slug": "araruama"},
    {"nome": "Arraial do Cabo", "uf": "RJ", "slug": "arraial-do-cabo"},
    {"nome": "São Pedro da Aldeia", "uf": "RJ", "slug": "sao-pedro-da-aldeia"},
    {"nome": "Itaperuna", "uf": "RJ", "slug": "itaperuna"},
    {"nome": "Japeri", "uf": "RJ", "slug": "japeri"},
    {"nome": "Barra do Piraí", "uf": "RJ", "slug": "barra-do-pirai"},
    {"nome": "Saquarema", "uf": "RJ", "slug": "saquarema"},
    {"nome": "Seropédica", "uf": "RJ", "slug": "seropedica"},
    {"nome": "Três Rios", "uf": "RJ", "slug": "tres-rios"},
    {"nome": "Valença", "uf": "RJ", "slug": "valenca"},
    {"nome": "Rio Bonito", "uf": "RJ", "slug": "rio-bonito"},
    {"nome": "Guapimirim", "uf": "RJ", "slug": "guapimirim"},
    {"nome": "Cachoeiras de Macacu", "uf": "RJ", "slug": "cachoeiras-de-macacu"},
    {"nome": "Paracambi", "uf": "RJ", "slug": "paracambi"},
    {"nome": "Paraíba do Sul", "uf": "RJ", "slug": "paraiba-do-sul"},
    {"nome": "Ilha Grande", "uf": "RJ", "slug": "ilha-grande"},
    {"nome": "Paraty", "uf": "RJ", "slug": "paraty"},
    # --- MINAS GERAIS (MG) ---
    {"nome": "Uberlândia", "uf": "MG", "slug": "uberlandia"},
    {"nome": "Contagem", "uf": "MG", "slug": "contagem"},
    {"nome": "Juiz de Fora", "uf": "MG", "slug": "juiz-de-fora"},
    {"nome": "Betim", "uf": "MG", "slug": "betim"},
    {"nome": "Montes Claros", "uf": "MG", "slug": "montes-claros"},
    {"nome": "Ribeirão das Neves", "uf": "MG", "slug": "ribeirao-das-neves"},
    {"nome": "Uberaba", "uf": "MG", "slug": "uberaba"},
    {"nome": "Governador Valadares", "uf": "MG", "slug": "governador-valadares"},
    {"nome": "Ipatinga", "uf": "MG", "slug": "ipatinga"},
    {"nome": "Sete Lagoas", "uf": "MG", "slug": "sete-lagoas"},
    {"nome": "Divinópolis", "uf": "MG", "slug": "divinopolis"},
    {"nome": "Santa Luzia", "uf": "MG", "slug": "santa-luzia"},
    {"nome": "Ibirité", "uf": "MG", "slug": "ibirite"},
    {"nome": "Poços de Caldas", "uf": "MG", "slug": "pocos-de-caldas"},
    {"nome": "Patos de Minas", "uf": "MG", "slug": "patos-de-minas"},
    {"nome": "Pouso Alegre", "uf": "MG", "slug": "pouso-alegre"},
    {"nome": "Teófilo Otoni", "uf": "MG", "slug": "teofilo-otoni"},
    {"nome": "Barbacena", "uf": "MG", "slug": "barbacena"},
    {"nome": "Sabará", "uf": "MG", "slug": "sabara"},
    {"nome": "Varginha", "uf": "MG", "slug": "varginha"},
    {"nome": "Conselheiro Lafaiete", "uf": "MG", "slug": "conselheiro-lafaiete"},
    {"nome": "Vespasiano", "uf": "MG", "slug": "vespasiano"},
    {"nome": "Itabira", "uf": "MG", "slug": "itabira"},
    {"nome": "Araguari", "uf": "MG", "slug": "araguari"},
    {"nome": "Passos", "uf": "MG", "slug": "passos"},
    {"nome": "Ubá", "uf": "MG", "slug": "uba"},
    {"nome": "Coronel Fabriciano", "uf": "MG", "slug": "coronel-fabriciano"},
    {"nome": "Muriaé", "uf": "MG", "slug": "muriae"},
    {"nome": "Ituiutaba", "uf": "MG", "slug": "ituiutaba"},
    {"nome": "Araxá", "uf": "MG", "slug": "araxa"},
    {"nome": "Lavras", "uf": "MG", "slug": "lavras"},
    {"nome": "Itajubá", "uf": "MG", "slug": "itajuba"},
    {"nome": "Itaúna", "uf": "MG", "slug": "itauna"},
    {"nome": "Pará de Minas", "uf": "MG", "slug": "para-de-minas"},
    {"nome": "Paracatu", "uf": "MG", "slug": "paracatu"},
    {"nome": "Caratinga", "uf": "MG", "slug": "caratinga"},
    {"nome": "Nova Lima", "uf": "MG", "slug": "nova-lima"},
    {"nome": "São João del Rei", "uf": "MG", "slug": "sao-joao-del-rei"},
    {"nome": "Patrocínio", "uf": "MG", "slug": "patrocinio"},
    {"nome": "Timóteo", "uf": "MG", "slug": "timoteo"},
    {"nome": "Manhuaçu", "uf": "MG", "slug": "manhuacu"},
    {"nome": "Unaí", "uf": "MG", "slug": "unai"},
    {"nome": "Curvelo", "uf": "MG", "slug": "curvelo"},
    {"nome": "Alfenas", "uf": "MG", "slug": "alfenas"},
    {"nome": "João Monlevade", "uf": "MG", "slug": "joao-monlevade"},
    {"nome": "Três Corações", "uf": "MG", "slug": "tres-coracoes"},
    {"nome": "Viçosa", "uf": "MG", "slug": "vicosa"},
    {"nome": "Cataguases", "uf": "MG", "slug": "cataguases"},
    {"nome": "Ouro Preto", "uf": "MG", "slug": "ouro-preto"},
    {"nome": "Janaúba", "uf": "MG", "slug": "janauba"},
    {"nome": "São Sebastião do Paraíso", "uf": "MG", "slug": "sao-sebastiao-do-paraiso"},
    {"nome": "Januária", "uf": "MG", "slug": "januaria"},
    {"nome": "Formiga", "uf": "MG", "slug": "formiga"},
    {"nome": "Esmeraldas", "uf": "MG", "slug": "esmeraldas"},
    {"nome": "Pedro Leopoldo", "uf": "MG", "slug": "pedro-leopoldo"},
    {"nome": "Ponte Nova", "uf": "MG", "slug": "ponte-nova"},
    {"nome": "Mariana", "uf": "MG", "slug": "mariana"},
    {"nome": "Frutal", "uf": "MG", "slug": "frutal"},
    {"nome": "Três Pontas", "uf": "MG", "slug": "tres-pontas"},
    # --- SANTA CATARINA (SC) ---
    {"nome": "Joinville", "uf": "SC", "slug": "joinville"},
    {"nome": "Blumenau", "uf": "SC", "slug": "blumenau"},
    {"nome": "São José", "uf": "SC", "slug": "sao-jose"},
    {"nome": "Chapecó", "uf": "SC", "slug": "chapeco"},
    {"nome": "Itajaí", "uf": "SC", "slug": "itajai"},
    {"nome": "Criciúma", "uf": "SC", "slug": "criciuma"},
    {"nome": "Jaraguá do Sul", "uf": "SC", "slug": "jaragua-do-sul"},
    {"nome": "Palhoça", "uf": "SC", "slug": "palhoca"},
    {"nome": "Lages", "uf": "SC", "slug": "lages"},
    {"nome": "Balneário Camboriú", "uf": "SC", "slug": "balneario-camboriu"},
    {"nome": "Brusque", "uf": "SC", "slug": "brusque"},
    {"nome": "Tubarão", "uf": "SC", "slug": "tubarao"},
    {"nome": "São Bento do Sul", "uf": "SC", "slug": "sao-bento-do-sul"},
    {"nome": "Camboriú", "uf": "SC", "slug": "camboriu"},
    {"nome": "Caçador", "uf": "SC", "slug": "cacador"},
    {"nome": "Navegantes", "uf": "SC", "slug": "navegantes"},
    {"nome": "Concórdia", "uf": "SC", "slug": "concordia"},
    {"nome": "Rio do Sul", "uf": "SC", "slug": "rio-do-sul"},
    {"nome": "Araranguá", "uf": "SC", "slug": "ararangua"},
    {"nome": "Gaspar", "uf": "SC", "slug": "gaspar"},
    {"nome": "Biguaçu", "uf": "SC", "slug": "biguacu"},
    {"nome": "Indaial", "uf": "SC", "slug": "indaial"},
    {"nome": "Itapema", "uf": "SC", "slug": "itapema"},
    {"nome": "Mafra", "uf": "SC", "slug": "mafra"},
    {"nome": "Canoinhas", "uf": "SC", "slug": "canoinhas"},
    {"nome": "Içara", "uf": "SC", "slug": "icara"},
    {"nome": "Videira", "uf": "SC", "slug": "videira"},
    {"nome": "Xanxerê", "uf": "SC", "slug": "xanxere"},
    {"nome": "São Francisco do Sul", "uf": "SC", "slug": "sao-francisco-do-sul"},
    # --- PARANÁ (PR) ---
    {"nome": "Londrina", "uf": "PR", "slug": "londrina"},
    {"nome": "Maringá", "uf": "PR", "slug": "maringa"},
    {"nome": "Ponta Grossa", "uf": "PR", "slug": "ponta-grossa"},
    {"nome": "Cascavel", "uf": "PR", "slug": "cascavel"},
    {"nome": "São José dos Pinhais", "uf": "PR", "slug": "sao-jose-dos-pinhais"},
    {"nome": "Foz do Iguaçu", "uf": "PR", "slug": "foz-do-iguacu"},
    {"nome": "Colombo", "uf": "PR", "slug": "colombo"},
    {"nome": "Guarapuava", "uf": "PR", "slug": "guarapuava"},
    {"nome": "Paranaguá", "uf": "PR", "slug": "paranagua"},
    {"nome": "Araucária", "uf": "PR", "slug": "araucaria"},
    {"nome": "Toledo", "uf": "PR", "slug": "toledo"},
    {"nome": "Apucarana", "uf": "PR", "slug": "apucarana"},
    {"nome": "Pinhais", "uf": "PR", "slug": "pinhais"},
    {"nome": "Campo Largo", "uf": "PR", "slug": "campo-largo"},
    {"nome": "Arapongas", "uf": "PR", "slug": "arapongas"},
    {"nome": "Almirante Tamandaré", "uf": "PR", "slug": "almirante-tamandare"},
    {"nome": "Umuarama", "uf": "PR", "slug": "umuarama"},
    {"nome": "Piraquara", "uf": "PR", "slug": "piraquara"},
    {"nome": "Cambé", "uf": "PR", "slug": "cambe"},
    {"nome": "Fazenda Rio Grande", "uf": "PR", "slug": "fazenda-rio-grande"},
    {"nome": "Sarandi", "uf": "PR", "slug": "sarandi"},
    {"nome": "Campo Mourão", "uf": "PR", "slug": "campo-mourao"},
    {"nome": "Francisco Beltrão", "uf": "PR", "slug": "francisco-beltrao"},
    {"nome": "Paranavaí", "uf": "PR", "slug": "paranavai"},
    {"nome": "Pato Branco", "uf": "PR", "slug": "pato-branco"},
    {"nome": "Cianorte", "uf": "PR", "slug": "cianorte"},
    {"nome": "Telêmaco Borba", "uf": "PR", "slug": "telemaco-borba"},
    {"nome": "Castro", "uf": "PR", "slug": "castro"},
    {"nome": "Rolândia", "uf": "PR", "slug": "rolandia"},
    {"nome": "Irati", "uf": "PR", "slug": "irati"},
    {"nome": "União da Vitória", "uf": "PR", "slug": "uniao-da-vitoria"},
    {"nome": "Marechal Cândido Rondon", "uf": "PR", "slug": "marechal-candido-rondon"},
    {"nome": "Ibiporã", "uf": "PR", "slug": "ibipora"},
    {"nome": "Prudentópolis", "uf": "PR", "slug": "prudentopolis"},
    {"nome": "Palmas", "uf": "PR", "slug": "palmas-pr"},
    {"nome": "Lapa", "uf": "PR", "slug": "lapa"},
    {"nome": "Cornélio Procópio", "uf": "PR", "slug": "cornelio-procopio"},
    {"nome": "Medianeira", "uf": "PR", "slug": "medianeira"},
    {"nome": "Dois Vizinhos", "uf": "PR", "slug": "dois-vizinhos"},
    # --- RIO GRANDE DO SUL (RS) ---
    {"nome": "Caxias do Sul", "uf": "RS", "slug": "caxias-do-sul"},
    {"nome": "Canoas", "uf": "RS", "slug": "canoas"},
    {"nome": "Pelotas", "uf": "RS", "slug": "pelotas"},
    {"nome": "Santa Maria", "uf": "RS", "slug": "santa-maria"},
    {"nome": "Gravataí", "uf": "RS", "slug": "gravatai"},
    {"nome": "Viamão", "uf": "RS", "slug": "viamao"},
    {"nome": "Novo Hamburgo", "uf": "RS", "slug": "novo-hamburgo"},
    {"nome": "São Leopoldo", "uf": "RS", "slug": "sao-leopoldo"},
    {"nome": "Rio Grande", "uf": "RS", "slug": "rio-grande"},
    {"nome": "Alvorada", "uf": "RS", "slug": "alvorada"},
    {"nome": "Passo Fundo", "uf": "RS", "slug": "passo-fundo"},
    {"nome": "Sapucaia do Sul", "uf": "RS", "slug": "sapucaia-do-sul"},
    {"nome": "Uruguaiana", "uf": "RS", "slug": "uruguaiana"},
    {"nome": "Santa Cruz do Sul", "uf": "RS", "slug": "santa-cruz-do-sul"},
    {"nome": "Cachoeirinha", "uf": "RS", "slug": "cachoeirinha"},
    {"nome": "Bagé", "uf": "RS", "slug": "bage"},
    {"nome": "Bento Gonçalves", "uf": "RS", "slug": "bento-goncalves"},
    {"nome": "Erechim", "uf": "RS", "slug": "erechim"},
    {"nome": "Guaíba", "uf": "RS", "slug": "guaiba"},
    {"nome": "Cachoeira do Sul", "uf": "RS", "slug": "cachoeira-do-sul"},
    {"nome": "Santana do Livramento", "uf": "RS", "slug": "santana-do-livramento"},
    {"nome": "Esteio", "uf": "RS", "slug": "esteio"},
    {"nome": "Ijuí", "uf": "RS", "slug": "ijui"},
    {"nome": "Santo Ângelo", "uf": "RS", "slug": "santo-angelo"},
    {"nome": "Alegrete", "uf": "RS", "slug": "alegrete"},
    {"nome": "Lajeado", "uf": "RS", "slug": "lajeado"},
    {"nome": "Farroupilha", "uf": "RS", "slug": "farroupilha"},
    {"nome": "Santa Rosa", "uf": "RS", "slug": "santa-rosa"},
    {"nome": "Venâncio Aires", "uf": "RS", "slug": "venancio-aires"},
    {"nome": "Campo Bom", "uf": "RS", "slug": "campo-bom"},
    {"nome": "Vacaria", "uf": "RS", "slug": "vacaria"},
    {"nome": "Cruz Alta", "uf": "RS", "slug": "cruz-alta"},
    {"nome": "Montenegro", "uf": "RS", "slug": "montenegro"},
    {"nome": "São Borja", "uf": "RS", "slug": "sao-borja"},
    {"nome": "São Gabriel", "uf": "RS", "slug": "sao-gabriel"},
    {"nome": "Carazinho", "uf": "RS", "slug": "carazinho"},
    {"nome": "Taquara", "uf": "RS", "slug": "taquara"},
    {"nome": "Camaquã", "uf": "RS", "slug": "camaqua"},
    {"nome": "Parobé", "uf": "RS", "slug": "parobe"},
    # --- BAHIA (BA) ---
    {"nome": "Feira de Santana", "uf": "BA", "slug": "feira-de-santana"},
    {"nome": "Vitória da Conquista", "uf": "BA", "slug": "vitoria-da-conquista"},
    {"nome": "Camaçari", "uf": "BA", "slug": "camacari"},
    {"nome": "Itabuna", "uf": "BA", "slug": "itabuna"},
    {"nome": "Juazeiro", "uf": "BA", "slug": "juazeiro"},
    {"nome": "Lauro de Freitas", "uf": "BA", "slug": "lauro-de-freitas"},
    {"nome": "Ilhéus", "uf": "BA", "slug": "ilheus"},
    {"nome": "Jequié", "uf": "BA", "slug": "jequie"},
    {"nome": "Teixeira de Freitas", "uf": "BA", "slug": "teixeira-de-freitas"},
    {"nome": "Barreiras", "uf": "BA", "slug": "barreiras"},
    {"nome": "Alagoinhas", "uf": "BA", "slug": "alagoinhas"},
    {"nome": "Porto Seguro", "uf": "BA", "slug": "porto-seguro"},
    {"nome": "Simões Filho", "uf": "BA", "slug": "simoes-filho"},
    {"nome": "Paulo Afonso", "uf": "BA", "slug": "paulo-afonso"},
    {"nome": "Eunápolis", "uf": "BA", "slug": "eunapolis"},
    {"nome": "Santo Antônio de Jesus", "uf": "BA", "slug": "santo-antonio-de-jesus"},
    {"nome": "Valença", "uf": "BA", "slug": "valenca"},
    {"nome": "Candeias", "uf": "BA", "slug": "candeias"},
    {"nome": "Guanambi", "uf": "BA", "slug": "guanambi"},
    {"nome": "Jacobina", "uf": "BA", "slug": "jacobina"},
    {"nome": "Serrinha", "uf": "BA", "slug": "serrinha"},
    {"nome": "Senhor do Bonfim", "uf": "BA", "slug": "senhor-do-bonfim"},
    {"nome": "Dias d'Ávila", "uf": "BA", "slug": "dias-davila"},
    {"nome": "Luís Eduardo Magalhães", "uf": "BA", "slug": "luis-eduardo-magalhaes"},
    {"nome": "Itapetinga", "uf": "BA", "slug": "itapetinga"},
    {"nome": "Irecê", "uf": "BA", "slug": "irece"},
    {"nome": "Campo Formoso", "uf": "BA", "slug": "campo-formoso"},
    {"nome": "Casa Nova", "uf": "BA", "slug": "casa-nova"},
    {"nome": "Bom Jesus da Lapa", "uf": "BA", "slug": "bom-jesus-da-lapa"},
    # --- ESPÍRITO SANTO (ES) ---
    {"nome": "Vila Velha", "uf": "ES", "slug": "vila-velha"},
    {"nome": "Serra", "uf": "ES", "slug": "serra"},
    {"nome": "Cariacica", "uf": "ES", "slug": "cariacica"},
    {"nome": "Cachoeiro de Itapemirim", "uf": "ES", "slug": "cachoeiro-de-itapemirim"},
    {"nome": "Linhares", "uf": "ES", "slug": "linhares"},
    {"nome": "São Mateus", "uf": "ES", "slug": "sao-mateus"},
    {"nome": "Colatina", "uf": "ES", "slug": "colatina"},
    {"nome": "Guarapari", "uf": "ES", "slug": "guarapari"},
    {"nome": "Aracruz", "uf": "ES", "slug": "aracruz"},
    {"nome": "Viana", "uf": "ES", "slug": "viana"},
    {"nome": "Nova Venécia", "uf": "ES", "slug": "nova-venecia"},
    {"nome": "Barra de São Francisco", "uf": "ES", "slug": "barra-de-sao-francisco"},
    {"nome": "Santa Maria de Jetibá", "uf": "ES", "slug": "santa-maria-de-jetiba"},
    {"nome": "Castelo", "uf": "ES", "slug": "castelo"},
    {"nome": "Marataízes", "uf": "ES", "slug": "marataizes"},
    {"nome": "São Gabriel da Palha", "uf": "ES", "slug": "sao-gabriel-da-palha"},
    # --- PERNAMBUCO (PE) ---
    {"nome": "Jaboatão dos Guararapes", "uf": "PE", "slug": "jaboatao-dos-guararapes"},
    {"nome": "Olinda", "uf": "PE", "slug": "olinda"},
    {"nome": "Caruaru", "uf": "PE", "slug": "caruaru"},
    {"nome": "Petrolina", "uf": "PE", "slug": "petrolina"},
    {"nome": "Paulista", "uf": "PE", "slug": "paulista"},
    {"nome": "Cabo de Santo Agostinho", "uf": "PE", "slug": "cabo-de-santo-agostinho"},
    {"nome": "Camaragibe", "uf": "PE", "slug": "camaragibe"},
    {"nome": "Garanhuns", "uf": "PE", "slug": "garanhuns"},
    {"nome": "Vitória de Santo Antão", "uf": "PE", "slug": "vitoria-de-santo-antao"},
    {"nome": "Igarassu", "uf": "PE", "slug": "igarassu"},
    {"nome": "São Lourenço da Mata", "uf": "PE", "slug": "sao-lourenco-da-mata"},
    {"nome": "Santa Cruz do Capibaribe", "uf": "PE", "slug": "santa-cruz-do-capibaribe"},
    {"nome": "Abreu e Lima", "uf": "PE", "slug": "abreu-e-lima"},
    {"nome": "Ipojuca", "uf": "PE", "slug": "ipojuca"},
    {"nome": "Serra Talhada", "uf": "PE", "slug": "serra-talhada"},
    {"nome": "Araripina", "uf": "PE", "slug": "araripina"},
    {"nome": "Gravatá", "uf": "PE", "slug": "gravata"},
    {"nome": "Carpina", "uf": "PE", "slug": "carpina"},
    {"nome": "Goiana", "uf": "PE", "slug": "goiana"},
    {"nome": "Belo Jardim", "uf": "PE", "slug": "belo-jardim"},
    # --- GOIÁS (GO) ---
    {"nome": "Aparecida de Goiânia", "uf": "GO", "slug": "aparecida-de-goiania"},
    {"nome": "Anápolis", "uf": "GO", "slug": "anapolis"},
    {"nome": "Rio Verde", "uf": "GO", "slug": "rio-verde"},
    {"nome": "Luziânia", "uf": "GO", "slug": "luziania"},
    {"nome": "Águas Lindas de Goiás", "uf": "GO", "slug": "aguas-lindas-de-goias"},
    {"nome": "Valparaíso de Goiás", "uf": "GO", "slug": "valparaiso-de-goias"},
    {"nome": "Trindade", "uf": "GO", "slug": "trindade"},
    {"nome": "Formosa", "uf": "GO", "slug": "formosa"},
    {"nome": "Novo Gama", "uf": "GO", "slug": "novo-gama"},
    {"nome": "Senador Canedo", "uf": "GO", "slug": "senador-canedo"},
    {"nome": "Itumbiara", "uf": "GO", "slug": "itumbiara"},
    {"nome": "Catalão", "uf": "GO", "slug": "catalao"},
    {"nome": "Jataí", "uf": "GO", "slug": "jatai"},
    {"nome": "Planaltina", "uf": "GO", "slug": "planaltina"},
    {"nome": "Caldas Novas", "uf": "GO", "slug": "caldas-novas"},
    {"nome": "Santo Antônio do Descoberto", "uf": "GO", "slug": "santo-antonio-do-descoberto"},
    {"nome": "Cidade Ocidental", "uf": "GO", "slug": "cidade-ocidental"},
    {"nome": "Goianésia", "uf": "GO", "slug": "goianesia"},
    {"nome": "Mineiros", "uf": "GO", "slug": "mineiros"},
    {"nome": "Cristalina", "uf": "GO", "slug": "cristalina"},
    # --- MATO GROSSO (MT) ---
    {"nome": "Várzea Grande", "uf": "MT", "slug": "varzea-grande"},
    {"nome": "Rondonópolis", "uf": "MT", "slug": "rondonopolis"},
    {"nome": "Sinop", "uf": "MT", "slug": "sinop"},
    {"nome": "Tangará da Serra", "uf": "MT", "slug": "tangara-da-serra"},
    {"nome": "Cáceres", "uf": "MT", "slug": "caceres"},
    {"nome": "Sorriso", "uf": "MT", "slug": "sorriso"},
    {"nome": "Lucas do Rio Verde", "uf": "MT", "slug": "lucas-do-rio-verde"},
    {"nome": "Primavera do Leste", "uf": "MT", "slug": "primavera-do-leste"},
    {"nome": "Barra do Garças", "uf": "MT", "slug": "barra-do-garcas"},
    {"nome": "Alta Floresta", "uf": "MT", "slug": "alta-floresta"},
    {"nome": "Pontes e Lacerda", "uf": "MT", "slug": "pontes-e-lacerda"},
    # --- MATO GROSSO DO SUL (MS) ---
    {"nome": "Dourados", "uf": "MS", "slug": "dourados"},
    {"nome": "Três Lagoas", "uf": "MS", "slug": "tres-lagoas"},
    {"nome": "Corumbá", "uf": "MS", "slug": "corumba"},
    {"nome": "Ponta Porã", "uf": "MS", "slug": "ponta-pora"},
    {"nome": "Sidrolândia", "uf": "MS", "slug": "sidrolandia"},
    {"nome": "Naviraí", "uf": "MS", "slug": "navirai"},
    {"nome": "Nova Andradina", "uf": "MS", "slug": "nova-andradina"},
    {"nome": "Aquidauana", "uf": "MS", "slug": "aquidauana"},
    {"nome": "Maracaju", "uf": "MS", "slug": "maracaju"},
    # --- PARAÍBA (PB) ---
    {"nome": "Campina Grande", "uf": "PB", "slug": "campina-grande"},
    {"nome": "Santa Rita", "uf": "PB", "slug": "santa-rita"},
    {"nome": "Patos", "uf": "PB", "slug": "patos"},
    {"nome": "Bayeux", "uf": "PB", "slug": "bayeux"},
    {"nome": "Sousa", "uf": "PB", "slug": "sousa"},
    {"nome": "Cabedelo", "uf": "PB", "slug": "cabedelo"},
    {"nome": "Cajazeiras", "uf": "PB", "slug": "cajazeiras"},
    {"nome": "Guarabira", "uf": "PB", "slug": "guarabira"},
    {"nome": "Sapé", "uf": "PB", "slug": "sape"},
    # --- RIO GRANDE DO NORTE (RN) ---
    {"nome": "Mossoró", "uf": "RN", "slug": "mossoro"},
    {"nome": "Parnamirim", "uf": "RN", "slug": "parnamirim"},
    {"nome": "São Gonçalo do Amarante", "uf": "RN", "slug": "sao-goncalo-do-amarante"},
    {"nome": "Ceará-Mirim", "uf": "RN", "slug": "ceara-mirim"},
    {"nome": "Macaíba", "uf": "RN", "slug": "macaiba"},
    {"nome": "Caicó", "uf": "RN", "slug": "caico"},
    {"nome": "Açu", "uf": "RN", "slug": "acu"},
    {"nome": "Currais Novos", "uf": "RN", "slug": "currais-novos"},
    {"nome": "São José de Mipibu", "uf": "RN", "slug": "sao-jose-de-mipibu"},
    # --- ALAGOAS (AL) ---
    {"nome": "Arapiraca", "uf": "AL", "slug": "arapiraca"},
    {"nome": "Rio Largo", "uf": "AL", "slug": "rio-largo"},
    {"nome": "Palmeira dos Índios", "uf": "AL", "slug": "palmeira-dos-indios"},
    # --- SERGIPE (SE) ---
    {"nome": "Nossa Senhora do Socorro", "uf": "SE", "slug": "nossa-senhora-do-socorro"},
    {"nome": "Lagarto", "uf": "SE", "slug": "lagarto"},
    {"nome": "Itabaiana", "uf": "SE", "slug": "itabaiana"},
    {"nome": "São Cristóvão", "uf": "SE", "slug": "sao-cristovao"},
    {"nome": "Estância", "uf": "SE", "slug": "estancia"},
    {"nome": "Tobias Barreto", "uf": "SE", "slug": "tobias-barreto"},
    # --- MARANHÃO (MA) ---
    {"nome": "Imperatriz", "uf": "MA", "slug": "imperatriz"},
    {"nome": "São José de Ribamar", "uf": "MA", "slug": "sao-jose-de-ribamar"},
    {"nome": "Timon", "uf": "MA", "slug": "timon"},
    {"nome": "Caxias", "uf": "MA", "slug": "caxias"},
    {"nome": "Paço do Lumiar", "uf": "MA", "slug": "paco-do-lumiar"},
    {"nome": "Codó", "uf": "MA", "slug": "codo"},
    {"nome": "Açailândia", "uf": "MA", "slug": "acailandia"},
    {"nome": "Bacabal", "uf": "MA", "slug": "bacabal"},
    {"nome": "Balsas", "uf": "MA", "slug": "balsas"},
    {"nome": "Santa Inês", "uf": "MA", "slug": "santa-ines"},
    {"nome": "Barra do Corda", "uf": "MA", "slug": "barra-do-corda"},
    {"nome": "Pinheiro", "uf": "MA", "slug": "pinheiro"},
    {"nome": "Chapadinha", "uf": "MA", "slug": "chapadinha"},
    {"nome": "Buriticupu", "uf": "MA", "slug": "buriticupu"},
    {"nome": "Grajaú", "uf": "MA", "slug": "grajau"},
    {"nome": "Itapecuru Mirim", "uf": "MA", "slug": "itapecuru-mirim"},
    {"nome": "Coroatá", "uf": "MA", "slug": "coroata"},
    # --- PIAUÍ (PI) ---
    {"nome": "Parnaíba", "uf": "PI", "slug": "parnaiba"},
    {"nome": "Picos", "uf": "PI", "slug": "picos"},
    {"nome": "Piripiri", "uf": "PI", "slug": "piripiri"},
    {"nome": "Floriano", "uf": "PI", "slug": "floriano"},
    {"nome": "Barras", "uf": "PI", "slug": "barras"},
    {"nome": "Campo Maior", "uf": "PI", "slug": "campo-maior"},
    {"nome": "União", "uf": "PI", "slug": "uniao"},
    {"nome": "Altos", "uf": "PI", "slug": "altos"},
    {"nome": "Esperantina", "uf": "PI", "slug": "esperantina"},
    # --- PARÁ (PA) ---
    {"nome": "Ananindeua", "uf": "PA", "slug": "ananindeua"},
    {"nome": "Santarém", "uf": "PA", "slug": "santarem"},
    {"nome": "Marabá", "uf": "PA", "slug": "maraba"},
    {"nome": "Parauapebas", "uf": "PA", "slug": "parauapebas"},
    {"nome": "Castanhal", "uf": "PA", "slug": "castanhal"},
    {"nome": "Abaetetuba", "uf": "PA", "slug": "abaetetuba"},
    {"nome": "Cametá", "uf": "PA", "slug": "cameta"},
    {"nome": "Marituba", "uf": "PA", "slug": "marituba"},
    {"nome": "Bragança", "uf": "PA", "slug": "braganca"},
    {"nome": "São Félix do Xingu", "uf": "PA", "slug": "sao-felix-do-xingu"},
    {"nome": "Barcarena", "uf": "PA", "slug": "barcarena"},
    {"nome": "Altamira", "uf": "PA", "slug": "altamira"},
    {"nome": "Tucuruí", "uf": "PA", "slug": "tucurui"},
    {"nome": "Paragominas", "uf": "PA", "slug": "paragominas"},
    {"nome": "Tailândia", "uf": "PA", "slug": "tailandia"},
    {"nome": "Breves", "uf": "PA", "slug": "breves"},
    {"nome": "Itaituba", "uf": "PA", "slug": "itaituba"},
    # --- RONDÔNIA (RO) ---
    {"nome": "Ji-Paraná", "uf": "RO", "slug": "ji-parana"},
    {"nome": "Ariquemes", "uf": "RO", "slug": "ariquemes"},
    {"nome": "Vilhena", "uf": "RO", "slug": "vilhena"},
    {"nome": "Cacoal", "uf": "RO", "slug": "cacoal"},
    {"nome": "Rolim de Moura", "uf": "RO", "slug": "rolim-de-moura"},
    {"nome": "Jaru", "uf": "RO", "slug": "jaru"},
    # --- TOCANTINS (TO) ---
    {"nome": "Araguaína", "uf": "TO", "slug": "araguaina"},
    {"nome": "Gurupi", "uf": "TO", "slug": "gurupi"},
    {"nome": "Porto Nacional", "uf": "TO", "slug": "porto-nacional"},
    {"nome": "Paraíso do Tocantins", "uf": "TO", "slug": "paraiso-do-tocantins"},
    # --- CEARÁ (CE) ---
    {"nome": "Caucaia", "uf": "CE", "slug": "caucaia"},
    {"nome": "Juazeiro do Norte", "uf": "CE", "slug": "juazeiro-do-norte"},
    {"nome": "Maracanaú", "uf": "CE", "slug": "maracanau"},
    {"nome": "Sobral", "uf": "CE", "slug": "sobral"},
    {"nome": "Crato", "uf": "CE", "slug": "crato"},
    {"nome": "Itapipoca", "uf": "CE", "slug": "itapipoca"},
    {"nome": "Maranguape", "uf": "CE", "slug": "maranguape"},
    {"nome": "Iguatu", "uf": "CE", "slug": "iguatu"},
    {"nome": "Quixadá", "uf": "CE", "slug": "quixada"},
    {"nome": "Pacatuba", "uf": "CE", "slug": "pacatuba"},
    {"nome": "Aquiraz", "uf": "CE", "slug": "aquiraz"},
    {"nome": "Quixeramobim", "uf": "CE", "slug": "quixeramobim"},
    {"nome": "Canindé", "uf": "CE", "slug": "caninde"},
    {"nome": "Russas", "uf": "CE", "slug": "russas"},
    {"nome": "Crateús", "uf": "CE", "slug": "crateus"},
    {"nome": "Tianguá", "uf": "CE", "slug": "tiangua"},
    {"nome": "Aracati", "uf": "CE", "slug": "aracati"},
    {"nome": "Cascavel", "uf": "CE", "slug": "cascavel-ce"},
    {"nome": "Pacajus", "uf": "CE", "slug": "pacajus"},
    # --- OUTROS ---
    {"nome": "Cruzeiro do Sul", "uf": "AC", "slug": "cruzeiro-do-sul"},
    {"nome": "Parintins", "uf": "AM", "slug": "parintins"},
    {"nome": "Itacoatiara", "uf": "AM", "slug": "itacoatiara"},
    {"nome": "Manacapuru", "uf": "AM", "slug": "manacapuru"},
    {"nome": "Santana", "uf": "AP", "slug": "santana"},
    {"nome": "Rorainópolis", "uf": "RR", "slug": "rorainopolis"},
    # --- NOVAS ADIÇÕES (Para chegar a 600+) ---
    # SP
    {"nome": "Tupã", "uf": "SP", "slug": "tupa"},
    {"nome": "Penápolis", "uf": "SP", "slug": "penapolis"},
    {"nome": "Nova Odessa", "uf": "SP", "slug": "nova-odessa"},
    {"nome": "Monte Mor", "uf": "SP", "slug": "monte-mor"},
    {"nome": "Santa Isabel", "uf": "SP", "slug": "santa-isabel"},
    {"nome": "Boituva", "uf": "SP", "slug": "boituva"},
    {"nome": "Ibiúna", "uf": "SP", "slug": "ibiuna"},
    {"nome": "Cosmópolis", "uf": "SP", "slug": "cosmopolis"},
    # MG
    {"nome": "Almenara", "uf": "MG", "slug": "almenara"},
    {"nome": "Leopoldina", "uf": "MG", "slug": "leopoldina"},
    {"nome": "Santos Dumont", "uf": "MG", "slug": "santos-dumont"},
    {"nome": "Monte Carmelo", "uf": "MG", "slug": "monte-carmelo"},
    {"nome": "São Francisco", "uf": "MG", "slug": "sao-francisco"},
    {"nome": "Guaxupé", "uf": "MG", "slug": "guaxupe"},
    {"nome": "Bocaiuva", "uf": "MG", "slug": "bocaiuva"},
    {"nome": "Lagoa da Prata", "uf": "MG", "slug": "lagoa-da-prata"},
    {"nome": "Além Paraíba", "uf": "MG", "slug": "alem-paraiba"},
    {"nome": "Oliveira", "uf": "MG", "slug": "oliveira"},
    {"nome": "Boa Esperança", "uf": "MG", "slug": "boa-esperanca"},
    {"nome": "João Pinheiro", "uf": "MG", "slug": "joao-pinheiro"},
    {"nome": "Caeté", "uf": "MG", "slug": "caete"},
    {"nome": "Piumhi", "uf": "MG", "slug": "piumhi"},
    {"nome": "Santa Rita do Sapucaí", "uf": "MG", "slug": "santa-rita-do-sapucai"},
    {"nome": "Visconde do Rio Branco", "uf": "MG", "slug": "visconde-do-rio-branco"},
    {"nome": "Machado", "uf": "MG", "slug": "machado"},
    {"nome": "Andradas", "uf": "MG", "slug": "andradas"},
    {"nome": "Arcos", "uf": "MG", "slug": "arcos"},
    {"nome": "Iturama", "uf": "MG", "slug": "iturama"},
    {"nome": "Matozinhos", "uf": "MG", "slug": "matozinhos"},
    {"nome": "São Gotardo", "uf": "MG", "slug": "sao-gotardo"},
    {"nome": "Brumadinho", "uf": "MG", "slug": "brumadinho"},
    {"nome": "Ouro Branco", "uf": "MG", "slug": "ouro-branco"},
    {"nome": "Capelinha", "uf": "MG", "slug": "capelinha"},
    {"nome": "Araçuaí", "uf": "MG", "slug": "aracuai"},
    {"nome": "Jaíba", "uf": "MG", "slug": "jaiba"},
    {"nome": "Pompéu", "uf": "MG", "slug": "pompeu"},
    {"nome": "Carangola", "uf": "MG", "slug": "carangola"},
    {"nome": "Ouro Fino", "uf": "MG", "slug": "ouro-fino"},
    {"nome": "Três Marias", "uf": "MG", "slug": "tres-marias"},
    {"nome": "Sarzedo", "uf": "MG", "slug": "sarzedo"},
    {"nome": "Mateus Leme", "uf": "MG", "slug": "mateus-leme"},
    {"nome": "São Lourenço", "uf": "MG", "slug": "sao-lourenco"},
    {"nome": "Campo Belo", "uf": "MG", "slug": "campo-belo"},
    # RJ
    {"nome": "Itaguaí", "uf": "RJ", "slug": "itaguai"},
    {"nome": "São Fidélis", "uf": "RJ", "slug": "sao-fidelis"},
    {"nome": "Mangaratiba", "uf": "RJ", "slug": "mangaratiba"},
    {"nome": "Casimiro de Abreu", "uf": "RJ", "slug": "casimiro-de-abreu"},
    {"nome": "Santo Antônio de Pádua", "uf": "RJ", "slug": "santo-antonio-de-padua"},
    {"nome": "São Francisco de Itabapoana", "uf": "RJ", "slug": "sao-francisco-de-itabapoana"},
    {"nome": "Bom Jesus do Itabapoana", "uf": "RJ", "slug": "bom-jesus-do-itabapoana"},
    {"nome": "Vassouras", "uf": "RJ", "slug": "vassouras"},
    {"nome": "Tanguá", "uf": "RJ", "slug": "tangua"},
    {"nome": "Itatiaia", "uf": "RJ", "slug": "itatiaia"},
    {"nome": "Piraí", "uf": "RJ", "slug": "pirai"},
    {"nome": "Paty do Alferes", "uf": "RJ", "slug": "paty-do-alferes"},
    {"nome": "Miracema", "uf": "RJ", "slug": "miracema"},
    {"nome": "Iguaba Grande", "uf": "RJ", "slug": "iguaba-grande"},
    # BA
    {"nome": "Brumado", "uf": "BA", "slug": "brumado"},
    {"nome": "Conceição do Coité", "uf": "BA", "slug": "conceicao-do-coite"},
    {"nome": "Itamaraju", "uf": "BA", "slug": "itamaraju"},
    {"nome": "Itaberaba", "uf": "BA", "slug": "itaberaba"},
    {"nome": "Cruz das Almas", "uf": "BA", "slug": "cruz-das-almas"},
    {"nome": "Ipirá", "uf": "BA", "slug": "ipira"},
    {"nome": "Santo Amaro", "uf": "BA", "slug": "santo-amaro"},
    {"nome": "Euclides da Cunha", "uf": "BA", "slug": "euclides-da-cunha"},
    {"nome": "Tucano", "uf": "BA", "slug": "tucano"},
    {"nome": "Araci", "uf": "BA", "slug": "araci"},
    {"nome": "Catu", "uf": "BA", "slug": "catu"},
    {"nome": "Jaguaquara", "uf": "BA", "slug": "jaguaquara"},
    {"nome": "Ribeira do Pombal", "uf": "BA", "slug": "ribeira-do-pombal"},
    {"nome": "Poções", "uf": "BA", "slug": "pocoes"},
    {"nome": "Barra do Choça", "uf": "BA", "slug": "barra-do-choca"},
    {"nome": "Seabra", "uf": "BA", "slug": "seabra"},
    {"nome": "Xique-Xique", "uf": "BA", "slug": "xique-xique"},
    {"nome": "Livramento de Nossa Senhora", "uf": "BA", "slug": "livramento-de-nossa-senhora"},
    {"nome": "Caetité", "uf": "BA", "slug": "caetite"},
    {"nome": "Macaúbas", "uf": "BA", "slug": "macaubas"},
    {"nome": "Mata de São João", "uf": "BA", "slug": "mata-de-sao-joao"},
    {"nome": "Ipiaú", "uf": "BA", "slug": "ipiau"},
    {"nome": "Monte Santo", "uf": "BA", "slug": "monte-santo"},
    # RS
    {"nome": "Canguçu", "uf": "RS", "slug": "cangucu"},
    {"nome": "Santiago", "uf": "RS", "slug": "santiago"},
    {"nome": "Tramandaí", "uf": "RS", "slug": "tramandai"},
    {"nome": "Osório", "uf": "RS", "slug": "osorio"},
    {"nome": "Canela", "uf": "RS", "slug": "canela"},
    {"nome": "Panambi", "uf": "RS", "slug": "panambi"},
    {"nome": "Santo Antônio da Patrulha", "uf": "RS", "slug": "santo-antonio-da-patrulha"},
    {"nome": "São Luiz Gonzaga", "uf": "RS", "slug": "sao-luiz-gonzaga"},
    {"nome": "Marau", "uf": "RS", "slug": "marau"},
    {"nome": "Rosário do Sul", "uf": "RS", "slug": "rosario-do-sul"},
    {"nome": "Itaqui", "uf": "RS", "slug": "itaqui"},
    {"nome": "São José do Norte", "uf": "RS", "slug": "sao-jose-do-norte"},
    {"nome": "Torres", "uf": "RS", "slug": "torres"},
    {"nome": "Caçapava do Sul", "uf": "RS", "slug": "cacapava-do-sul"},
    {"nome": "Dom Pedrito", "uf": "RS", "slug": "dom-pedrito"},
    {"nome": "Garibaldi", "uf": "RS", "slug": "garibaldi"},
    {"nome": "Encantado", "uf": "RS", "slug": "encantado"},
    {"nome": "Estância Velha", "uf": "RS", "slug": "estancia-velha"},
    {"nome": "Igrejinha", "uf": "RS", "slug": "igrejinha"},
    # PR
    {"nome": "Santo Antônio da Platina", "uf": "PR", "slug": "santo-antonio-da-platina"},
    {"nome": "Paiçandu", "uf": "PR", "slug": "paicandu"},
    {"nome": "São Mateus do Sul", "uf": "PR", "slug": "sao-mateus-do-sul"},
    {"nome": "Jacarezinho", "uf": "PR", "slug": "jacarezinho"},
    {"nome": "Rio Negro", "uf": "PR", "slug": "rio-negro"},
    {"nome": "Jaguariaíva", "uf": "PR", "slug": "jaguariaiva"},
    {"nome": "Mandaguari", "uf": "PR", "slug": "mandaguari"},
    {"nome": "Guaíra", "uf": "PR", "slug": "guaira-pr"},
    {"nome": "Quedas do Iguaçu", "uf": "PR", "slug": "quedas-do-iguacu"},
    {"nome": "Marialva", "uf": "PR", "slug": "marialva"},
    {"nome": "Imbituva", "uf": "PR", "slug": "imbituva"},
    {"nome": "Palmeira", "uf": "PR", "slug": "palmeira"},
    {"nome": "Assis Chateaubriand", "uf": "PR", "slug": "assis-chateaubriand"},
    {"nome": "Rio Branco do Sul", "uf": "PR", "slug": "rio-branco-do-sul"},
    {"nome": "Laranjeiras do Sul", "uf": "PR", "slug": "laranjeiras-do-sul"},
    {"nome": "Pinhão", "uf": "PR", "slug": "pinhao"},
    # SC
    {"nome": "Laguna", "uf": "SC", "slug": "laguna"},
    {"nome": "Imbituba", "uf": "SC", "slug": "imbituba"},
    {"nome": "São Miguel do Oeste", "uf": "SC", "slug": "sao-miguel-do-oeste"},
    {"nome": "Curitibanos", "uf": "SC", "slug": "curitibanos"},
    {"nome": "Fraiburgo", "uf": "SC", "slug": "fraiburgo"},
    {"nome": "Timbó", "uf": "SC", "slug": "timbo"},
    {"nome": "São João Batista", "uf": "SC", "slug": "sao-joao-batista"},
    {"nome": "Braço do Norte", "uf": "SC", "slug": "braco-do-norte"},
    {"nome": "Pomerode", "uf": "SC", "slug": "pomerode"},
    {"nome": "Penha", "uf": "SC", "slug": "penha"},
    {"nome": "Sombrio", "uf": "SC", "slug": "sombrio"},
    {"nome": "Joaçaba", "uf": "SC", "slug": "joacaba"},
    {"nome": "Xaxim", "uf": "SC", "slug": "xaxim"},
    {"nome": "Campos Novos", "uf": "SC", "slug": "campos-novos"},
    {"nome": "Forquilhinha", "uf": "SC", "slug": "forquilhinha"},
    {"nome": "Porto União", "uf": "SC", "slug": "porto-uniao"},
    # PE
    {"nome": "Arcoverde", "uf": "PE", "slug": "arcoverde"},
    {"nome": "Ouricuri", "uf": "PE", "slug": "ouricuri"},
    {"nome": "Escada", "uf": "PE", "slug": "escada"},
    {"nome": "Pesqueira", "uf": "PE", "slug": "pesqueira"},
    {"nome": "Surubim", "uf": "PE", "slug": "surubim"},
    {"nome": "Palmares", "uf": "PE", "slug": "palmares"},
    {"nome": "Bezerros", "uf": "PE", "slug": "bezerros"},
    {"nome": "Moreno", "uf": "PE", "slug": "moreno"},
    {"nome": "São Bento do Una", "uf": "PE", "slug": "sao-bento-do-una"},
    {"nome": "Buíque", "uf": "PE", "slug": "buique"},
    {"nome": "Limoeiro", "uf": "PE", "slug": "limoeiro"},
    {"nome": "Brejo da Madre de Deus", "uf": "PE", "slug": "brejo-da-madre-de-deus"},
    # CE
    {"nome": "Icó", "uf": "CE", "slug": "ico"},
    {"nome": "Morada Nova", "uf": "CE", "slug": "morada-nova"},
    {"nome": "Camocim", "uf": "CE", "slug": "camocim"},
    {"nome": "Acaraú", "uf": "CE", "slug": "acarau"},
    {"nome": "Viçosa do Ceará", "uf": "CE", "slug": "vicosa-do-ceara"},
    {"nome": "Barbalha", "uf": "CE", "slug": "barbalha"},
    {"nome": "Limoeiro do Norte", "uf": "CE", "slug": "limoeiro-do-norte"},
    {"nome": "Tauá", "uf": "CE", "slug": "taua"},
    {"nome": "Trairi", "uf": "CE", "slug": "trairi"},
    {"nome": "Granja", "uf": "CE", "slug": "granja"},
    {"nome": "Boa Viagem", "uf": "CE", "slug": "boa-viagem"},
    {"nome": "Acopiara", "uf": "CE", "slug": "acopiara"},
    {"nome": "Beberibe", "uf": "CE", "slug": "beberibe"},
    {"nome": "Eusébio", "uf": "CE", "slug": "eusebio"},
    {"nome": "Itaitinga", "uf": "CE", "slug": "itaitinga"},
    # GO
    {"nome": "Inhumas", "uf": "GO", "slug": "inhumas"},
    {"nome": "Jaraguá", "uf": "GO", "slug": "jaragua"},
    {"nome": "Quirinópolis", "uf": "GO", "slug": "quirinopolis"},
    {"nome": "Niquelândia", "uf": "GO", "slug": "niquelandia"},
    {"nome": "Porangatu", "uf": "GO", "slug": "porangatu"},
    {"nome": "Morrinhos", "uf": "GO", "slug": "morrinhos"},
    {"nome": "Itaberaí", "uf": "GO", "slug": "itaberai"},
    {"nome": "Uruaçu", "uf": "GO", "slug": "uruacu"},
    {"nome": "Santa Helena de Goiás", "uf": "GO", "slug": "santa-helena-de-goias"},
    {"nome": "Posse", "uf": "GO", "slug": "posse"},
    {"nome": "Goiatuba", "uf": "GO", "slug": "goiatuba"},
    {"nome": "São Luís de Montes Belos", "uf": "GO", "slug": "sao-luis-de-montes-belos"},
    {"nome": "Iporá", "uf": "GO", "slug": "ipora"},
    {"nome": "Pires do Rio", "uf": "GO", "slug": "pires-do-rio"},
    # ES
    {"nome": "Domingos Martins", "uf": "ES", "slug": "domingos-martins"},
    {"nome": "Itapemirim", "uf": "ES", "slug": "itapemirim"},
    {"nome": "Afonso Cláudio", "uf": "ES", "slug": "afonso-claudio"},
    {"nome": "Alegre", "uf": "ES", "slug": "alegre"},
    {"nome": "Baixo Guandu", "uf": "ES", "slug": "baixo-guandu"},
    {"nome": "Conceição da Barra", "uf": "ES", "slug": "conceicao-da-barra"},
    {"nome": "Guaçuí", "uf": "ES", "slug": "guacui"},
    {"nome": "Iúna", "uf": "ES", "slug": "iuna"},
    {"nome": "Jaguaré", "uf": "ES", "slug": "jaguare"},
    {"nome": "Mimoso do Sul", "uf": "ES", "slug": "mimoso-do-sul"},
    {"nome": "Sooretama", "uf": "ES", "slug": "sooretama"},
    # MT
    {"nome": "Nova Mutum", "uf": "MT", "slug": "nova-mutum"},
    {"nome": "Campo Novo do Parecis", "uf": "MT", "slug": "campo-novo-do-parecis"},
    {"nome": "Juína", "uf": "MT", "slug": "juina"},
    {"nome": "Juara", "uf": "MT", "slug": "juara"},
    {"nome": "Peixoto de Azevedo", "uf": "MT", "slug": "peixoto-de-azevedo"},
    {"nome": "Colniza", "uf": "MT", "slug": "colniza"},
    {"nome": "Guarantã do Norte", "uf": "MT", "slug": "guaranta-do-norte"},
    # MS
    {"nome": "Paranaíba", "uf": "MS", "slug": "paranaiba"},
    {"nome": "Amambai", "uf": "MS", "slug": "amambai"},
    {"nome": "Rio Brilhante", "uf": "MS", "slug": "rio-brilhante"},
    {"nome": "Coxim", "uf": "MS", "slug": "coxim"},
    {"nome": "Caarapó", "uf": "MS", "slug": "caarapo"},
    {"nome": "Miranda", "uf": "MS", "slug": "miranda"},
    # PA
    {"nome": "Redenção", "uf": "PA", "slug": "redencao"},
    {"nome": "Moju", "uf": "PA", "slug": "moju"},
    {"nome": "Novo Repartimento", "uf": "PA", "slug": "novo-repartimento"},
    {"nome": "Oriximiná", "uf": "PA", "slug": "oriximina"},
    {"nome": "Capanema", "uf": "PA", "slug": "capanema"},
    {"nome": "Santa Izabel do Pará", "uf": "PA", "slug": "santa-izabel-do-para"},
    {"nome": "Breu Branco", "uf": "PA", "slug": "breu-branco"},
    {"nome": "Tomé-Açu", "uf": "PA", "slug": "tome-acu"},
    {"nome": "Igarapé-Miri", "uf": "PA", "slug": "igarape-miri"},
    {"nome": "Viseu", "uf": "PA", "slug": "viseu"},
    # MA
    {"nome": "Barreirinhas", "uf": "MA", "slug": "barreirinhas"},
    {"nome": "Tutóia", "uf": "MA", "slug": "tutoia"},
    {"nome": "Vargem Grande", "uf": "MA", "slug": "vargem-grande"},
    {"nome": "Coelho Neto", "uf": "MA", "slug": "coelho-neto"},
    {"nome": "Presidente Dutra", "uf": "MA", "slug": "presidente-dutra"},
    {"nome": "Araioses", "uf": "MA", "slug": "araioses"},
    {"nome": "São Bento", "uf": "MA", "slug": "sao-bento"},
    {"nome": "Santa Luzia", "uf": "MA", "slug": "santa-luzia-ma"},
    {"nome": "Zé Doca", "uf": "MA", "slug": "ze-doca"},
    # PB
    {"nome": "Mamanguape", "uf": "PB", "slug": "mamanguape"},
    {"nome": "Queimadas", "uf": "PB", "slug": "queimadas"},
    {"nome": "São Bento", "uf": "PB", "slug": "sao-bento-pb"},
    {"nome": "Monteiro", "uf": "PB", "slug": "monteiro"},
    {"nome": "Esperança", "uf": "PB", "slug": "esperanca"},
    {"nome": "Pombal", "uf": "PB", "slug": "pombal"},
    {"nome": "Catolé do Rocha", "uf": "PB", "slug": "catole-do-rocha"},
    {"nome": "Alagoa Grande", "uf": "PB", "slug": "alagoa-grande"},
    # RN
    {"nome": "Santa Cruz", "uf": "RN", "slug": "santa-cruz"},
    {"nome": "Nova Cruz", "uf": "RN", "slug": "nova-cruz"},
    {"nome": "Apodi", "uf": "RN", "slug": "apodi"},
    {"nome": "João Câmara", "uf": "RN", "slug": "joao-camara"},
    {"nome": "Canguaretama", "uf": "RN", "slug": "canguaretama"},
    {"nome": "Touros", "uf": "RN", "slug": "touros"},
    {"nome": "Macau", "uf": "RN", "slug": "macau"},
    # AL
    {"nome": "União dos Palmares", "uf": "AL", "slug": "uniao-dos-palmares"},
    {"nome": "Penedo", "uf": "AL", "slug": "penedo"},
    {"nome": "São Miguel dos Campos", "uf": "AL", "slug": "sao-miguel-dos-campos"},
    {"nome": "Coruripe", "uf": "AL", "slug": "coruripe"},
    {"nome": "Campo Alegre", "uf": "AL", "slug": "campo-alegre"},
    {"nome": "Delmiro Gouveia", "uf": "AL", "slug": "delmiro-gouveia"},
    {"nome": "Marechal Deodoro", "uf": "AL", "slug": "marechal-deodoro"},
    {"nome": "Santana do Ipanema", "uf": "AL", "slug": "santana-do-ipanema"},
    {"nome": "Atalaia", "uf": "AL", "slug": "atalaia"},
    {"nome": "Teotônio Vilela", "uf": "AL", "slug": "teotonio-vilela"},
    # SE
    {"nome": "Simão Dias", "uf": "SE", "slug": "simao-dias"},
    {"nome": "Itabaianinha", "uf": "SE", "slug": "itabaianinha"},
    {"nome": "Poço Verde", "uf": "SE", "slug": "poco-verde"},
    {"nome": "Capela", "uf": "SE", "slug": "capela"},
    {"nome": "Nossa Senhora da Glória", "uf": "SE", "slug": "nossa-senhora-da-gloria"},
    {"nome": "Propriá", "uf": "SE", "slug": "propria"},
    # PI
    {"nome": "José de Freitas", "uf": "PI", "slug": "jose-de-freitas"},
    {"nome": "Pedro II", "uf": "PI", "slug": "pedro-ii"},
    {"nome": "Oeiras", "uf": "PI", "slug": "oeiras"},
    {"nome": "São Raimundo Nonato", "uf": "PI", "slug": "sao-raimundo-nonato"},
    {"nome": "Miguel Alves", "uf": "PI", "slug": "miguel-alves"},
    {"nome": "Luís Correia", "uf": "PI", "slug": "luis-correia"},
    # RO
    {"nome": "Guajará-Mirim", "uf": "RO", "slug": "guajara-mirim"},
    {"nome": "Ouro Preto do Oeste", "uf": "RO", "slug": "ouro-preto-do-oeste"},
    {"nome": "Pimenta Bueno", "uf": "RO", "slug": "pimenta-bueno"},
    {"nome": "Buritis", "uf": "RO", "slug": "buritis"},
    # TO
    {"nome": "Colinas do Tocantins", "uf": "TO", "slug": "colinas-do-tocantins"},
    {"nome": "Guaraí", "uf": "TO", "slug": "guarai"},
    # AM
    {"nome": "Coari", "uf": "AM", "slug": "coari"},
    {"nome": "Tefé", "uf": "AM", "slug": "tefe"},
    {"nome": "Tabatinga", "uf": "AM", "slug": "tabatinga"},
    {"nome": "Maués", "uf": "AM", "slug": "maues"},
    # AP
    {"nome": "Laranjal do Jari", "uf": "AP", "slug": "laranjal-do-jari"},
    # AC
    {"nome": "Sena Madureira", "uf": "AC", "slug": "sena-madureira"},
    {"nome": "Tarauacá", "uf": "AC", "slug": "tarauaca"},
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
    
    # Correção para evitar "Sim! Sim!"
    template = template.replace('Sim! Atendemos empresas de todos os estados do Brasil de forma 100% remota', 'Sim! Atendemos empresas de [[CIDADE]] de forma 100% remota')
    # Fallback caso o texto seja diferente
    template = template.replace('Atendemos empresas de todos os estados do Brasil de forma 100% remota', 'Atendemos empresas de [[CIDADE]] de forma 100% remota')
    
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
        "Criação de sites modernos e otimizados para o Google para empresas de [[CIDADE]].",
        "Transforme visitantes em clientes com um site exclusivo para sua empresa em [[CIDADE]].",
        "Aumente sua autoridade em [[CIDADE]] com um site profissional e veloz.",
        "Web design focado em conversão para negócios locais de [[CIDADE]].",
        "Sua empresa em [[CIDADE]] merece um site que vende 24 horas por dia.",
        "Sua marca em destaque em [[CIDADE]] com um site de alta conversão.",
        "Conquiste o mercado de [[CIDADE]] com tecnologia web de ponta.",
        "Sites que carregam rápido e vendem mais para o público de [[CIDADE]].",
        "Acelere o crescimento da sua empresa em [[CIDADE]] com um site otimizado.",
        "Não perca mais clientes em [[CIDADE]]. Tenha um site profissional hoje.",
        "Destaque-se da concorrência em [[CIDADE]] com um design exclusivo.",
        "Sites institucionais e lojas virtuais para empresas de [[CIDADE]].",
        "A melhor solução em criação de sites para o mercado de [[CIDADE]].",
        "Tenha um site que funciona e vende para seu público em [[CIDADE]].",
        "Desenvolvimento web sob medida para negócios de [[CIDADE]].",
        "Sua vitrine digital em [[CIDADE]] aberta 24 horas por dia.",
        "Atraia mais clientes qualificados em [[CIDADE]] com SEO local.",
        "Tecnologia e design unidos para impulsionar seu negócio em [[CIDADE]]."
    ]
    
    variacoes_cta = [
        "Quero um Site Profissional", "Solicitar Orçamento Agora", "Aumentar Minhas Vendas", 
        "Falar com Especialista", "Pedir Cotação", "Começar Agora", "Quero Vender Mais",
        "Solicitar Proposta", "Ver Planos Disponíveis", "Quero Crescer Online", "Fale Conosco"
    ]
    
    variacoes_atendimento = [
        "Atendimento especializado em [[CIDADE]]", "Suporte dedicado para empresas de [[CIDADE]]", 
        "Soluções digitais em [[CIDADE]]", "Parceiro digital em [[CIDADE]]", "Consultoria web em [[CIDADE]]",
        "Agência focada em [[CIDADE]]", "Desenvolvimento web para [[CIDADE]]", "Seu parceiro de tecnologia em [[CIDADE]]"
    ]
    
    variacoes_titulo_extra = [
        "Por que sua empresa em [[CIDADE]] precisa de um site?", "Destaque-se no mercado de [[CIDADE]]", 
        "Aumente suas vendas em [[CIDADE]]", "Domine o Google em [[CIDADE]]", "Como crescer seu negócio em [[CIDADE]]",
        "A importância de um site para empresas de [[CIDADE]]", "Saia na frente da concorrência em [[CIDADE]]"
    ]
    
    variacoes_texto_extra = [
        "O mercado em <strong>[[CIDADE]]</strong> está cada vez mais digital. Ter um site otimizado garante que sua empresa seja encontrada.",
        "Não deixe seu negócio fora do mapa digital de <strong>[[CIDADE]]</strong> (DDD [[DDD]]). A internet é sua maior vitrine.",
        "Empresas de <strong>[[CIDADE]]</strong> que não estão na internet estão perdendo dinheiro. Um site rápido é a chave para captar novos clientes.",
        "Em <strong>[[CIDADE]]</strong>, a concorrência está online. Garanta seu espaço com uma presença digital forte e profissional.",
        "Seus clientes em <strong>[[CIDADE]]</strong> estão buscando no Google agora. Sua empresa aparece lá? Nós resolvemos isso.",
        "Para se destacar em <strong>[[CIDADE]]</strong>, você precisa de mais que um cartão de visitas. Precisa de uma máquina de vendas online.",
        "Aumente a credibilidade da sua marca em <strong>[[CIDADE]]</strong> com um site que transmite confiança e profissionalismo."
    ]

    variacoes_servicos_titulo = [
        "Soluções digitais para seu negócio",
        "Nossos serviços especializados",
        "Como posso ajudar sua empresa",
        "O que oferecemos para você", 
        "Estratégias para o seu crescimento",
        "Serviços de alta performance",
        "O que fazemos por você",
        "Tecnologia para o seu sucesso"
    ]

    variacoes_servicos_subtitulo = [
        "Estruturas otimizadas para captar leads e gerar oportunidades de negócio.",
        "Tecnologia de ponta para destacar sua marca no mercado digital.",
        "Desenvolvimento focado em resultados reais e aumento de faturamento.",
        "Não entrego apenas \"um site\". Entrego uma ferramenta de vendas pronta para o Google.",
        "Sites rápidos, seguros e preparados para converter visitantes em clientes.",
        "Soluções completas, do design ao código, focadas na experiência do usuário."
    ]

    # --- NOVAS VARIAÇÕES PARA SEO (ANTI-SPAM) ---
    variacoes_meta = [
        "Criação de sites profissionais e Landing Pages para empresas de [[CIDADE]]. Desenvolvimento web de alta performance, SEO e tráfego pago. Peça seu orçamento!",
        "Procurando Criação de Sites em [[CIDADE]]? Desenvolvemos sites rápidos e otimizados para o Google. Aumente suas vendas hoje!",
        "Agência de Criação de Sites focada em [[CIDADE]]. Sites Institucionais e Lojas Virtuais que convertem visitantes em clientes.",
        "Desenvolvimento de Sites Profissionais em [[CIDADE]]. Tenha um site moderno, responsivo e pronto para SEO. Solicite um orçamento.",
        "Especialistas em Web Design e SEO em [[CIDADE]]. Transforme sua presença digital com um site que vende 24h por dia.",
        "Empresa de desenvolvimento de sites em [[CIDADE]]. Criamos sites rápidos, seguros e otimizados para o Google. Solicite seu orçamento agora!",
        "Melhore a presença digital da sua empresa em [[CIDADE]]. Sites profissionais, Landing Pages e E-commerce. Resultados reais.",
        "Especialistas em criação de sites e SEO em [[CIDADE]]. Aumente sua visibilidade e vendas com um site de alta performance.",
        "Seu negócio em [[CIDADE]] precisa de um site profissional. Desenvolvemos soluções web personalizadas para você.",
        "Criação de sites em [[CIDADE]] com foco em vendas. Design moderno e tecnologia de ponta para destacar sua marca."
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

        # Variações de Serviços para evitar conteúdo duplicado
        conteudo = conteudo.replace("Soluções digitais para seu negócio", random.choice(variacoes_servicos_titulo))
        conteudo = conteudo.replace("Estruturas otimizadas para captar leads e gerar oportunidades de negócio.", random.choice(variacoes_servicos_subtitulo))

        # 1. Variação da Meta Description (Crucial para o Google)
        meta_content = random.choice(variacoes_meta).replace('[[CIDADE]]', local['nome'])
        # Substitui a meta tag inteira para garantir que pegue a versão correta
        conteudo = re.sub(r'<meta name="description" content="[^"]+">', f'<meta name="description" content="{meta_content}">', conteudo)

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
    run_step("verificar_site.py")

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

# --- 4. CONTEÚDO DE GERAR_SITEMAP.PY ---
code_sitemap = r'''import os
import glob
import datetime

# Configurações
BASE_URL = "https://www.cybernexinnovatech.com.br"
SITEMAP_FILE = "sitemap.xml"

def gerar_sitemap():
    print("--- Gerando Sitemap.xml ---")
    
    today = datetime.date.today().isoformat()
    urls = []
    
    # 1. Home
    urls.append({"loc": f"{BASE_URL}/", "priority": "1.00"})
    
    # 2. Cobertura
    if os.path.exists("cobertura.html"):
        urls.append({"loc": f"{BASE_URL}/cobertura.html", "priority": "0.80"})

    # 3. Cidades
    for arq in glob.glob("criacao-de-sites-em-*.html"):
        urls.append({"loc": f"{BASE_URL}/{os.path.basename(arq)}", "priority": "0.80"})
        
    # 4. Segmentos
    for arq in glob.glob("site-para-*.html"):
        urls.append({"loc": f"{BASE_URL}/{os.path.basename(arq)}", "priority": "0.90"})

    # 5. Blog
    for arq in glob.glob("artigo-*.html"):
        urls.append({"loc": f"{BASE_URL}/{os.path.basename(arq)}", "priority": "0.80"})

    # Gerar XML
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls:
        xml_content += f'  <url>\n    <loc>{url["loc"]}</loc>\n    <lastmod>{today}</lastmod>\n    <priority>{url["priority"]}</priority>\n  </url>\n'
    xml_content += '</urlset>'
    
    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(xml_content)
    print(f"✅ Sitemap gerado com {len(urls)} URLs.")

if __name__ == "__main__":
    gerar_sitemap()
'''

# --- 5. CONTEÚDO DE VERIFICAR_SITE.PY ---
code_verificar = r'''import os
import glob

def verificar():
    print("\n--- 🕵️‍♂️ Verificação Final do Site ---")
    
    # 1. Verificar se as páginas foram geradas
    paginas = glob.glob("criacao-de-sites-em-*.html")
    print(f"✅ Páginas de cidades encontradas: {len(paginas)}")
    
    if len(paginas) == 0:
        print("❌ ERRO: Nenhuma página de cidade foi gerada!")
        return

    # 2. Verificar conteúdo de uma página aleatória
    amostra = paginas[0]
    with open(amostra, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    erros = []
    if "[[CIDADE]]" in conteudo:
        erros.append("Placeholder [[CIDADE]] não foi substituído.")
    if "Sim! Sim!" in conteudo:
        erros.append("Texto duplicado 'Sim! Sim!' encontrado.")
    if "<title>Cybernex Innovatech - Criação de Sites para Todo o Brasil</title>" in conteudo:
        erros.append("Título da página não foi alterado.")
        
    if erros:
        print(f"❌ ERROS ENCONTRADOS em {amostra}:")
        for erro in erros:
            print(f"   - {erro}")
    else:
        print(f"✅ Verificação de conteúdo em {amostra}: OK")
        
    # 3. Verificar Sitemap
    if os.path.exists("sitemap.xml"):
        with open("sitemap.xml", 'r', encoding='utf-8') as f:
            sitemap = f.read()
            urls = sitemap.count("<loc>")
            print(f"✅ Sitemap gerado com {urls} URLs.")
    else:
        print("❌ Sitemap.xml não encontrado.")

if __name__ == "__main__":
    verificar()
'''

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
    
    # Reescreve gerar_sitemap.py
    with open('gerar_sitemap.py', 'w', encoding='utf-8') as f:
        f.write(code_sitemap)
    print("✅ gerar_sitemap.py restaurado.")

    # Reescreve verificar_site.py
    with open('verificar_site.py', 'w', encoding='utf-8') as f:
        f.write(code_verificar)
    print("✅ verificar_site.py criado.")

    print("\n--- 🚀 Iniciando execução... ---")
    try:
        subprocess.run([sys.executable, 'gerar_tudo.py'], check=True)
    except Exception as e:
        print(f"Erro ao rodar: {e}")

if __name__ == "__main__":
    reparar()
