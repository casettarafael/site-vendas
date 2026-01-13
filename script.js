// Lógica do Accordion (FAQ)
const faqItems = document.querySelectorAll('.faq-item');

faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    question.addEventListener('click', () => {
        // Fecha outros itens abertos (opcional)
        faqItems.forEach(otherItem => {
            if (otherItem !== item) otherItem.classList.remove('active');
        });
        // Alterna o atual
        item.classList.toggle('active');
    });
});

// Fade-in Animation on Scroll
const hiddenElements = document.querySelectorAll('.hidden, .hidden-left, .hidden-right, .scale-up, .blur-in');

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
            observer.unobserve(entry.target); // Opcional: remove o observer após a animação
        }
    });
}, {
    threshold: 0.2 // Define quando o elemento é considerado visível (20% neste caso)
});

hiddenElements.forEach((el) => observer.observe(el));

// Form Validation
const contactForm = document.querySelector('form');
if (contactForm) {
    contactForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Impede o envio padrão e recarregamento

        let nome = document.getElementById('nome').value;
        let objetivo = document.getElementById('objetivo') ? document.getElementById('objetivo').value : '';

        if (nome === '' || objetivo === '') {
            contactForm.classList.add('shake');
            setTimeout(() => {
                contactForm.classList.remove('shake');
            }, 500);
            alert('Por favor, preencha todos os campos obrigatórios.');
            return;
        }

        // Coleta dados dos campos (verifica se existem para funcionar em ambas as páginas)
        const empresa = document.getElementById('empresa') ? document.getElementById('empresa').value : '';
        const telefone = document.getElementById('telefone') ? document.getElementById('telefone').value : '';
        const cpf = document.getElementById('cpf') ? document.getElementById('cpf').value : '';
        const orcamento = document.getElementById('orcamento') ? document.getElementById('orcamento').value : '';

        // Formata a mensagem para o WhatsApp
        let message = `*Novo Contato do Site*\n\n*Nome:* ${nome}\n`;
        if (empresa) message += `*Empresa:* ${empresa}\n`;
        if (telefone) message += `*Telefone:* ${telefone}\n`;
        if (cpf) message += `*CPF:* ${cpf}\n`;
        message += `*Objetivo:* ${objetivo}\n`;
        if (orcamento) message += `*Orçamento:* ${orcamento}`;

        // Envia para o WhatsApp (Substitua o número abaixo pelo seu)
        const phoneNumber = "5511976678655"; 
        window.open(`https://wa.me/${phoneNumber}?text=${encodeURIComponent(message)}`, '_blank');

        // Limpa o formulário após o envio
        contactForm.reset();

        // Efeito de Confete
        if (typeof confetti === 'function') {
            confetti({
                particleCount: 150,
                spread: 100,
                origin: { y: 0.6 },
                colors: ['#7c3aed', '#f59e0b', '#ffffff'] // Cores do site
            });
        }
    });
}

// Máscaras de Input (Telefone e CPF)
const inputTelefone = document.getElementById('telefone');
const inputCPF = document.getElementById('cpf');

if (inputTelefone) {
    inputTelefone.addEventListener('input', (e) => {
        let value = e.target.value.replace(/\D/g, '');
        value = value.replace(/^(\d{2})(\d)/g, '($1) $2');
        value = value.replace(/(\d)(\d{4})$/, '$1-$2');
        e.target.value = value;
    });
}

if (inputCPF) {
    inputCPF.addEventListener('input', (e) => {
        let value = e.target.value.replace(/\D/g, '');
        if (value.length > 11) value = value.slice(0, 11);
        value = value.replace(/(\d{3})(\d)/, '$1.$2');
        value = value.replace(/(\d{3})(\d)/, '$1.$2');
        value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
        e.target.value = value;
    });
}

// Menu Hambúrguer
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-links");
const overlay = document.querySelector(".overlay");
const logo = document.querySelector(".logo");

if (hamburger && navMenu) {
    hamburger.addEventListener("click", () => {
        hamburger.classList.toggle("active");
        navMenu.classList.toggle("active");
        if (overlay) overlay.classList.toggle("active");
    });

    // Função centralizada para fechar o menu
    const closeMenu = () => {
        hamburger.classList.remove("active");
        navMenu.classList.remove("active");
        if (overlay) overlay.classList.remove("active");
    };

    document.querySelectorAll(".nav-links a").forEach(n => n.addEventListener("click", closeMenu));
    if (logo) logo.addEventListener("click", closeMenu);

    // Fechar menu ao clicar fora
    document.addEventListener('click', (e) => {
        if (navMenu.classList.contains('active') && !navMenu.contains(e.target) && !hamburger.contains(e.target)) {
            closeMenu();
        }
    });
}

// Header Shadow on Scroll
const header = document.querySelector('header');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
}, { passive: true });

// Back to Top Button
const backToTopButton = document.querySelector('.back-to-top');

if (backToTopButton) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopButton.classList.add('show');
        } else {
            backToTopButton.classList.remove('show');
        }
    }, { passive: true });

    backToTopButton.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// Typewriter Effect
const typewriterElement = document.querySelector('.typewriter-text');
const cursorElement = document.querySelector('.cursor');
const phrases = ["visitantes em clientes.", "ideias em inovação.", "código em resultados."];
let phraseIndex = 0;
let charIndex = 0;
let isDeleting = false;

// --- Som de Teclado Mecânico ---
// Para produção, baixe um som e use algo como: new Audio('audio/tecla.mp3');
const keySound = new Audio('https://www.soundjay.com/mechanical/sounds/mechanical-keyboard-single-button-press-1.mp3');
keySound.volume = 0.3; // Volume ajustado para 30% (suave)

// Controle de Som
let isSoundEnabled = true;
const toggleSoundBtn = document.getElementById('toggle-sound');

if (toggleSoundBtn) {
    toggleSoundBtn.addEventListener('click', () => {
        isSoundEnabled = !isSoundEnabled;
        const iconOn = toggleSoundBtn.querySelector('.sound-icon.on');
        const iconOff = toggleSoundBtn.querySelector('.sound-icon.off');
        
        if (isSoundEnabled) {
            iconOn.style.display = 'block';
            iconOff.style.display = 'none';
            toggleSoundBtn.setAttribute('aria-label', 'Desligar som');
        } else {
            iconOn.style.display = 'none';
            iconOff.style.display = 'block';
            toggleSoundBtn.setAttribute('aria-label', 'Ligar som');
        }
    });
}

function typeWriter() {
    if (!typewriterElement) return;

    const currentPhrase = phrases[phraseIndex];

    if (isDeleting) {
        typewriterElement.textContent = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
    } else {
        typewriterElement.textContent = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
        
        if (isSoundEnabled) {
            // Toca o som ao digitar
            const sound = keySound.cloneNode(); // Clona para permitir sons rápidos sobrepostos
            sound.volume = 0.3;
            // Varia o tom (playbackRate) entre 0.9 e 1.1 para parecer mais natural
            sound.playbackRate = Math.random() * (1.1 - 0.9) + 0.9;
            sound.play().catch(() => { /* Ignora erro se o usuário ainda não interagiu com a página */ });
        }
    }

    let typeSpeed = 100;

    if (!isDeleting && charIndex === currentPhrase.length) {
        typeSpeed = 2000; // Pausa ao terminar a frase
        isDeleting = true;
        if (cursorElement) cursorElement.classList.remove('typing'); // Pausa: volta a piscar
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        typeSpeed = 500; // Pausa antes de começar a próxima
        if (isDeleting) {
            typeSpeed /= 2; // Apagar é mais rápido
        }
        if (cursorElement) cursorElement.classList.add('typing'); // Digitando: cursor sólido
    }

    setTimeout(typeWriter, typeSpeed);
}

if (typewriterElement) {
    setTimeout(typeWriter, 500); // Delay inicial antes de começar
}

// Stats Counter Animation
const statsSection = document.querySelector('.stats-section');
const counters = document.querySelectorAll('.counter');
let started = false; // Garante que a animação rode apenas uma vez

if (statsSection && counters.length > 0) {
    const statsObserver = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting && !started) {
            counters.forEach(counter => {
                const target = +counter.getAttribute('data-target');
                const duration = 2000; // Duração da animação em ms
                const increment = target / (duration / 16); // 60fps

                let current = 0;
                const updateCounter = () => {
                    current += increment;
                    if (current < target) {
                        counter.innerText = Math.ceil(current);
                        requestAnimationFrame(updateCounter);
                    } else {
                        counter.innerText = target;
                    }
                };
                updateCounter();
            });
            started = true;
        }
    }, { threshold: 0.5 });

    statsObserver.observe(statsSection);
}

// 3D Tilt Effect for Service Cards
const serviceCards = document.querySelectorAll('.service-card');

if (serviceCards.length > 0) {
    serviceCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateX = ((y - centerY) / centerY) * -8; // Intensidade da rotação X
            const rotateY = ((x - centerX) / centerX) * 8;  // Intensidade da rotação Y

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
            card.style.transition = 'transform 0.1s ease'; // Transição rápida para seguir o mouse
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)';
            card.style.transition = 'transform 0.5s ease'; // Retorno suave
        });
    });
}

// Testimonials Carousel
const track = document.querySelector('.carousel-track');
const slides = track ? Array.from(track.children) : [];
const nextButton = document.querySelector('.next-btn');
const prevButton = document.querySelector('.prev-btn');
const dotsContainer = document.querySelector('.carousel-dots');

if (track && slides.length > 0) {
    // Criar bolinhas (dots)
    slides.forEach((_, index) => {
        const dot = document.createElement('div');
        dot.classList.add('dot');
        if (index === 0) dot.classList.add('active');
        dotsContainer.appendChild(dot);
        
        dot.addEventListener('click', () => {
            moveToSlide(index);
        });
    });

    const dots = Array.from(dotsContainer.children);
    let currentSlideIndex = 0;

    const moveToSlide = (index) => {
        track.style.transform = 'translateX(-' + (index * 100) + '%)';
        dots[currentSlideIndex].classList.remove('active');
        dots[index].classList.add('active');
        currentSlideIndex = index;
    };

    nextButton.addEventListener('click', () => {
        const nextIndex = (currentSlideIndex + 1) % slides.length;
        moveToSlide(nextIndex);
    });

    prevButton.addEventListener('click', () => {
        const prevIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
        moveToSlide(prevIndex);
    });
    
    // Auto-play
    setInterval(() => {
        const nextIndex = (currentSlideIndex + 1) % slides.length;
        moveToSlide(nextIndex);
    }, 5000);
}

// Particles Effect in Hero
const canvas = document.getElementById('particles-canvas');

if (canvas) {
    const ctx = canvas.getContext('2d');
    let particlesArray;
    let animationId;

    // Ajustar tamanho do canvas
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;

    // Mouse Interaction
    const mouse = {
        x: null,
        y: null,
        radius: 100
    }

    const heroSection = document.querySelector('.hero');
    
    heroSection.addEventListener('mousemove', (event) => {
        const rect = heroSection.getBoundingClientRect();
        mouse.x = event.clientX - rect.left;
        mouse.y = event.clientY - rect.top;
    });

    heroSection.addEventListener('mouseleave', () => {
        mouse.x = null;
        mouse.y = null;
    });

    window.addEventListener('resize', () => {
        canvas.width = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;
        init();
    });

    class Particle {
        constructor(x, y, directionX, directionY, size, color) {
            this.x = x;
            this.y = y;
            this.directionX = directionX;
            this.directionY = directionY;
            this.size = size;
            this.color = color;
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
            ctx.fillStyle = this.color;
            ctx.fill();
        }

        update() {
            if (this.x > canvas.width || this.x < 0) {
                this.directionX = -this.directionX;
            }
            if (this.y > canvas.height || this.y < 0) {
                this.directionY = -this.directionY;
            }

            this.x += this.directionX;
            this.y += this.directionY;
            this.draw();
        }
    }

    function init() {
        particlesArray = [];
        let numberOfParticles = (canvas.height * canvas.width) / 9000;
        for (let i = 0; i < numberOfParticles; i++) {
            let size = (Math.random() * 2) + 1;
            let x = (Math.random() * ((canvas.width - size * 2) - (size * 2)) + size * 2);
            let y = (Math.random() * ((canvas.height - size * 2) - (size * 2)) + size * 2);
            let directionX = (Math.random() * 1) - 0.5;
            let directionY = (Math.random() * 1) - 0.5;
            let color = 'rgba(255, 255, 255, 0.7)';

            particlesArray.push(new Particle(x, y, directionX, directionY, size, color));
        }
    }

    function connect() {
        for (let a = 0; a < particlesArray.length; a++) {
            // Conexão entre partículas próximas
            for (let b = a; b < particlesArray.length; b++) {
                let distance = ((particlesArray[a].x - particlesArray[b].x) * (particlesArray[a].x - particlesArray[b].x))
                    + ((particlesArray[a].y - particlesArray[b].y) * (particlesArray[a].y - particlesArray[b].y));
                
                if (distance < (canvas.width/7) * (canvas.height/7)) {
                    let opacityValue = 1 - (distance/20000);
                    if(opacityValue > 0) {
                        ctx.strokeStyle = 'rgba(255, 255, 255,' + opacityValue * 0.2 + ')';
                        ctx.lineWidth = 1;
                        ctx.beginPath();
                        ctx.moveTo(particlesArray[a].x, particlesArray[a].y);
                        ctx.lineTo(particlesArray[b].x, particlesArray[b].y);
                        ctx.stroke();
                    }
                }
            }
            
            // Conexão com mouse
            if (mouse.x != null) {
                let dx = mouse.x - particlesArray[a].x;
                let dy = mouse.y - particlesArray[a].y;
                let distanceMouse = (dx*dx + dy*dy);
                if (distanceMouse < mouse.radius * mouse.radius) {
                    ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
                    ctx.lineWidth = 1;
                    ctx.beginPath();
                    ctx.moveTo(particlesArray[a].x, particlesArray[a].y);
                    ctx.lineTo(mouse.x, mouse.y);
                    ctx.stroke();
                }
            }
        }
    }

    function animate() {
        animationId = requestAnimationFrame(animate);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < particlesArray.length; i++) {
            particlesArray[i].update();
        }
        connect();
    }

    init();
    
    // Otimização: Pausa a animação quando não está visível para economizar CPU/Bateria
    const heroObserver = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
            if (!animationId) animate();
        } else {
            cancelAnimationFrame(animationId);
            animationId = null;
        }
    });
    heroObserver.observe(heroSection);
}

// Discount Modal (Popup)
const modal = document.getElementById('discount-modal');
const closeModalBtn = document.querySelector('.close-modal');
const claimDiscountBtn = document.getElementById('claim-discount');

if (modal) {
    // Mostrar modal após 10 segundos
    setTimeout(() => {
        modal.classList.add('show');
    }, 10000);

    // Função para fechar o modal
    const closeModal = () => {
        modal.classList.remove('show');
    };

    if (closeModalBtn) {
        closeModalBtn.addEventListener('click', closeModal);
    }

    if (claimDiscountBtn) {
        claimDiscountBtn.addEventListener('click', closeModal);
    }

    // Fechar ao clicar fora do conteúdo
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });
}

// Blog Search Filter
const blogSearchInput = document.getElementById('blog-search-input');
const blogCards = document.querySelectorAll('.blog-card');

if (blogSearchInput) {
    blogSearchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase();

        blogCards.forEach(card => {
            const title = card.querySelector('h3').textContent.toLowerCase();
            const description = card.querySelector('p').textContent.toLowerCase();
            const category = card.querySelector('.blog-category').textContent.toLowerCase();

            if (title.includes(searchTerm) || description.includes(searchTerm) || category.includes(searchTerm)) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    });
}

// --- Preloader Logic ---
window.addEventListener('load', () => {
    const preloader = document.getElementById('preloader');
    if (preloader) {
        preloader.style.opacity = '0';
        preloader.style.visibility = 'hidden';
        document.body.classList.add('loaded'); // Triggers hero animations
        
        // Remove do DOM após a transição
        setTimeout(() => {
            preloader.style.display = 'none';
        }, 500);
    } else {
        document.body.classList.add('loaded');
    }
});

// --- Reading Progress Bar ---
window.addEventListener('scroll', () => {
    const progressBar = document.getElementById("myBar");
    if (progressBar) {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        progressBar.style.width = scrolled + "%";
    }
});

// --- Hero Parallax Effect ---
const heroParallax = document.querySelector('.hero');
if (heroParallax) {
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        // Move o background a 50% da velocidade do scroll (efeito de profundidade)
        heroParallax.style.backgroundPositionY = `${scrolled * 0.5}px`;
    });
}

// --- Logo Scroller Animation ---
const scrollers = document.querySelectorAll(".logo-scroller");

function addAnimation() {
    scrollers.forEach((scroller) => {
        scroller.setAttribute("data-animated", true);

        const scrollerInner = scroller.querySelector(".logo-scroller__inner");
        const scrollerContent = Array.from(scrollerInner.children);

        scrollerContent.forEach((item) => {
            const duplicatedItem = item.cloneNode(true);
            duplicatedItem.setAttribute("aria-hidden", true);
            scrollerInner.appendChild(duplicatedItem);
        });
    });
}

if (scrollers.length > 0 && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    addAnimation();
}

// --- Sistema de Blog Dinâmico ---
const blogPosts = {
    "seo-basico": {
        title: "5 Dicas de SEO para Iniciantes",
        category: "SEO",
        date: "12 Out 2023",
        readTime: "5 min leitura",
        image: "https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a?auto=format&fit=crop&w=1200&q=80",
        content: `
            <p class="lead">Você sabia que a maioria das experiências online começa com uma pesquisa no Google? Se o seu site não aparece na primeira página, você está perdendo dinheiro. O SEO (Search Engine Optimization) não é mágica, é engenharia e conteúdo. Aqui estão 5 dicas práticas e detalhadas para mudar o jogo.</p>
            
            <h2>1. Pesquisa de Palavras-chave: A Fundação</h2>
            <p>Antes de escrever qualquer coisa, você precisa saber o que seu público está procurando. Não adianta escrever sobre "conserto de computadores" se todo mundo pesquisa por "assistência técnica PC".</p>
            <ul>
                <li><strong>Use ferramentas:</strong> Google Keyword Planner, Ubersuggest ou SEMrush.</li>
                <li><strong>Foque em Cauda Longa:</strong> Em vez de tentar ranquear para "tênis" (muito concorrido), tente "tênis de corrida para iniciantes". O volume é menor, mas a intenção de compra é maior.</li>
                <li><strong>Analise a concorrência:</strong> Veja o que quem está em primeiro lugar escreveu e faça melhor.</li>
            </ul>

            <h2>2. Conteúdo de Qualidade e Relevância</h2>
            <p>O Google prioriza conteúdo que resolve o problema do usuário. O algoritmo E-E-A-T (Experiência, Especialização, Autoridade e Confiabilidade) é crucial.</p>
            <p>Escreva textos originais, bem estruturados e que entreguem valor real. Evite blocos enormes de texto; use parágrafos curtos, listas e imagens para quebrar a leitura.</p>

            <h2>3. Otimização On-Page: O Básico Bem Feito</h2>
            <p>Facilite a vida do robô do Google. Ele precisa ler seu código para entender seu conteúdo.</p>
            <ul>
                <li><strong>Title Tag:</strong> O título que aparece na aba do navegador. Deve conter a palavra-chave principal.</li>
                <li><strong>Meta Description:</strong> O resumo que aparece nos resultados da busca. Funciona como um anúncio para atrair o clique.</li>
                <li><strong>Hierarquia de Cabeçalhos (H1, H2, H3):</strong> Use apenas um H1 por página (o título principal) e organize os subtemas com H2 e H3.</li>
                <li><strong>URLs Amigáveis:</strong> Evite <code>site.com/p=123</code>. Prefira <code>site.com/dicas-de-seo</code>.</li>
            </ul>

            <h2>4. Velocidade e Experiência do Usuário (Core Web Vitals)</h2>
            <p>Sites lentos são penalizados. O Google não quer enviar usuários para páginas que demoram a carregar ou que mudam de lugar enquanto carregam (CLS).</p>
            <p>Otimize suas imagens (use WebP), minifique arquivos CSS e JavaScript e use um bom serviço de hospedagem. A experiência mobile é prioritária: seu site deve ser perfeito no celular.</p>

            <h2>5. Link Building e Autoridade</h2>
            <p>Links de outros sites apontando para o seu funcionam como "votos de confiança". Quanto mais sites relevantes linkarem para você, mais autoridade seu domínio ganha.</p>
            <p>Crie conteúdo compartilhável, faça parcerias (guest posts) e divulgue seus artigos nas redes sociais para atrair tráfego natural.</p>`
    },
    "performance-web": {
        title: "Por que seu site está lento?",
        category: "Performance",
        date: "15 Out 2023",
        readTime: "4 min leitura",
        image: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1200&q=80",
        content: `
            <p class="lead">A velocidade de carregamento impacta diretamente nas suas vendas. Estudos mostram que um atraso de apenas 1 segundo no carregamento pode reduzir as conversões em 7%. Se seu site demora 3 segundos, 40% dos usuários já foram embora.</p>
            
            <h2>O que são Core Web Vitals?</h2>
            <p>O Google usa métricas específicas para medir a experiência do usuário, chamadas de Core Web Vitals:</p>
            <ul>
                <li><strong>LCP (Largest Contentful Paint):</strong> Mede quanto tempo leva para o maior elemento da tela (geralmente uma imagem ou título) aparecer. O ideal é menos de 2.5s.</li>
                <li><strong>INP (Interaction to Next Paint):</strong> Substituiu o FID. Mede a responsividade do site a cliques e interações.</li>
                <li><strong>CLS (Cumulative Layout Shift):</strong> Mede a estabilidade visual. Sabe quando você vai clicar em um botão e ele muda de lugar porque uma imagem carregou em cima? Isso é um CLS ruim.</li>
            </ul>

            <h2>Vilão #1: Imagens Pesadas</h2>
            <p>Imagens não otimizadas são a causa número 1 de lentidão. Uma foto tirada do celular pode ter 5MB. Na web, ela deveria ter 100KB.</p>
            <p><strong>Solução:</strong> Converta imagens para formatos modernos como WebP ou AVIF e use compressão. Implemente <em>Lazy Loading</em> para carregar imagens apenas quando elas aparecem na tela.</p>

            <h2>Vilão #2: Excesso de Scripts (JavaScript)</h2>
            <p>Muitos plugins, chats online, pixels de rastreamento e animações pesadas bloqueiam o navegador de desenhar a página.</p>
            <p><strong>Solução:</strong> Audite seus scripts. Remova o que não usa. Carregue scripts de terceiros com <code>async</code> ou <code>defer</code>.</p>

            <h2>Vilão #3: Hospedagem Ruim</h2>
            <p>Se o servidor demora para responder (TTFB alto), nenhuma otimização de código vai salvar seu site. Hospedagens compartilhadas baratas costumam ser o gargalo.</p>
            <p>Invista em uma hospedagem de qualidade, preferencialmente com servidores próximos ao seu público-alvo ou usando uma CDN (Content Delivery Network) como Cloudflare.</p>`
    },
    "landing-vs-institucional": {
        title: "Landing Page vs Site Institucional",
        category: "Marketing",
        date: "20 Out 2023",
        readTime: "6 min leitura",
        image: "https://images.unsplash.com/photo-1533750349088-cd871a92f312?auto=format&fit=crop&w=1200&q=80",
        content: `
            <p class="lead">Muitos empresários investem dinheiro em tráfego pago (Google Ads, Facebook Ads) e enviam os visitantes para a página inicial do site. Isso é jogar dinheiro fora. Entenda a diferença crucial entre Landing Page e Site Institucional.</p>
            
            <h2>O que é um Site Institucional?</h2>
            <p>É a "casa" da sua empresa na internet. Ele serve para construir autoridade, apresentar a história, a equipe, todos os serviços, o blog e formas de contato.</p>
            <p><strong>Objetivo:</strong> Informar, educar e criar branding.</p>
            <p><strong>Estrutura:</strong> Menu de navegação completo, links para redes sociais, várias páginas internas. O usuário tem liberdade para explorar.</p>

            <h2>O que é uma Landing Page?</h2>
            <p>É uma página de aterrissagem criada com um <strong>único objetivo</strong>: conversão. Pode ser vender um produto, capturar um lead (email/telefone) ou agendar uma reunião.</p>
            <p><strong>Objetivo:</strong> Fazer o usuário tomar UMA ação específica.</p>
            <p><strong>Estrutura:</strong> Sem menu de navegação (para o usuário não fugir), copy persuasiva, prova social (depoimentos), e botões de CTA (Call to Action) claros e repetidos.</p>

            <h2>Qual escolher?</h2>
            <ul>
                <li><strong>Use Site Institucional quando:</strong> O cliente está na fase de pesquisa, quer conhecer a empresa, ou quando você precisa de SEO para longo prazo em vários tópicos.</li>
                <li><strong>Use Landing Page quando:</strong> Você está pagando por anúncios. Se você anuncia "Consultoria Financeira", o link deve ir para uma página que fala SÓ sobre isso e tem um formulário de contato, não para a home do site onde ele vai se perder.</li>
            </ul>
            
            <h2>A Estratégia Vencedora</h2>
            <p>Tenha os dois. Use o site institucional para tráfego orgânico e fortalecimento de marca. Crie landing pages específicas para cada campanha de marketing ou produto que você promover ativamente.</p>`
    },
    "design-trends-2024": {
        title: "Tendências de Web Design 2024",
        category: "Design",
        date: "25 Out 2023",
        readTime: "3 min leitura",
        image: "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?auto=format&fit=crop&w=1200&q=80",
        content: `
            <p class="lead">O web design evolui rápido. O que era moderno há 3 anos hoje parece datado. Para 2024, a palavra de ordem é imersão e usabilidade. Veja o que está dominando a web.</p>
            
            <h2>1. Bento Grids</h2>
            <p>Inspirado nas marmitas japonesas e popularizado pela Apple, o layout em "Bento Grid" organiza o conteúdo em caixas modulares de diferentes tamanhos. É visualmente organizado, responsivo e permite destacar informações importantes de forma hierárquica.</p>

            <h2>2. Modo Escuro (Dark Mode)</h2>
            <p>Não é mais apenas uma preferência, é uma expectativa. Sites que oferecem alternância para modo escuro proporcionam conforto visual e economia de bateria em dispositivos OLED. O design escuro também transmite sofisticação e modernidade.</p>

            <h2>3. Micro-interações e Animações de Scroll</h2>
            <p>Sites estáticos são chatos. Micro-interações são aquelas pequenas animações quando você passa o mouse sobre um botão, ou quando um elemento reage ao clique. O "Scrollytelling" (contar histórias através do scroll) mantém o usuário engajado enquanto ele navega pela página.</p>

            <h2>4. Tipografia Gigante e Negrito</h2>
            <p>O minimalismo continua, mas agora com tipografia como elemento central de design. Títulos enormes, fontes sans-serif grossas e contrastantes substituem o excesso de imagens, comunicando a mensagem de forma direta e impactante.</p>

            <h2>5. Acessibilidade como Padrão</h2>
            <p>Design inclusivo não é tendência, é obrigação. Contraste de cores adequado, navegação por teclado e suporte a leitores de tela estão sendo integrados desde a fase de prototipagem, não como um "puxadinho" no final do projeto.</p>`
    },
    "ga4-guia": {
        title: "Entendendo o Google Analytics 4",
        category: "Dados",
        date: "28 Out 2023",
        readTime: "8 min leitura",
        image: "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?auto=format&fit=crop&w=1200&q=80",
        content: `
            <p class="lead">O Universal Analytics morreu. O GA4 é o novo padrão e ele mudou fundamentalmente a forma como medimos dados na web. Agora, tudo é baseado em eventos, não mais em sessões.</p>
            
            <h2>A Mudança de Paradigma: Eventos</h2>
            <p>No GA antigo, o foco era a "Sessão" (uma visita). No GA4, o foco é o "Usuário" e o que ele faz. Cada clique, rolagem de página, download ou visualização de vídeo é um <strong>Evento</strong>.</p>
            <p>Isso permite um rastreamento muito mais flexível e detalhado da jornada do usuário, inclusive cruzando dados entre site e aplicativo.</p>

            <h2>Métricas que Mudaram</h2>
            <ul>
                <li><strong>Taxa de Rejeição (Bounce Rate):</strong> Perdeu relevância. Agora olhamos para a <strong>Taxa de Engajamento</strong>. Uma sessão engajada é aquela que durou mais de 10s, teve uma conversão ou viu 2+ páginas.</li>
                <li><strong>Sessões:</strong> A contagem pode ser diferente do UA devido à forma como o GA4 agrupa interações.</li>
            </ul>

            <h2>Configurando Conversões</h2>
            <p>No GA4, você define quais eventos são importantes e os marca como "Conversão".</p>
            <ol>
                <li>Vá em Administrador > Eventos.</li>
                <li>Crie um evento personalizado (ex: <code>generate_lead</code> quando alguém envia o formulário).</li>
                <li>Marque a chave "Marcar como conversão".</li>
            </ol>

            <h2>Relatórios de Exploração</h2>
            <p>A aba "Explorar" é o poder real do GA4. Ela permite criar funis personalizados, análise de caminho (path exploration) e sobreposição de segmentos. É ali que você descobre onde os usuários estão desistindo da compra.</p>`
    },
    "email-marketing": {
        title: "Email Marketing ainda funciona?",
        category: "Marketing",
        date: "01 Nov 2023",
        readTime: "5 min leitura",
        image: "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1200&q=80",
        content: `
            <p class="lead">Com o hype das redes sociais e TikTok, muitos dizem que o email morreu. Estão errados. O Email Marketing continua sendo o canal com maior ROI (Retorno sobre Investimento) no marketing digital: média de $36 para cada $1 investido.</p>
            
            <h2>Por que o Email é Poderoso?</h2>
            <p><strong>1. É terreno próprio:</strong> Nas redes sociais, o algoritmo decide quem vê seu post (geralmente menos de 5% dos seguidores). No email, a entrega é direta na caixa de entrada.</p>
            <p><strong>2. É pessoal:</strong> O email é um canal de comunicação um-para-um. É onde as pessoas tratam de trabalho e assuntos sérios.</p>

            <h2>O Segredo: Segmentação</h2>
            <p>O "Email Blast" (enviar a mesma mensagem para todos) não funciona mais. O segredo é a segmentação.</p>
            <ul>
                <li>Se o cliente comprou ração de cachorro, não envie oferta de areia de gato.</li>
                <li>Se o lead baixou um ebook sobre SEO, envie dicas avançadas de SEO, não de Design.</li>
            </ul>
            <p>Ferramentas como Mailchimp, ActiveCampaign ou RD Station permitem criar essas regras automaticamente.</p>

            <h2>Automação de Marketing</h2>
            <p>Você não precisa enviar emails manualmente. Crie fluxos automáticos:</p>
            <ul>
                <li><strong>Boas-vindas:</strong> Envie um cupom ou conteúdo exclusivo assim que a pessoa se cadastrar.</li>
                <li><strong>Carrinho Abandonado:</strong> O cliente colocou o produto no carrinho e saiu? Envie um lembrete 1 hora depois. Isso recupera cerca de 10-20% das vendas perdidas.</li>
                <li><strong>Pós-venda:</strong> Peça um review ou ofereça um produto complementar 7 dias após a compra.</li>
            </ul>

            <h2>Dica de Ouro: Limpeza de Lista</h2>
            <p>Ter 10.000 contatos onde apenas 500 abrem é pior do que ter 1.000 contatos onde 500 abrem. Provedores de email (Gmail, Outlook) penalizam remetentes com baixo engajamento. Remova periodicamente quem não interage há mais de 6 meses.</p>`
    }
};

// Lógica para carregar o artigo na página artigo.html
if (window.location.pathname.includes('artigo.html')) {
    const params = new URLSearchParams(window.location.search);
    const articleId = params.get('id');
    const post = blogPosts[articleId];

    if (post) {
        document.title = `${post.title} - Cybernex Blog`;
        document.getElementById('article-category').textContent = post.category;
        document.getElementById('article-title').textContent = post.title;
        document.getElementById('article-date').textContent = post.date;
        document.getElementById('article-read-time').textContent = post.readTime;
        document.getElementById('article-img').src = post.image;
        document.getElementById('article-img').alt = post.title;
        document.getElementById('article-body').innerHTML = post.content;
    } else {
        // Artigo não encontrado (Redireciona ou mostra erro)
        document.querySelector('.article-content').innerHTML = "<h1>Artigo não encontrado.</h1><p>O artigo que você procura não existe ou foi removido.</p>";
        document.querySelector('.article-image').style.display = 'none';
        document.querySelector('.article-header').style.display = 'none';
    }
}