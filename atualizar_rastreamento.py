import os
import glob

def main():
    # O código que está atualmente nos arquivos (comentado e com URL antiga)
    target_code = """      /* Este é o código do radar. Está desativado temporariamente.
      fetch('https://huffier-kenogenetically-delbert.ngrok-free.dev/webhook/visita-site', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          url: window.location.href,
          cidade: document.title,
          timestamp: new Date().toLocaleString()
        })
      })
      .then(response => console.log('Radar Cybernex: Sinal enviado!'))
      .catch(err => console.error('Radar Cybernex: Erro ao enviar', err));
      */"""

    # O novo código que queremos (ativo e com a nova URL)
    replacement_code = """      fetch('http://187.77.40.40:5678/webhook/f45658e9-96d7-42ba-ae55-f436c072e328', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          url: window.location.href,
          cidade: document.title,
          timestamp: new Date().toLocaleString()
        })
      })
      .then(response => console.log('Radar Cybernex: Sinal enviado!'))
      .catch(err => console.error('Radar Cybernex: Erro ao enviar', err));"""

    # Busca todos os arquivos .html na pasta atual
    files = glob.glob("*.html")
    count = 0

    print(f"🔍 Iniciando atualização de Webhook em {len(files)} arquivos HTML...")

    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            if target_code in content:
                new_content = content.replace(target_code, replacement_code)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"✅ Atualizado: {file_path}")
                count += 1
            elif "http://187.77.40.40:5678" in content:
                print(f"ℹ️  Já atualizado: {file_path}")
            else:
                print(f"⚠️  Código alvo não encontrado em: {file_path}")

        except Exception as e:
            print(f"❌ Erro em {file_path}: {e}")

    print(f"\n🎉 Concluído! {count} arquivos foram modificados.")

if __name__ == "__main__":
    main()