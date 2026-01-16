import os
import subprocess
import time
import webbrowser
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

def run_step(script_name, description):
    print(f"🔄 {description} ({script_name})...")
    if os.path.exists(script_name):
        try:
            # Usa sys.executable para garantir que usa o mesmo Python que está rodando este script
            subprocess.run([sys.executable, script_name], check=True)
            print("✅ Concluído.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao executar {script_name}: {e}")
    else:
        print(f"⚠️ Arquivo {script_name} não encontrado. Pulando.")
    print("-" * 40)

def main():
    print("--- 🚀 AUTO-BUILD & SERVER: Cybernex Innovatech ---")
    print("Gerando todo o site estático e iniciando servidor...\n")

    # Lista de scripts para rodar em ordem
    scripts = [
        ("gerar_paginas.py", "Gerando Cidades e Segmentos"),
        ("gerar_blog.py", "Gerando Artigos do Blog"),
        ("gerar_sitemap.py", "Atualizando Sitemap.xml"),
        ("gerar_rss.py", "Gerando Feed RSS"),
        ("gerar_robots.py", "Criando Robots.txt"),
        ("seo_booster.py", "Injetando Dados Estruturados na Home"),
        ("verificar_deploy.py", "Verificação Final de Segurança")
    ]

    for script, desc in scripts:
        run_step(script, desc)

    print("\n✨ Geração concluída! Iniciando servidor local...")
    print("👉 Acesse: http://localhost:8000")
    print("⌨️  Pressione Ctrl+C para encerrar.\n")

    # Abre o navegador automaticamente após 2 segundos
    def open_browser():
        time.sleep(2)
        webbrowser.open("http://localhost:8000")
    
    threading.Thread(target=open_browser).start()

    # Inicia o servidor na porta 8000
    server_address = ('', 8000)
    try:
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        httpd.serve_forever()
    except OSError as e:
        print(f"\n❌ Erro ao iniciar servidor na porta 8000: {e}")
        print("Tente fechar outros terminais ou usar outra porta.")
    except KeyboardInterrupt:
        print("\n🛑 Servidor encerrado.")

if __name__ == "__main__":
    main()
