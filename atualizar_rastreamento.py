import os
import glob

def main():
    # 1. Código antigo (comentado) - Caso ainda não tenha sido atualizado
    old_commented_code = """      /* Este é o código do radar. Está desativado temporariamente.
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

    # 2. Código da tentativa anterior (sem no-cors) - Caso já tenha rodado o script antes
    previous_attempt_code = """      fetch('http://187.77.40.40:5678/webhook/f45658e9-96d7-42ba-ae55-f436c072e328', {
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

    # 3. Novo código correto (com no-cors e body ajustado)
    new_correct_code = """      fetch('http://187.77.40.40:5678/webhook/f45658e9-96d7-42ba-ae55-f436c072e328', {
        method: 'POST',
        mode: 'no-cors',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          origem: document.title,
          url: window.location.href,
          mensagem: "Visita capturada pelo Radar Cybernex"
        })
      });"""

    # Busca todos os arquivos .html na pasta atual
    files = glob.glob("*.html")
    count = 0

    print(f"🔍 Iniciando correção do Webhook em {len(files)} arquivos HTML...")

    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            new_content = content
            updated = False

            # Tenta substituir o código comentado antigo
            if old_commented_code in new_content:
                new_content = new_content.replace(old_commented_code, new_correct_code)
                updated = True
            
            # Tenta substituir o código da tentativa anterior
            if previous_attempt_code in new_content:
                new_content = new_content.replace(previous_attempt_code, new_correct_code)
                updated = True

            if updated:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"✅ Atualizado: {file_path}")
                count += 1
            elif "mode: 'no-cors'" in content:
                print(f"ℹ️  Já está correto: {file_path}")
            else:
                print(f"⚠️  Nenhum padrão conhecido encontrado em: {file_path}")

        except Exception as e:
            print(f"❌ Erro em {file_path}: {e}")

    print(f"\n🎉 Concluído! {count} arquivos foram corrigidos.")

if __name__ == "__main__":
    main()