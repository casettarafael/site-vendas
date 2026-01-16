# Cybernex Innovatech - Gerador de Site SEO Local

Este projeto é um gerador de sites estáticos focado em SEO Local e segmentação de mercado. Ele utiliza um template base (`index.html`) para gerar centenas de páginas otimizadas para diferentes cidades e nichos de atuação.

## 📋 Pré-requisitos

- **Python 3.x** instalado no seu computador.

## 🚀 Como Rodar o Projeto

A maneira mais fácil de gerar o site completo e testar é utilizando o script de automação:

1. Abra o terminal na pasta do projeto.
2. Execute o comando:
   ```bash
   python gerar_tudo.py
   ```

Este comando irá:
1. Gerar todas as páginas de cidades e segmentos.
2. Gerar os artigos do blog.
3. Atualizar o `sitemap.xml`, `robots.txt` e `rss.xml`.
4. Injetar dados estruturados (JSON-LD) na home.
5. Verificar se há erros críticos.
6. Iniciar um servidor local em `http://localhost:8000`.

## 📂 Estrutura dos Scripts

- **`gerar_tudo.py`**: Script principal. Roda todos os outros na ordem correta e abre o servidor local.
- **`gerar_paginas.py`**: Gera as páginas específicas para cada cidade (ex: `criacao-de-sites-em-sao-paulo.html`) e segmento (ex: `site-para-advogado.html`) usando `index.html` como base.
- **`gerar_blog.py`**: Gera as páginas de artigos do blog baseadas em `artigo.html`.
- **`gerar_sitemap.py`**: Cria o arquivo `sitemap.xml` listando todas as páginas geradas para o Google.
- **`gerar_robots.py`**: Cria o arquivo `robots.txt` com regras de acesso para robôs de busca.
- **`seo_booster.py`**: Atualiza o `index.html` com dados estruturados (Rich Snippets) atualizados.
- **`verificar_deploy.py`**: Faz uma varredura final para garantir que não ficaram placeholders (como `[[CIDADE]]`) no código final.

## ⚙️ Como Personalizar

### Adicionar Novas Cidades ou Segmentos
Edite o arquivo **`gerar_paginas.py`**:
- Procure a lista `locais` para adicionar cidades.
- Procure a lista `segmentos` para adicionar nichos.

### Alterar o Layout
Edite o arquivo **`index.html`**. Ele serve como o "molde" para todas as páginas de cidades e segmentos.
- **Atenção**: O script usa o conteúdo do `index.html` para criar as outras páginas. Se você mudar o design da Home, todas as outras páginas serão atualizadas na próxima geração.

### Configurar Analytics
No arquivo **`index.html`**, procure por `G-SEU_ID_AQUI` e substitua pelo seu ID do Google Analytics 4.

## 📦 Deploy (Subir para Produção)

1. Rode `python gerar_tudo.py` e aguarde a mensagem "🚀 TUDO PRONTO!".
2. Se houver erros, o script avisará. Corrija-os antes de subir.
3. Faça o upload de **todos os arquivos .html, .css, .js, .xml, .txt e imagens** para sua hospedagem (Vercel, Netlify, Hostgator, etc.).
   - *Não é necessário subir os scripts .py ou a pasta .git.*