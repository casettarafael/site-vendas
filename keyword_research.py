import requests
import json
import time

def get_google_suggestions(seed_keyword):
    """
    Busca sugestões do Google Autocomplete para uma palavra-chave.
    O Google retorna os termos mais buscados (relevantes) relacionados à semente.
    """
    # URL da API não oficial do Google Suggest (usada pelo Firefox/Chrome)
    url = f"http://suggestqueries.google.com/complete/search?client=firefox&q={seed_keyword}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = json.loads(response.text)
            # O formato retornado é [query, [lista_de_sugestoes]]
            return data[1]
    except Exception as e:
        print(f"Erro ao buscar '{seed_keyword}': {e}")
    
    return []

def main():
    print("--- 🤖 Robô de Pesquisa de Palavras-Chave (Google Suggest) ---")
    print("Descobrindo termos relevantes que seus clientes realmente digitam...\n")

    # Termos "semente" baseados no seu negócio
    seeds = [
        "criação de sites",
        "desenvolvimento web",
        "consultoria seo",
        "landing page",
        "gestão de tráfego",
        "otimização de sites",
        "programador de sites",
        "empresa de sites"
    ]

    all_keywords = set()

    for seed in seeds:
        print(f"🔍 Investigando: '{seed}'...", end=" ")
        suggestions = get_google_suggestions(seed)
        
        if suggestions:
            print(f"✅ {len(suggestions)} variações encontradas.")
            for s in suggestions:
                all_keywords.add(s)
        else:
            print("❌ Nenhuma sugestão.")
        
        # Pausa para não bloquear o IP
        time.sleep(1.5)

    print("\n" + "="*50)
    print(f"📊 RELATÓRIO: {len(all_keywords)} Palavras-Chave de Alta Relevância")
    print("="*50)
    
    # Salvar e mostrar resultados
    with open("palavras_relevantes.txt", "w", encoding="utf-8") as f:
        for kw in sorted(all_keywords):
            print(f" -> {kw}")
            f.write(kw + "\n")
            
    print("\n📁 Lista completa salva em 'palavras_relevantes.txt'")

if __name__ == "__main__":
    main()