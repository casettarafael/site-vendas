import json
import re
import os

def check_seo():
    print("--- Verificando Instalação de SEO ---")
    file_path = 'index.html'
    
    if not os.path.exists(file_path):
        print(f"❌ Erro: {file_path} não encontrado.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Verifica se o comentário identificador existe
    if "<!-- SEO AUTOMÁTICO: JSON-LD -->" in content:
        print("✅ Marcador de SEO encontrado no HTML.")
    else:
        print("❌ Marcador de SEO NÃO encontrado. Rode o 'python seo_booster.py' primeiro.")
        return

    # 2. Tenta extrair e validar o JSON
    # Procura pelo script logo após o comentário
    pattern = r'<!-- SEO AUTOMÁTICO: JSON-LD -->\s*<script type="application/ld\+json">(.*?)</script>'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        json_str = match.group(1)
        try:
            data = json.loads(json_str)
            print("✅ JSON-LD extraído e validado com sucesso!")
            
            # Detalhes do que foi encontrado
            if "@graph" in data:
                print(f"   📊 Entidades encontradas: {len(data['@graph'])}")
                for item in data['@graph']:
                    tipo = item.get('@type', 'Desconhecido')
                    nome = item.get('name', 'Sem nome')
                    print(f"      - {tipo}: {nome}")
            else:
                print("   ⚠️ JSON válido, mas estrutura diferente da esperada.")
                
        except json.JSONDecodeError as e:
            print(f"❌ Erro de sintaxe no JSON: {e}")
    else:
        print("❌ Tag <script> não encontrada logo após o marcador.")

if __name__ == "__main__":
    check_seo()