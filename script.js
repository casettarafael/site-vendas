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

// Smooth Scroll para links internos
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
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
    });

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
        requestAnimationFrame(animate);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < particlesArray.length; i++) {
            particlesArray[i].update();
        }
        connect();
    }

    init();
    animate();
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