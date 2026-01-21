import json
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
