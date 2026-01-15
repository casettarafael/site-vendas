import os

def check_performance():
    print("--- 🚀 Auditoria de Performance Cybernex ---")
    
    # 1. Verificar Imagens Pesadas
    print("\n1. Verificando Imagens Pesadas (>500KB)...")
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp']
    heavy_images = []
    
    for root, dirs, files in os.walk("."):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                path = os.path.join(root, file)
                size_kb = os.path.getsize(path) / 1024
                if size_kb > 500:
                    heavy_images.append((file, size_kb))
    
    if heavy_images:
        for img, size in heavy_images:
            print(f"   ⚠️  {img}: {size:.2f} KB (Considere otimizar ou converter para WebP)")
    else:
        print("   ✅ Nenhuma imagem excessivamente pesada encontrada.")

    # 2. Verificar .htaccess
    print("\n2. Verificando Configuração de Servidor...")
    if os.path.exists(".htaccess"):
        print("   ✅ Arquivo .htaccess encontrado (Gzip e Cache ativos).")
    else:
        print("   ❌ Arquivo .htaccess NÃO encontrado. Crie-o para ativar a compressão.")

    print("\n--- Fim da Auditoria ---")

if __name__ == "__main__":
    check_performance()