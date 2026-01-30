import os
import glob

def main():
    # Padrão exato do código que queremos comentar
    # Importante: A indentação (espaços) deve ser exata conforme está nos arquivos HTML
    target_code = """      fetch('https://huffier-kenogenetically-delbert.ngrok-free.dev/webhook/visita-site', {
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

    # Versão comentada que substituirá o código acima
    replacement_code = """      /* Este é o código do radar. Está desativado temporariamente.
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

    # Busca todos os arquivos .html na pasta atual
    files = glob.glob("*.html")
    count = 0

    print(f"🔍 Iniciando verificação em {len(files)} arquivos HTML...")

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
            elif "/* Este é o código do radar" in content:
                print(f"ℹ️  Já estava comentado: {file_path}")
            else:
                print(f"⚠️  Código não encontrado em: {file_path} (Verifique a formatação)")

        except Exception as e:
            print(f"❌ Erro em {file_path}: {e}")

    print(f"\n🎉 Concluído! {count} arquivos foram modificados.")

if __name__ == "__main__":
    main()