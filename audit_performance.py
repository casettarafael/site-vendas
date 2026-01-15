import os
import re

def audit_html(filename='index.html'):
    print(f"--- 🚀 Auditoria de Performance: {filename} ---")
    
    if not os.path.exists(filename):
        print(f"❌ Arquivo {filename} não encontrado.")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        size_kb = len(content) / 1024

    # 1. Tamanho do Arquivo
    print(f"📦 Tamanho do HTML: {size_kb:.2f} KB", end=" ")
    if size_kb < 50:
        print("✅ (Excelente)")
    elif size_kb < 100:
        print("⚠️ (Bom, mas pode melhorar)")
    else:
        print("❌ (Pesado - considere minificar)")

    # 2. Imagens e Lazy Loading
    img_tags = re.findall(r'<img\s+[^>]*>', content)
    lazy_count = len(re.findall(r'loading=["\']lazy["\']', content))
    async_count = len(re.findall(r'decoding=["\']async["\']', content))
    
    print(f"\n🖼️  Imagens encontradas: {len(img_tags)}")
    print(f"   - Com Lazy Loading: {lazy_count} ✅")
    print(f"   - Com Decoding Async: {async_count} ✅")
    
    if len(img_tags) > (lazy_count + 2): # +2 tolerância para imagens above-the-fold
        print("   ⚠️ Algumas imagens podem estar sem lazy loading.")

    # 3. Scripts Bloqueantes
    scripts = re.findall(r'<script\s+[^>]*src=["\']([^"\']+)["\'][^>]*>', content)
    defer_count = len(re.findall(r'<script\s+[^>]*defer[^>]*>', content))
    async_script_count = len(re.findall(r'<script\s+[^>]*async[^>]*>', content))
    
    print(f"\n📜 Scripts Externos: {len(scripts)}")
    print(f"   - Defer/Async: {defer_count + async_script_count}")
    
    if len(scripts) > (defer_count + async_script_count):
        print("   ❌ Alerta: Existem scripts bloqueando a renderização (sem defer/async).")
    else:
        print("   ✅ Todos os scripts estão otimizados.")

    # 4. Resource Hints
    if 'dns-prefetch' in content:
        print("\n🌐 DNS Prefetch: Detectado ✅")
    else:
        print("\n🌐 DNS Prefetch: Não detectado (Recomendado para domínios externos)")

    print("\n--- Fim da Auditoria ---")

if __name__ == "__main__":
    audit_html()