import os
import glob
import re

def main():
    # Código que faz o Telegram apitar
    new_radar_script = """
    <script>
      fetch('http://187.77.40.40:5678/webhook/f45658e9-96d7-42ba-ae55-f436c072e328', {
        method: 'POST',
        mode: 'no-cors',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          origem: document.title,
          url: window.location.href,
          mensagem: "Visita capturada pelo Radar Cybernex"
        })
      });
    </script>
    """

    files = glob.glob("*.html")
    count = 0

    print(f"🚀 Iniciando ATIVAÇÃO TOTAL em {len(files)} páginas...")

    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 1. Limpeza: Remove scripts antigos do Ngrok ou do IP anterior
            # Isso evita que o código fique duplicado ou com erro
            content = re.sub(r'<script>.*?ngrok-free\.dev.*?</script>', '', content, flags=re.DOTALL)
            content = re.sub(r'<script>.*?187\.77\.40\.40.*?/script>', '', content, flags=re.DOTALL)
            
            # Remove também blocos comentados que você tinha antes
            content = re.sub(r'/\*.*?ngrok-free\.dev.*?\*/', '', content, flags=re.DOTALL)

            # 2. Inserção: Coloca o novo script logo antes do </body>
            if "</body>" in content:
                # Verifica se já não foi inserido nesta rodada para não duplicar
                if "f45658e9-96d7-42ba-ae55-f436c072e328" not in content:
                    new_content = content.replace("</body>", f"{new_radar_script}\n</body>")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    count += 1
            else:
                print(f"⚠️ Sem tag body em: {file_path}")

        except Exception as e:
            print(f"❌ Erro em {file_path}: {e}")

    print(f"\n✅ SUCESSO! {count} páginas agora estão enviando notificações para o Telegram!")

if __name__ == "__main__":
    main()