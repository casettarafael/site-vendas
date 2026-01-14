document.addEventListener('DOMContentLoaded', () => {

    // --- Preloader Logic (Prioridade Máxima) ---
    // Movido para o topo para garantir que o site apareça mesmo se houver erros abaixo
    function removePreloader() {
        const preloader = document.getElementById('preloader');
        if (preloader) {
            preloader.style.opacity = '0';
            preloader.style.visibility = 'hidden';
            document.body.classList.add('loaded'); 
            setTimeout(() => { preloader.style.display = 'none'; }, 500);
        } else {
            document.body.classList.add('loaded');
        }
    }
    setTimeout(removePreloader, 100);
    window.addEventListener('load', removePreloader);

    // Lógica do Accordion (FAQ)
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');

            // Fecha todos os outros itens para um comportamento de acordeão clássico
            faqItems.forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove('active');
                    otherItem.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
                }
            });

            // Alterna o item atual
            item.classList.toggle('active');
            question.setAttribute('aria-expanded', String(!isActive));
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
        const orcamento = document.getElementById('orcamento') ? document.getElementById('orcamento').value : '';

        // Formata a mensagem para o WhatsApp
        let message = `*Novo Contato do Site*\n\n*Nome:* ${nome}\n`;
        if (empresa) message += `*Empresa:* ${empresa}\n`;
        if (telefone) message += `*Telefone:* ${telefone}\n`;
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
});
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
// Otimização: Inicializa vazio e só carrega se necessário (Lazy Load)
let keySound;

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
            if (!keySound) {
                // Carrega o áudio apenas na primeira vez que for necessário
                keySound = new Audio('https://www.soundjay.com/mechanical/sounds/mechanical-keyboard-single-button-press-1.mp3');
                keySound.volume = 0.3;
            }
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
        // Otimização: Cache do tamanho do elemento para evitar cálculos pesados constantes
        let rect = card.getBoundingClientRect();

        // Atualiza as coordenadas apenas ao entrar no card
        card.addEventListener('mouseenter', () => {
            rect = card.getBoundingClientRect();
        });

        card.addEventListener('mousemove', (e) => {
            // Otimização: requestAnimationFrame sincroniza com a taxa de atualização da tela (60fps)
            requestAnimationFrame(() => {
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;

                const centerX = rect.width / 2;
                const centerY = rect.height / 2;

                const rotateX = ((y - centerY) / centerY) * -8;
                const rotateY = ((x - centerX) / centerX) * 8;

                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
            });
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)';
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
    let autoPlayInterval = setInterval(() => {
        const nextIndex = (currentSlideIndex + 1) % slides.length;
        moveToSlide(nextIndex);
    }, 5000);

    // Pausa no hover para melhor UX e acessibilidade
    const carouselContainer = document.querySelector('.carousel-container');
    carouselContainer.addEventListener('mouseenter', () => {
        clearInterval(autoPlayInterval);
    });
    carouselContainer.addEventListener('mouseleave', () => {
        autoPlayInterval = setInterval(() => {
            const nextIndex = (currentSlideIndex + 1) % slides.length;
            moveToSlide(nextIndex);
        }, 5000);
    });
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
        // Otimização: Redu
        let numberOfParticles = (canvas.height * canvas.width) / 25000;
        if (numberOfParticles > 80) numberOfParticles = 80; // Limite máximo fixo
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

// --- Blog Pagination ---
const blogGrid = document.querySelector('.blog-grid');
if (blogGrid) {
    const articles = Array.from(blogGrid.querySelectorAll('.blog-card'));
    const prevPageBtn = document.getElementById('prev-page');
    const nextPageBtn = document.getElementById('next-page');
    const pageIndicator = document.getElementById('page-indicator');
    const paginationContainer = document.querySelector('.blog-pagination');
    
    const itemsPerPage = 3; // Defina quantos artigos por página
    let currentPage = 1;
    const totalPages = Math.ceil(articles.length / itemsPerPage);

    function showPage(page) {
        currentPage = page;
        const startIndex = (page - 1) * itemsPerPage;
        const endIndex = startIndex + itemsPerPage;

        articles.forEach((article, index) => {
            article.style.display = (index >= startIndex && index < endIndex) ? 'flex' : 'none';
        });

        if (pageIndicator) pageIndicator.textContent = `Página ${currentPage} de ${totalPages}`;
        if (prevPageBtn) prevPageBtn.disabled = currentPage === 1;
        if (nextPageBtn) nextPageBtn.disabled = currentPage === totalPages;
    }

    if (articles.length > itemsPerPage && paginationContainer) {
        prevPageBtn.addEventListener('click', () => {
            if (currentPage > 1) showPage(currentPage - 1);
        });
        nextPageBtn.addEventListener('click', () => {
            if (currentPage < totalPages) showPage(currentPage + 1);
        });
        showPage(1); // Exibe a primeira página inicialmente
    } else if (paginationContainer) {
        paginationContainer.style.display = 'none'; // Esconde a paginação se não for necessária
    }
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
        // Após a busca, reaplica a paginação para os itens visíveis
        // Esta parte pode ser complexa. Uma abordagem mais simples é desativar a paginação durante a busca.
        const pagination = document.querySelector('.blog-pagination');
        if (pagination) pagination.style.display = searchTerm ? 'none' : 'flex';
        if (!searchTerm) showPage(1); // Volta para a primeira página quando a busca é limpa
    });
}

// --- Reading Progress Bar ---
window.addEventListener('scroll', () => {
    const progressBar = document.getElementById("myBar");
    if (progressBar) {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        progressBar.style.width = scrolled + "%";
    }
}, { passive: true });
// --- Hero Parallax Effect ---
const heroParallax = document.querySelector('.hero');
if (heroParallax) {
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        // Move o background a 50% da velocidade do scroll (efeito de profundidade)
        heroParallax.style.backgroundPositionY = `${scrolled * 0.5}px`;
    }, { passive: true });
}

// --- Logo Scroller Animation ---
const scrollers = document.querySelectorAll(".logo-scroller");

if (scrollers.length > 0 && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    addAnimation();
}

/**
 * Clona os itens do scroller para criar um loop infinito.
 */
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

// --- Dynamic Footer Year ---
const yearSpan = document.getElementById('current-year');
if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear().toString();
}

// Lógica para carregar o artigo na página artigo.html
if (window.location.pathname.includes('artigo.html')) {
    
    /* 
       OTIMIZAÇÃO: O conteúdo do blog agora só é definido se estivermos na página de artigo.
       Isso economiza memória e tempo de processamento na Home Page.
    */
    // A variável blogPosts agora é carregada do arquivo dados-blog.js
    // Isso evita que o texto pesado seja baixado na Home Page.

    const params = new URLSearchParams(window.location.search);
    const articleId = params.get('id');
    
    // Verifica se o arquivo externo foi carregado corretamente
    const post = (typeof blogPosts !== 'undefined') ? blogPosts[articleId] : null;

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

// --- Lógica para Landing Pages Locais (local.html) ---
if (window.location.pathname.includes('local.html')) {
    const params = new URLSearchParams(window.location.search);
    const geoSlug = params.get('geo');

    if (geoSlug) {
        // Função para formatar slug: "rio-de-janeiro" -> "Rio de Janeiro"
        const formatCityName = (slug) => {
            return slug.split('-').map(word => {
                // Exceções para preposições (de, da, do, dos)
                if (['de', 'da', 'do', 'dos', 'e'].includes(word)) return word;
                return word.charAt(0).toUpperCase() + word.slice(1);
            }).join(' ');
        };

        const cityName = formatCityName(geoSlug);
        const pageTitle = `Criação de Sites em ${cityName} - Web Design Profissional`;
        const metaDesc = `Procurando criação de sites em ${cityName}? A Cybernex desenvolve sites rápidos e otimizados para empresas de ${cityName} e região. Peça um orçamento!`;

        // 1. Atualizar Meta Tags (SEO)
        document.title = pageTitle;
        document.querySelector('meta[name="description"]').setAttribute('content', metaDesc);
        
        // Atualizar Canonical para evitar conteúdo duplicado (aponta para a URL atual)
        const canonicalLink = document.getElementById('dynamic-canonical');
        if (canonicalLink) {
            canonicalLink.href = window.location.href;
        }

        // 2. Injetar Nome da Cidade nos Elementos
        const elementsToUpdate = [
            { id: 'city-name-hero', text: cityName },
            { id: 'city-name-text', text: cityName },
            { id: 'city-name-btn', text: cityName },
            { id: 'city-name-subtitle', text: cityName },
            { id: 'city-name-seo', text: cityName },
            { id: 'city-name-form', text: cityName },
            { id: 'city-name-footer', text: cityName }
        ];

        elementsToUpdate.forEach(item => {
            const el = document.getElementById(item.id);
            if (el) el.textContent = item.text;
        });

        // 3. Atualizar campo oculto do formulário
        const hiddenInput = document.getElementById('cidade-origem');
        if (hiddenInput) hiddenInput.value = cityName;

        // 4. Enviar evento personalizado para o Google Analytics
        if (typeof gtag === 'function') {
            gtag('event', 'acesso_cidade', {
                'city_name': cityName,
                'geo_slug': geoSlug
            });
        }

    } else {
        // Se não tiver parâmetro, redireciona para home ou define padrão
        // window.location.href = 'index.html'; // Opcional
        const defaultName = "Todo o Brasil";
        document.getElementById('city-name-hero').textContent = defaultName;
        // ... atualizar outros elementos com padrão se necessário
    }
}

}); // Fim do DOMContentLoaded