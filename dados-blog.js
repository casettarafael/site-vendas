const blogPosts = {
    "seo-basico": {
        title: "5 Dicas de SEO para Iniciantes",
        category: "SEO",
        date: "12 Out 2023",
        readTime: "5 min leitura",
        image: "https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a?auto=format&fit=crop&w=1200&q=80",
        content: `
            <p class="lead">Se você quer que seu site seja encontrado no Google, precisa entender o básico de SEO (Search Engine Optimization).</p>
            <h2>1. Palavras-chave são a base</h2>
            <p>Antes de escrever, pesquise o que seu público está buscando. Ferramentas como Google Keyword Planner ou Ubersuggest ajudam a encontrar termos com bom volume de busca.</p>
            <h2>2. Títulos e Meta Descrições</h2>
            <p>O título da página (Title Tag) é o fator mais importante on-page. Certifique-se de que sua palavra-chave principal esteja nele. A meta descrição funciona como um anúncio para atrair o clique.</p>
            <h2>3. Velocidade de Carregamento</h2>
            <p>O Google odeia sites lentos. Use ferramentas como PageSpeed Insights para identificar gargalos. Comprima imagens e evite scripts desnecessários.</p>
            <h2>4. Conteúdo de Qualidade</h2>
            <p>Não escreva para robôs, escreva para humanos. O Google prioriza conteúdo que resolve a dúvida do usuário de forma completa e original.</p>
            <h2>5. Links Internos</h2>
            <p>Crie uma teia de links dentro do seu site. Isso ajuda o Google a entender a estrutura do seu conteúdo e distribui autoridade entre as páginas.</p>
        `
    },
    "performance-web": {
        title: "Por que seu site está lento?",
        category: "Performance",
        date: "15 Out 2023",
        readTime: "4 min leitura",
        image: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1200&q=80",
        content: `
            <p class="lead">A velocidade do site impacta diretamente suas vendas e seu posicionamento no Google.</p>
            <h2>O Impacto do Core Web Vitals</h2>
            <p>O Google agora usa métricas de experiência do usuário (Core Web Vitals) como fator de ranqueamento. LCP (tempo de carregamento), FID (interatividade) e CLS (estabilidade visual) são cruciais.</p>
            <h2>Imagens Pesadas</h2>
            <p>O erro mais comum são imagens gigantes. Use formatos modernos como WebP e defina dimensões explícitas no HTML para evitar layout shifts.</p>
            <h2>Excesso de JavaScript</h2>
            <p>Scripts de terceiros (chat, analytics, pixels) podem travar o navegador do usuário. Carregue-os de forma assíncrona ou diferida (defer).</p>
        `
    },
    "landing-vs-institucional": {
        title: "Landing Page vs Site Institucional",
        category: "Marketing",
        date: "20 Out 2023",
        readTime: "6 min leitura",
        image: "https://images.unsplash.com/photo-1533750349088-cd871a92f312?auto=format&fit=crop&w=1200&q=80",
        content: `
            <p class="lead">Escolher o tipo certo de site é fundamental para atingir seus objetivos de negócio.</p>
            <h2>O que é uma Landing Page?</h2>
            <p>É uma página focada em uma única ação (conversão). Geralmente usada em campanhas de tráfego pago. Não tem menu de navegação para não distrair o usuário.</p>
            <h2>O que é um Site Institucional?</h2>
            <p>É o cartão de visitas da sua empresa. Tem várias páginas (Sobre, Serviços, Contato) e serve para construir autoridade e apresentar a marca.</p>
            <h2>Qual escolher?</h2>
            <p>Se você quer vender um produto específico agora, vá de Landing Page. Se quer construir marca a longo prazo, comece com um Institucional.</p>
        `
    },
    "design-trends-2024": {
        title: "Tendências de Web Design 2024",
        category: "Design",
        date: "25 Out 2023",
        readTime: "3 min leitura",
        image: "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?auto=format&fit=crop&w=1200&q=80",
        content: `
            <p class="lead">O web design está em constante evolução. Veja o que está em alta para 2024.</p>
            <h2>1. Bento Grids</h2>
            <p>Inspirado nas marmitas japonesas e popularizado pela Apple, esse layout em grade é organizado e visualmente interessante.</p>
            <h2>2. Tipografia Gigante</h2>
            <p>Textos grandes e em negrito que ocupam a tela toda estão substituindo imagens de herói tradicionais.</p>
            <h2>3. Micro-interações</h2>
            <p>Pequenas animações ao passar o mouse ou clicar tornam a experiência mais viva e responsiva.</p>
            <h2>4. Modo Escuro (Dark Mode)</h2>
            <p>Mais do que uma tendência, virou uma necessidade para conforto visual e economia de bateria.</p>
        `
    },
    "ga4-guia": {
        title: "Entendendo o Google Analytics 4",
        category: "Dados",
        date: "28 Out 2023",
        readTime: "8 min leitura",
        image: "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?auto=format&fit=crop&w=1200&q=80",
        content: `
            <p class="lead">O Universal Analytics morreu. O GA4 é o novo padrão e foca em eventos, não em sessões.</p>
            <h2>Tudo é um Evento</h2>
            <p>No GA4, uma visualização de página é um evento. Um clique é um evento. Isso dá muito mais flexibilidade para rastrear o que importa.</p>
            <h2>Engajamento vs Rejeição</h2>
            <p>A Taxa de Rejeição foi substituída pela Taxa de Engajamento. O Google agora mede se o usuário interagiu com o site, não apenas se ele saiu.</p>
            <h2>Configuração Essencial</h2>
            <p>Certifique-se de configurar o "Enhanced Measurement" para rastrear scrolls, cliques em links externos e downloads automaticamente.</p>
        `
    },
    "email-marketing": {
        title: "Email Marketing ainda funciona?",
        category: "Marketing",
        date: "01 Nov 2023",
        readTime: "5 min leitura",
        image: "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1200&q=80",
        content: `
            <p class="lead">Com tantas redes sociais, o email parece velho. Mas é o canal com maior ROI (Retorno sobre Investimento).</p>
            <h2>A Lista é Sua</h2>
            <p>Redes sociais podem mudar o algoritmo e cortar seu alcance. Sua lista de emails é um ativo que você controla.</p>
            <h2>Segmentação</h2>
            <p>Você pode enviar ofertas específicas para quem clicou em um link ou abandonou o carrinho. Isso aumenta muito a conversão.</p>
            <h2>Automação</h2>
            <p>Crie sequências de boas-vindas que vendem para você no piloto automático enquanto você dorme.</p>
        `
    }
};