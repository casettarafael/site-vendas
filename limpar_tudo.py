import os
import glob

def limpar():
    print("--- Iniciando Limpeza do Projeto ---")
    
    # 1. Remove arquivos HTML gerados anteriormente
    files = glob.glob('criacao-de-sites-em-*.html')
    for f in files:
        try:
            os.remove(f)
            print(f"Removido: {f}")
        except Exception as e:
            print(f"Erro ao remover {f}: {e}")

    # 2. Remove scripts de geração/verificação antigos
    scripts = ['verificar_site.py']
    for s in scripts:
        if os.path.exists(s):
            os.remove(s)
            print(f"Removido script antigo: {s}")

    print("\nLimpeza concluída! Agora vamos configurar o local.html.")

if __name__ == "__main__":
    limpar()