import os
import glob
import sys

# Configurações
OUTPUT_PREFIX = 'criacao-de-sites-em-'

# Importa a lista oficial de locais para garantir consistência
try:
    from gerar_paginas import locais, segmentos
except ImportError:
    print("❌ ERRO CRÍTICO: Não foi possível importar 'gerar_paginas.py'.")
    # Define listas vazias para não quebrar o script totalmente
    locais = []
    segmentos = []

def verificar():
    print("=========================================")
    print("   🕵️‍♂️ DIAGNÓSTICO COMPLETO DO SISTEMA")
    print("=========================================")
    
    erros = 0
    avisos = 0

    # 1. Análise da Lista de Cidades
    print("\n[1] Analisando Configuração de Cidades...")
    total_cidades = len(locais)
    slugs = [l['slug'] for l in locais]
    slugs_unicos = set(slugs)
    
    print(f"   - Cidades configuradas: {total_cidades}")
    
    if len(slugs) != len(slugs_unicos):
        duplicadas = total_configurado - len(slugs_unicos)
        print(f"   ⚠️  AVISO: Existem {duplicadas} cidades duplicadas na lista!")
        avisos += 1
    else:
        print("   ✅ Nenhuma duplicidade encontrada.")

    # 2. Análise de Arquivos Gerados
    print("\n[2] Verificando Arquivos Gerados...")
    arquivos_cidades = glob.glob('criacao-de-sites-em-*.html')
    total_arquivos = len(arquivos_cidades)
    
    print(f"   - Arquivos HTML de cidades encontrados: {total_arquivos}")
    
    if total_arquivos == 0:
        print("   ❌ ERRO: Nenhuma página gerada. Rode 'python gerar_tudo.py'.")
        erros += 1
    elif total_arquivos < len(slugs_unicos):
        faltando = len(slugs_unicos) - total_arquivos
        print(f"   ❌ ERRO: Faltam {faltando} páginas para serem geradas.")
        erros += 1
    else:
        print("   ✅ Todas as páginas configuradas foram geradas.")

    # 3. Verificação de Estrutura
    print("\n[3] Verificando Estrutura do Site...")
    arquivos_essenciais = ['index.html', 'cobertura.html', 'sitemap.xml', 'robots.txt', 'rss.xml']
    for arq in arquivos_essenciais:
        if os.path.exists(arq):
            print(f"   ✅ {arq} encontrado.")
        else:
            print(f"   ❌ ERRO: {arq} não encontrado.")
            erros += 1

    # 4. Verificação de Conteúdo (Amostragem)
    print("\n[4] Verificando Conteúdo (Amostragem)...")
    if total_arquivos > 0:
        # Pega o primeiro arquivo para teste
        amostra = arquivos_cidades[0]
        try:
            with open(amostra, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Verifica Placeholders não substituídos
                if '[[CIDADE]]' in content:
                    print(f"   ❌ ERRO: Placeholder [[CIDADE]] encontrado em {amostra}")
                    erros += 1
                else:
                    print("   ✅ Substituição de variáveis: OK")
        except Exception as e:
            print(f"   ❌ ERRO ao ler amostra: {e}")
            erros += 1

    # 5. Verificação do Sitemap
    print("\n[5] Verificando Sitemap...")
    if os.path.exists('sitemap.xml'):
        try:
            with open('sitemap.xml', 'r', encoding='utf-8') as f:
                sitemap_content = f.read()
                count_urls = sitemap_content.count('<loc>')
                print(f"   - URLs no sitemap: {count_urls}")
                
                # Estimativa: Cidades + Segmentos + Home + Blog + Cobertura
                esperado = len(slugs_unicos) + len(segmentos) 
                if count_urls < esperado:
                    print(f"   ⚠️  AVISO: Sitemap parece incompleto (Tem {count_urls}, esperado aprox {esperado}).")
                    avisos += 1
                else:
                    print("   ✅ Sitemap parece completo.")
        except Exception as e:
            print(f"   ❌ ERRO ao ler sitemap: {e}")
            erros += 1

    print("\n=========================================")
    print(f"RESUMO: {erros} Erros, {avisos} Avisos")
    if erros == 0:
        print("🚀 SISTEMA OPERACIONAL E PRONTO PARA USO!")
    else:
        print("🛑 CORRIJA OS ERROS ACIMA.")
    print("=========================================")

if __name__ == "__main__":
    verificar()