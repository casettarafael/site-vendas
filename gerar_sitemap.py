import datetime

# Configurações
BASE_URL = "https://www.cybernexinnovatech.com.br"

# Lista de Locais (Mesma do seu site)
locais = [
    # Capitais
    "rio-branco", "maceio", "macapa", "manaus", "salvador", "fortaleza", 
    "brasilia", "vitoria", "goiania", "sao-luis", "cuiaba", "campo-grande", 
    "belo-horizonte", "belem", "joao-pessoa", "curitiba", "recife", "teresina", 
    "rio-de-janeiro", "natal", "porto-alegre", "porto-velho", "boa-vista", 
    "florianopolis", "sao-paulo", "aracaju", "palmas",
    # SP
    "guarulhos", "campinas", "sao-bernardo-do-campo", "santo-andre", "sao-jose-dos-campos", "osasco", "ribeirao-preto", "sorocaba", "maua", "sao-jose-do-rio-preto", "santos", "mogi-das-cruzes", "diadema", "jundiai", "carapicuiba", "piracicaba", "bauru", "sao-vicente", "itaquaquecetuba", "franca", "guaruja", "taubate", "limeira", "praia-grande", "suzano", "taboao-da-serra", "sumare", "barueri", "embu-das-artes", "sao-carlos", "marilia", "americana", "indaiatuba", "cotia", "jacarei", "araraquara", "presidente-prudente", "itapevi", "hortolandia", "rio-claro", "aracatuba", "santa-barbara-doeste", "ferraz-de-vasconcelos", "francisco-morato", "itapecerica-da-serra", "itu", "braganca-paulista", "pindamonhangaba", "itapetininga", "sao-caetano-do-sul", "mogi-guacu", "franco-da-rocha", "jau", "botucatu", "atibaia", "araras", "cubatao", "sertaozinho", "valinhos", "ribeirao-pires", "barretos", "catanduva", "jandira", "birigui", "guaratingueta", "votorantim", "tatui", "salto", "poa", "santana-de-parnaiba", "itatiba", "ourinhos", "assis", "leme", "paulinia", "caieiras", "mairipora", "itanhaem", "cacapava", "votuporanga",
    # RJ
    "sao-goncalo", "duque-de-caxias", "nova-iguacu", "niteroi", "belford-roxo", "campos-dos-goytacazes", "sao-joao-de-meriti", "petropolis", "volta-redonda", "mage", "macae", "itaborai", "cabo-frio", "nova-friburgo", "angra-dos-reis", "barra-mansa", "teresopolis", "mesquita", "nilopolis", "marica", "queimados", "resende", "rio-das-ostras", "araruama", "arraial-do-cabo", "sao-pedro-da-aldeia", "itaperuna", "japeri", "barra-do-pirai", "ilha-grande", "paraty",
    # MG
    "uberlandia", "contagem", "juiz-de-fora", "betim", "montes-claros", "ribeirao-das-neves", "uberaba", "governador-valadares", "ipatinga", "sete-lagoas", "divinopolis", "santa-luzia", "ibirite", "pocos-de-caldas", "patos-de-minas", "pouso-alegre", "teofilo-otoni", "barbacena", "sabara", "varginha", "conselheiro-lafaiete", "vespasiano", "itabira", "araguari", "passos", "coronel-fabriciano", "muriae", "uba", "ituiutaba", "araxa", "lavras", "itajuba", "nova-lima", "manhuacu", "sao-joao-del-rei", "para-de-minas", "itauna", "patrocinio", "caratinga", "timoteo",
    # RS
    "caxias-do-sul", "pelotas", "canoas", "santa-maria", "gravatai", "viamao", "novo-hamburgo", "sao-leopoldo", "rio-grande", "alvorada", "passo-fundo", "sapucaia-do-sul", "uruguaiana", "santa-cruz-do-sul", "cachoeirinha", "bage", "bento-goncalves", "erechim", "guaiba", "cachoeira-do-sul", "esteio", "ijui",
    # PR
    "londrina", "maringa", "ponta-grossa", "cascavel", "foz-do-iguacu", "colombo", "paranagua", "araucaria", "toledo", "apucarana", "pinhais", "campo-largo", "arapongas", "piraquara", "umuarama", "cambe", "campo-mourao", "sarandi", "fazenda-rio-grande", "paranavai", "francisco-beltrao", "pato-branco", "cianorte", "telemaco-borba", "castro", "rolandia", "irati", "uniao-da-vitoria", "marechal-candido-rondon", "ibipora",
    # SC
    "joinville", "blumenau", "sao-jose", "chapeco", "itajai", "criciuma", "jaragua-do-sul", "palhoca", "lages", "balneario-camboriu", "brusque", "tubarao", "camboriu", "navegantes", "rio-do-sul", "gaspar", "indaial", "biguacu", "ararangua", "cacador", "concordia", "videira", "sao-bento-do-sul",
    # BA
    "feira-de-santana", "vitoria-da-conquista", "camacari", "itabuna", "juazeiro", "lauro-de-freitas", "ilheus", "jequie", "teixeira-de-freitas", "alagoinhas", "porto-seguro", "simoes-filho", "paulo-afonso", "eunapolis", "santo-antonio-de-jesus",
    # PE
    "jaboatao-dos-guararapes", "olinda", "caruaru", "petrolina", "paulista", "camaragibe", "garanhuns", "vitoria-de-santo-antao", "cabo-de-santo-agostinho", "igarassu", "sao-lourenco-da-mata",
    # CE
    "caucaia", "juazeiro-do-norte", "maracanau", "sobral", "crato", "itapipoca", "iguatu",
    # GO
    "aparecida-de-goiania", "anapolis", "rio-verde", "luziania", "aguas-lindas-de-goias", "valparaiso-de-goias", "trindade", "formosa", "itumbiara", "caldas-novas",
    # ES
    "serra", "vila-velha", "cariacica", "cachoeiro-de-itapemirim", "linhares", "sao-mateus", "colatina", "guarapari", "aracruz",
    # Outros
    "ananindeua", "santarem", "maraba", "castanhal", "mossoro", "parnamirim", "varzea-grande", "rondonopolis", "sinop", "dourados", "campina-grande", "imperatriz", "sao-jose-de-ribamar", "timon", "caxias", "arapiraca", "ji-parana", "ariquemes", "santana",
    # Bairros RJ
    "barra-da-tijuca", "recreio-dos-bandeirantes", "copacabana", "ipanema", "leblon", "humaita", "laranjeiras"
]

# Lista de Segmentos (Mesma do gerar_paginas.py)
segmentos = [
    "advogado", "clinica", "medico", "engenheiro", "amarracao-amorosa", "magia-amorosa", "tarologa", "astrologa", "dentista", "arquiteto", "contador", "imobiliaria", "restaurante", "delivery", "academia", "personal-trainer", "psicologo", "nutricionista", "barbearia", "salao-de-beleza", "pet-shop", "oficina-mecanica", "construtora"
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
    # Aponta para as páginas estáticas geradas (Mais rápido e melhor SEO)
    for slug in locais:
        url = f"{BASE_URL}/criacao-de-sites-em-{slug}.html"
        
        xml_content += '  <url>\n'
        xml_content += f'    <loc>{url}</loc>\n'
        xml_content += f'    <lastmod>{hoje}</lastmod>\n'
        xml_content += '    <priority>0.80</priority>\n'
        xml_content += '  </url>\n'
        
    # 4. Páginas de Segmentos (Prioridade Alta)
    for seg in segmentos:
        url = f"{BASE_URL}/site-para-{seg}.html"
        xml_content += '  <url>\n'
        xml_content += f'    <loc>{url}</loc>\n'
        xml_content += f'    <lastmod>{hoje}</lastmod>\n'
        xml_content += '    <priority>0.90</priority>\n'
        xml_content += '  </url>\n'

    xml_content += '</urlset>'
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml_content)
        
    print(f"Sucesso! sitemap.xml gerado com {len(locais) + len(segmentos) + 2} URLs.")

if __name__ == "__main__":
    gerar_xml()