
import os
import glob

# O script que queremos injetar
SCRIPT_TRACKING = """
    <script>
      fetch('http://localhost:5678/webhook-test/visita-site', {
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
    </script>
"""

def main():
    print("--- 🔄 Injetando Script de Rastreamento em Massa ---")
    
    # Busca todos os arquivos .html na pasta atual
    arquivos = glob.glob("*.html")
    
    count = 0
    for arquivo in arquivos:
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            # Verifica se já tem o script para não duplicar
            if "webhook-test/visita-site" in conteudo:
                print(f"⏭️  {arquivo} já possui o script.")
                continue
                
            # Injeta antes do fechamento do body
            if "</body>" in conteudo:
                novo_conteudo = conteudo.replace("</body>", SCRIPT_TRACKING + "</body>")
                
                with open(arquivo, 'w', encoding='utf-8') as f:
                    f.write(novo_conteudo)
                print(f"✅ {arquivo} atualizado com sucesso.")
                count += 1
            else:
                print(f"⚠️  {arquivo} não tem tag </body>. Pulando.")
                
        except Exception as e:
            print(f"❌ Erro ao processar {arquivo}: {e}")

    print(f"\n✨ Concluído! {count} arquivos foram modificados.")

if __name__ == "__main__":
    main()
