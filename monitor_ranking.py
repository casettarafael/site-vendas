import time
import sys

# Tenta importar a biblioteca necessária
try:
    from googlesearch import search
except ImportError:
    print("❌ Erro: A biblioteca 'googlesearch-python' é necessária.")
    print("   Para instalar, abra o terminal e rode:")
    print("   pip install googlesearch-python")
    sys.exit(1)

# --- Configurações ---
TARGET_DOMAIN = "cybernex.com.br"
KEYWORDS = [
    "Cybernex Innovatech",                  # Marca (Deve ser Top 1)
    "Criação de Sites Profissionais",       # Principal (Difícil, mas meta)
    "Consultoria SEO para empresas",        # Serviço Específico
    "Criação de Landing Pages Vendas",      # Foco em conversão (Nicho)
    "Otimização de sites Core Web Vitals",  # Diferencial técnico do seu site
    "Empresa de criação de sites Brasil",   # Foco na abrangência nacional
    "Desenvolvimento de sites em São Paulo" # Foco local (Sua base)
]
MAX_RESULTS = 20  # Verifica até a 2ª página (aprox)

def check_rankings():
    print(f"--- 📊 Monitor de Ranking SEO: {TARGET_DOMAIN} ---")
    print(f"Verificando os top {MAX_RESULTS} resultados do Google...\n")

    results_summary = []

    for keyword in KEYWORDS:
        print(f"🔍 Buscando: '{keyword}'...", end=" ", flush=True)
        found = False
        
        try:
            # Pausa aleatória para parecer humano e evitar bloqueio (429)
            time.sleep(3)
            
            # Realiza a busca
            # num_results: Quantos resultados buscar
            # lang: Idioma (pt)
            # region: Região (br) - ajuda a simular busca local
            results = search(keyword, num_results=MAX_RESULTS, lang="pt", region="br")
            
            rank = 1
            for url in results:
                if TARGET_DOMAIN in url:
                    print(f"✅ Posição {rank}")
                    results_summary.append((keyword, rank, url))
                    found = True
                    break
                rank += 1
                
                # Segurança caso a lib retorne mais resultados que o solicitado
                if rank > MAX_RESULTS:
                    break
            
            if not found:
                print(f"❌ Fora do Top {MAX_RESULTS}")
                results_summary.append((keyword, "> " + str(MAX_RESULTS), "-"))

        except Exception as e:
            print(f"\n   ⚠️ Erro na busca: {e}")
            results_summary.append((keyword, "Erro", "-"))

    # Relatório Final
    print("\n" + "="*60)
    print(f"{'PALAVRA-CHAVE':<30} | {'POSIÇÃO':<10} | {'URL'}")
    print("-" * 60)
    for kw, pos, url in results_summary:
        # Truncar URL se for muito longa para caber na tabela
        url_display = (url[:35] + '..') if len(url) > 35 else url
        print(f"{kw:<30} | {str(pos):<10} | {url_display}")
    print("="*60)

if __name__ == "__main__":
    check_rankings()