import os
import glob

def verificar():
    print("--- 🕵️‍♂️ Verificação de Integridade para Produção ---")
    erros = 0
    avisos = 0

    # 1. Verificar se os arquivos foram gerados
    files = glob.glob('criacao-de-sites-em-*.html')
    if len(files) == 0:
        print("❌ ERRO: Nenhuma página de cidade encontrada. Rode gerar_paginas.py.")
        erros += 1
    else:
        print(f"✅ {len(files)} páginas de cidades encontradas.")

    # 2. Verificar Placeholders (Indica falha na substituição)
    placeholders = ['[[CIDADE]]', '[[UF]]', '[[SEGMENTO_SINGULAR]]', '[[FILENAME]]']
    # Verifica uma amostra para ser rápido
    for f in files[:50]: 
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            for p in placeholders:
                if p in content:
                    print(f"❌ ERRO: Placeholder {p} encontrado em {f}")
                    erros += 1

    # 3. Verificar Analytics
    if os.path.exists('index.html'):
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
            if 'G-SEU_ID_AQUI' in content or 'G-XXXXXXXXXX' in content:
                print("⚠️  AVISO: ID do Google Analytics não configurado (está como padrão).")
                avisos += 1

    # 4. Verificar Sitemap e Robots
    if not os.path.exists('sitemap.xml'):
        print("❌ ERRO: sitemap.xml ausente.")
        erros += 1
    if not os.path.exists('robots.txt'):
        print("❌ ERRO: robots.txt ausente.")
        erros += 1

    print("-" * 30)
    if erros == 0:
        print("🚀 TUDO PRONTO! Pode subir para produção.")
    else:
        print(f"🛑 Corrija os {erros} erros antes de subir.")

if __name__ == "__main__":
    verificar()