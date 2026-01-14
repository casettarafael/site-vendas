import os

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
    # 5 Maiores do Interior de SP
    {"nome": "Campinas", "uf": "SP", "slug": "campinas"},
    {"nome": "São José dos Campos", "uf": "SP", "slug": "sao-jose-dos-campos"},
    {"nome": "Ribeirão Preto", "uf": "SP", "slug": "ribeirao-preto"},
    {"nome": "Sorocaba", "uf": "SP", "slug": "sorocaba"},
    {"nome": "São José do Rio Preto", "uf": "SP", "slug": "sao-jose-do-rio-preto"}
]

def gerar_paginas():
    if not os.path.exists(SOURCE_FILE):
        print(f"Erro: O arquivo '{SOURCE_FILE}' não foi encontrado na pasta.")
        return

    print("Lendo index.html para usar como base...")
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        html_base = f.read()

    # --- PREPARAÇÃO DO TEMPLATE EM MEMÓRIA ---
    # Substituímos os textos genéricos da Home por placeholders [[VARIAVEL]]
    
    # 1. Título da Página e Meta Tags (SEO Principal)
    template = html_base.replace('Criação de Sites para Todo o Brasil', 'Criação de Sites em [[CIDADE]]')
    template = template.replace('Atendemos empresas de todos os estados do Brasil', 'Atendemos empresas de [[CIDADE]]')
    
    # 2. Conteúdo do Hero e Textos
    template = template.replace('empresas de todo o Brasil', 'empresas de [[CIDADE]]')
    template = template.replace('Atendimento em todo o território nacional', 'Atendimento especializado em [[CIDADE]]')
    
    # 3. Ajuste no FAQ para parecer mais personalizado
    template = template.replace('Vocês atendem minha cidade?', 'Vocês atendem em [[CIDADE]]?')
    template = template.replace('Atendemos empresas de todos os estados do Brasil de forma 100% remota', 'Sim! Atendemos empresas de [[CIDADE]] de forma 100% remota')

    # 4. Canonical Tag (CRUCIAL PARA SEO - Evita conteúdo duplicado)
    # Troca a canonical da home pela URL do arquivo gerado
    template = template.replace('<link rel="canonical" href="https://www.cybernex.com.br/">', '<link rel="canonical" href="https://www.cybernex.com.br/[[FILENAME]]">')

    # 5. Atualizações de Rodapé e Sociais (Failsafe)
    # Garante que o link do Instagram esteja correto caso o template base seja antigo
    template = template.replace('href="#" aria-label="Instagram"', 'href="https://www.instagram.com/cybernexinnovatech?igsh=eHF1OGNmNXlrbDYx" aria-label="Instagram" target="_blank"')
    template = template.replace('href="#" aria-label="LinkedIn"', 'href="https://wa.me/5511976678655" aria-label="WhatsApp" target="_blank"')
    template = template.replace(' CNPJ: 00.000.000/0001-00', '')

    print(f"Gerando {len(locais)} páginas estáticas otimizadas...")

    for local in locais:
        filename = f"{OUTPUT_PREFIX}{local['slug']}.html"
        
        # Aplica os dados da cidade no template
        conteudo_pagina = template.replace('[[CIDADE]]', local['nome'])
        conteudo_pagina = conteudo_pagina.replace('[[UF]]', local['uf'])
        conteudo_pagina = conteudo_pagina.replace('[[FILENAME]]', filename)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(conteudo_pagina)
        
    print(f"Sucesso! {len(locais)} arquivos gerados com prefixo '{OUTPUT_PREFIX}'.")

if __name__ == "__main__":
    gerar_paginas()