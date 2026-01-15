import json
import os
import re

# --- Configurações do Site ---
BASE_URL = "https://www.cybernexinnovatech.com.br"
BUSINESS_NAME = "Cybernex Innovatech"
LOGO_URL = f"{BASE_URL}/logo.png"
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
    """Gera os dados estruturados (Rich Snippets) em formato JSON."""
    
    # 1. Schema de Organização (LocalBusiness/ProfessionalService)
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
            "name": "Brazil"
        },
        "knowsAbout": [
            "Web Development",
            "SEO",
            "Digital Marketing",
            "E-commerce"
        ],
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": [
                "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
            ],
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

    # Adiciona serviços ao catálogo
    for service in SERVICES:
        organization_schema["hasOfferCatalog"]["itemListElement"].append({
            "@type": "Offer",
            "itemOffered": {
                "@type": "Service",
                "name": service
            }
        })

    # 2. Schema de FAQ
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }

    for item in FAQ_ITEMS:
        faq_schema["mainEntity"].append({
            "@type": "Question",
            "name": item["question"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": item["answer"]
            }
        })

    # 3. Schema de WebSite (Sitelinks Search Box)
    website_schema = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": BUSINESS_NAME,
        "url": BASE_URL,
        "potentialAction": {
            "@type": "SearchAction",
            "target": f"{BASE_URL}/search?q={{search_term_string}}",
            "query-input": "required name=search_term_string"
        }
    }

    # Retorna usando @graph para agrupar múltiplos schemas em um único JSON-LD
    return {
        "@context": "https://schema.org",
        "@graph": [
            organization_schema,
            faq_schema,
            website_schema
        ]
    }

def inject_into_html(json_data):
    """Injeta o JSON-LD diretamente no index.html, substituindo os antigos."""
    html_file = 'index.html'
    
    if not os.path.exists(html_file):
        print(f"[ERRO] {html_file} não encontrado.")
        return

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Criar Backup
    with open('index_backup.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("[OK] Backup criado: index_backup.html")

    # 2. Remover scripts JSON-LD antigos (limpeza)
    # Remove qualquer bloco <script type="application/ld+json">...</script> existente
    content = re.sub(r'<script type="application/ld\+json">.*?</script>', '', content, flags=re.DOTALL)
    
    # 3. Preparar o novo bloco de script
    json_string = json.dumps(json_data, indent=2, ensure_ascii=False)
    new_script = f'\n    <!-- SEO AUTOMÁTICO: JSON-LD -->\n    <script type="application/ld+json">\n{json_string}\n    </script>\n'

    # 4. Inserir antes do fechamento do </head>
    if '</head>' in content:
        content = content.replace('</head>', f'{new_script}</head>')
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("[SUCESSO] index.html atualizado automaticamente com SEO!")
    else:
        print("[ERRO] Tag </head> não encontrada no HTML.")

def main():
    print("--- Iniciando Otimizador de SEO Cybernex ---")
    
    # 1. Gerar JSON-LD
    data = generate_json_ld()
    
    # 2. Injetar no HTML
    inject_into_html(data)

if __name__ == "__main__":
    main()