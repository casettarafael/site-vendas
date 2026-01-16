import os
import sys
import subprocess

def run_script(script_name):
    print(f"🔄 Rodando {script_name}...")
    try:
        subprocess.run([sys.executable, script_name], check=True)
        print("✅ Sucesso.")
    except Exception as e:
        print(f"❌ Erro ao rodar {script_name}: {e}")

def fix_index_links():
    print("🔧 Verificando links no index.html...")
    if not os.path.exists('index.html'):
        print("⚠️ index.html não encontrado.")
        return

    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Mapa de correções (Slug antigo/dinâmico -> Arquivo estático)
    # Baseado nos slugs do gerar_blog.py
    correcoes = {
        'artigo.html?id=seo-basico': 'artigo-seo-basico.html',
        'artigo.html?id=performance-web': 'artigo-performance-web.html',
        'artigo.html?id=landing-vs-institucional': 'artigo-landing-vs-institucional.html',
        'artigo.html?id=design-trends-2024': 'artigo-design-trends-2024.html',
        'artigo.html?id=ga4-guia': 'artigo-ga4-guia.html',
        'artigo.html?id=email-marketing': 'artigo-email-marketing.html'
    }

    changes = 0
    for old, new in correcoes.items():
        if old in content:
            content = content.replace(old, new)
            changes += 1
            print(f"   - Corrigido link: {old} -> {new}")

    if changes > 0:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ {changes} links corrigidos no index.html!")
    else:
        print("✅ Nenhum link quebrado encontrado no index.html (ou já estão corretos).")

if __name__ == "__main__":
    print("--- 🚑 Reparo de Emergência do Blog ---")
    run_script('gerar_blog.py')
    run_script('gerar_rss.py')
    fix_index_links()
    print("\n🚀 Tudo pronto! Teste os botões 'Ler Mais' agora.")