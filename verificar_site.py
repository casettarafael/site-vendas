import os

# Configurações
OUTPUT_PREFIX = 'criacao-de-sites-em-'

# Lista de Locais (Deve ser igual ao gerar_paginas.py)
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
    # Interior de SP
    {"nome": "Campinas", "uf": "SP", "slug": "campinas"},
    {"nome": "São José dos Campos", "uf": "SP", "slug": "sao-jose-dos-campos"},
    {"nome": "Ribeirão Preto", "uf": "SP", "slug": "ribeirao-preto"},
    {"nome": "Sorocaba", "uf": "SP", "slug": "sorocaba"},
    {"nome": "São José do Rio Preto", "uf": "SP", "slug": "sao-jose-do-rio-preto"}
]

def verificar():
    print("--- Iniciando Auditoria do Site ---")
    erros = 0
    sucessos = 0

    # 1. Verificar index.html
    if not os.path.exists('index.html'):
        print("[CRÍTICO] index.html não encontrado!")
        return
    
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()

    # 2. Verificar cada página gerada
    for local in locais:
        filename = f"{OUTPUT_PREFIX}{local['slug']}.html"
        
        # Checa se arquivo existe
        if not os.path.exists(filename):
            print(f"[ERRO] Arquivo faltando: {filename}")
            erros += 1
            continue

        # Checa conteúdo do arquivo
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Verifica se o nome da cidade foi inserido
            if local['nome'] not in content:
                print(f"[ERRO] {filename}: Nome da cidade '{local['nome']}' não encontrado no HTML.")
                erros += 1
            
            # Verifica se o script de segurança (Failsafe) está presente
            if "var p = document.getElementById('preloader');" not in content:
                print(f"[ERRO] {filename}: Script de segurança (Failsafe) AUSENTE. A tela branca pode ocorrer.")
                erros += 1

            # Verifica se existe link no index.html apontando para esta página
            if filename not in index_content:
                print(f"[ALERTA] Não encontrei link para {filename} no rodapé do index.html.")
        
        sucessos += 1

    print(f"\n--- Resultado ---")
    print(f"Arquivos verificados: {len(locais)}")
    print(f"Páginas OK: {sucessos}")
    print(f"Erros: {erros}")

if __name__ == "__main__":
    verificar()