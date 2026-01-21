import os
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
