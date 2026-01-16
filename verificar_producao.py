import urllib.request
import sys

def check_live_site():
    url = "https://www.cybernexinnovatech.com.br"
    ga_id = "G-XQ3E4D0VRJ"
    
    print(f"--- 🌍 Verificando Site em Produção: {url} ---")
    
    try:
        # 1. Verificar Home
        print(f"📡 Conectando a {url}...", end=" ")
        # User-Agent para evitar bloqueios simples de bots
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        )
        
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                print("✅ Online (200 OK)")
                content = response.read().decode('utf-8')
                
                # 2. Verificar GA4
                if ga_id in content:
                    print(f"   ✅ Google Analytics ({ga_id}) encontrado.")
                else:
                    print(f"   ❌ ERRO: Google Analytics ({ga_id}) NÃO encontrado no código fonte.")
            else:
                print(f"❌ Erro: Status {response.status}")
                
        # 3. Verificar Sitemap
        sitemap_url = f"{url}/sitemap.xml"
        print(f"🗺️  Verificando {sitemap_url}...", end=" ")
        try:
            with urllib.request.urlopen(sitemap_url) as response:
                if response.status == 200:
                    print("✅ Encontrado")
                else:
                    print(f"❌ Status {response.status}")
        except Exception as e:
            print(f"❌ Erro: {e}")

        print("\n--- Dica Final ---")
        print("👉 Acesse o Google Search Console e envie seu sitemap.xml para indexação mais rápida.")

    except Exception as e:
        print(f"\n❌ Erro fatal ao conectar: {e}")
        print("Verifique se o domínio já propagou ou se a URL está correta.")

if __name__ == "__main__":
    check_live_site()
