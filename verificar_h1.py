import os
import re

# Configurações
OUTPUT_PREFIX = 'criacao-de-sites-em-'

# Importa a lista oficial de locais para garantir consistência
try:
    from gerar_paginas import locais
except ImportError:
    print("[ERRO] Não foi possível importar a lista de locais de gerar_paginas.py")
    locais = []

def verificar_h1():
    print("--- Verificação de H1 em Páginas Geradas ---")
    erros = 0
    sucessos = 0
    total = 0

    for local in locais:
        city_name = local['nome']
        slug = local['slug']
        filename = f"{OUTPUT_PREFIX}{slug}.html"
        
        if not os.path.exists(filename):
            print(f"[ERRO] Arquivo não encontrado: {filename}")
            erros += 1
            continue

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex para capturar o conteúdo do H1
        # O H1 pode ter atributos e spans dentro.
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL | re.IGNORECASE)
        
        if h1_match:
            h1_content = h1_match.group(1)
            # Verifica se o nome da cidade está presente no conteúdo do H1
            if city_name in h1_content:
                sucessos += 1
            else:
                print(f"[FALHA] {filename}: Cidade '{city_name}' NÃO encontrada no H1.")
                print(f"       Conteúdo H1 encontrado: {h1_content.strip()[:100]}...")
                erros += 1
        else:
            print(f"[FALHA] {filename}: Tag <h1> não encontrada.")
            erros += 1
        
        total += 1

    print("-" * 40)
    print(f"Total verificado: {total}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")

if __name__ == "__main__":
    verificar_h1()