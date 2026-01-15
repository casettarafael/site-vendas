import os

def gerar_robots():
    print("🤖 Gerando robots.txt Otimizado...")
    
    # Configurações
    base_url = "https://www.cybernexinnovatech.com.br"
    sitemap_url = f"{base_url}/sitemap.xml"
    
    # Lista de User-Agents considerados "ruins" ou desnecessários para este projeto
    # Inclui ferramentas de SEO de concorrentes e buscadores de países onde você não atua
    bots_bloqueados = [
        "MJ12bot",      # Majestic (Backlinks)
        "AhrefsBot",    # Ahrefs (SEO/Backlinks)
        "SemrushBot",   # Semrush (SEO)
        "DotBot",       # Moz (SEO)
        "Baiduspider",  # Baidu (Buscador Chinês)
        "YandexBot",    # Yandex (Buscador Russo)
        "Sogou",        # Sogou (Buscador Chinês)
        "Exabot",       # Exalead
        "SeznamBot",    # Seznam (Buscador Tcheco)
        "ia_archiver",  # Internet Archive (Wayback Machine - opcional bloquear)
    ]

    robots_content = []

    # 1. Bloqueio explícito de bots indesejados
    for bot in bots_bloqueados:
        robots_content.append(f"User-agent: {bot}")
        robots_content.append("Disallow: /")
        robots_content.append("") # Linha em branco

    # 2. Permissão explícita para o Google (Googlebot) e Google Imagens
    robots_content.append("User-agent: Googlebot")
    robots_content.append("Allow: /")
    robots_content.append("")

    robots_content.append("User-agent: Googlebot-Image")
    robots_content.append("Allow: /")
    robots_content.append("")

    # 3. Regra Geral (User-agent: *)
    # Permite todos os outros bots (Bing, DuckDuckGo, Facebook, etc.)
    robots_content.append("User-agent: *")
    robots_content.append("Allow: /")
    robots_content.append("")

    # 4. Indicação do Sitemap
    robots_content.append(f"Sitemap: {sitemap_url}")

    # Escreve o arquivo
    try:
        with open('robots.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(robots_content))
        print(f"✅ robots.txt criado com sucesso! ({len(bots_bloqueados)} bots bloqueados)")
    except Exception as e:
        print(f"❌ Erro ao criar robots.txt: {e}")

if __name__ == "__main__":
    gerar_robots()