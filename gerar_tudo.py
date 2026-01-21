import os
import subprocess
import time
import webbrowser
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

def run_step(script_name):
    print(f"🔄 Executando {script_name}...")
    if os.path.exists(script_name):
        try:
            subprocess.run([sys.executable, script_name], check=True)
            print("✅ OK.")
        except Exception as e:
            print(f"❌ Erro: {e}")
    else:
        print(f"⚠️ {script_name} não encontrado.")

def main():
    print("--- 🚀 AUTO-BUILD & SERVER ---")
    
    run_step("seo_booster.py") # Executa primeiro para atualizar o index.html
    run_step("gerar_paginas.py")
    run_step("gerar_blog.py")
    run_step("gerar_sitemap.py")
    run_step("gerar_rss.py")
    run_step("gerar_robots.py")
    run_step("seo_booster.py")

    print("\\n✨ Site gerado! Iniciando servidor em http://localhost:8000")
    
    def open_browser():
        time.sleep(2)
        webbrowser.open("http://localhost:8000")
    
    threading.Thread(target=open_browser).start()

    server_address = ('', 8000)
    try:
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        httpd.serve_forever()
    except Exception as e:
        print(f"Erro no servidor: {e}")

if __name__ == "__main__":
    main()
