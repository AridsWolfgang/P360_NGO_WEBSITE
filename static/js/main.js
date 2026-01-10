document.addEventListener('DOMContentLoaded', function () {
    // Language data with flags (using emoji flags for simplicity)
    const languages = [
        { code: 'en', name: 'English', flag: '🇺🇸', welcome: 'Welcome to Prosperity360' },
        { code: 'fr', name: 'Français', flag: '🇫🇷', welcome: 'Bienvenue à Prosperity360' },
        { code: 'ar', name: 'العربية', flag: '🇸🇦', welcome: 'مرحبًا بكم في Prosperity360' },
    ];

    // DOM elements
    const translateBtn = document.getElementById('translateBtn');
    const languageDropdown = document.getElementById('languageDropdown');
    const languageList = document.getElementById('languageList');
    const currentLangElement = document.getElementById('currentLang');
    const welcomeTextElement = document.querySelector('.welcome-text');
    const displayCurrentLang = document.getElementById('displayCurrentLang');

    // Current language
    let currentLanguage = languages[0];

    // Populate language list
    function populateLanguageList() {
        languageList.innerHTML = '';

        languages.forEach(language => {
            const li = document.createElement('li');
            li.dataset.code = language.code;

            // Create flag element
            const flagSpan = document.createElement('span');
            flagSpan.className = 'language-flag';
            flagSpan.textContent = language.flag;

            // Create language name element
            const nameSpan = document.createElement('span');
            nameSpan.textContent = language.name;

            li.appendChild(flagSpan);
            li.appendChild(nameSpan);

            // Mark if this is the current language
            if (language.code === currentLanguage.code) {
                li.classList.add('selected');
            }

            // Add click event
            li.addEventListener('click', () => selectLanguage(language));

            languageList.appendChild(li);
        });
    }

    // Select a language
    function selectLanguage(language) {
        currentLanguage = language;

        // Update button text
        currentLangElement.textContent = language.name;

        // Update welcome text
        const prosperitySpan = document.createElement('span');
        prosperitySpan.className = 'prosperity-text';
        prosperitySpan.textContent = 'Prosperity360';

        welcomeTextElement.innerHTML = '';
        welcomeTextElement.appendChild(document.createTextNode(language.welcome.replace('Prosperity360', '')));
        welcomeTextElement.appendChild(prosperitySpan);

        // Update display text
        displayCurrentLang.textContent = language.name;

        // Update selected state in dropdown
        const allListItems = languageList.querySelectorAll('li');
        allListItems.forEach(item => {
            if (item.dataset.code === language.code) {
                item.classList.add('selected');
            } else {
                item.classList.remove('selected');
            }
        });

        // Close dropdown
        languageDropdown.classList.remove('active');
    }

    // Toggle dropdown
    translateBtn.addEventListener('click', function (e) {
        e.stopPropagation();
        languageDropdown.classList.toggle('active');
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', function (e) {
        if (!translateBtn.contains(e.target) && !languageDropdown.contains(e.target)) {
            languageDropdown.classList.remove('active');
        }
    });

    // Initialize
    populateLanguageList();

    // Demo: Change language automatically every 10 seconds for demonstration
    let demoIndex = 0;
    setInterval(() => {
        demoIndex = (demoIndex + 1) % languages.length;
        selectLanguage(languages[demoIndex]);
    }, 10000);
});

// Mobile Menu Toggle
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const navLinks = document.getElementById('navLinks');

if (mobileMenuBtn && navLinks) {
    mobileMenuBtn.addEventListener('click', () => {
        navLinks.classList.toggle('active');

        // Toggle between hamburger and close icons
        const icon = mobileMenuBtn.querySelector('i');
        if (icon) {
            icon.className = navLinks.classList.contains('active')
                ? 'fas fa-times'
                : 'fas fa-bars';
        } else {
            // Fallback if there's no <i> element inside
            mobileMenuBtn.innerHTML = navLinks.classList.contains('active')
                ? '<i class="fas fa-times"></i>'
                : '<i class="fas fa-bars"></i>';
        }
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!mobileMenuBtn.contains(e.target) && !navLinks.contains(e.target) && navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');

            const icon = mobileMenuBtn.querySelector('i');
            if (icon) {
                icon.className = 'fas fa-bars';
            } else {
                mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
            }
        }
    });

    // Close menu when clicking a link
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');

            const icon = mobileMenuBtn.querySelector('i');
            if (icon) {
                icon.className = 'fas fa-bars';
            } else {
                mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
            }
        });
    });

    // Close menu on window resize (optional)
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768 && navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');

            const icon = mobileMenuBtn.querySelector('i');
            if (icon) {
                icon.className = 'fas fa-bars';
            } else {
                mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
            }
        }
    });
}
// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;

        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 80,
                behavior: 'smooth'
            });
        }
    });
});

// Contact Form Submission
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const submitBtn = contactForm.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;

        try {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Sending...';

            const formData = new FormData(contactForm);
            const response = await fetch('/contact', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();

            if (result.success) {
                alert(result.message);
                contactForm.reset();
            } else {
                alert('Error: ' + result.message);
            }
        } catch (error) {
            alert('An error occurred. Please try again.');
            console.error('Error:', error);
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
        }
    });
}

// Newsletter Subscription
const newsletterForm = document.getElementById('newsletterForm');
if (newsletterForm) {
    newsletterForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const emailInput = newsletterForm.querySelector('input[type="email"]');
        const submitBtn = newsletterForm.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;

        if (!emailInput.value) {
            alert('Please enter your email address');
            return;
        }

        try {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Subscribing...';

            const formData = new FormData(newsletterForm);
            const response = await fetch('/subscribe', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();

            if (result.success) {
                alert(result.message);
                newsletterForm.reset();
            } else {
                alert('Error: ' + result.message);
            }
        } catch (error) {
            alert('An error occurred. Please try again.');
            console.error('Error:', error);
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
        }
    });
}

// Stats Counter Animation
const animateCounters = () => {
    const counters = document.querySelectorAll('.stat-number');

    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;

        const updateCounter = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.ceil(current).toLocaleString();
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target.toLocaleString();
            }
        };

        updateCounter();
    });
};

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            if (entry.target.classList.contains('stats-grid')) {
                animateCounters();
            }
            entry.target.classList.add('animated');
        }
    });
}, observerOptions);

// Observe elements for animation
document.querySelectorAll('.program-card, .pillar-item, .cta-card, .stats-grid').forEach(el => {
    observer.observe(el);
});

// Parallax effect for hero
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    if (hero) {
        hero.style.transform = `translateY(${scrolled * 0.5}px)`;
    }
});

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
    // Add loading animation
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s';

    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
});


// Carousel scripts
document.addEventListener('DOMContentLoaded', function () {
    const track = document.getElementById('carouselTrack');
    const cards = document.querySelectorAll('.pillar-card');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const dotsContainer = document.getElementById('carouselDots');

    let currentIndex = 0;
    const cardWidth = cards[0].offsetWidth + 30; // Card width + margin
    const visibleCards = Math.floor(track.parentElement.offsetWidth / cardWidth);
    const totalCards = cards.length;

    // Create dots for navigation
    for (let i = 0; i < totalCards; i++) {
        const dot = document.createElement('div');
        dot.classList.add('dot');
        if (i === 0) dot.classList.add('active');
        dot.addEventListener('click', () => {
            goToSlide(i);
        });
        dotsContainer.appendChild(dot);
    }

    const dots = document.querySelectorAll('.dot');

    // Update carousel position
    function updateCarousel() {
        track.style.transform = `translateX(-${currentIndex * cardWidth}px)`;

        // Update active dot
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentIndex);
        });

        // Disable/enable buttons based on position
        prevBtn.disabled = currentIndex === 0;
        nextBtn.disabled = currentIndex >= totalCards - visibleCards;

        // Style disabled buttons
        prevBtn.style.opacity = prevBtn.disabled ? '0.5' : '1';
        nextBtn.style.opacity = nextBtn.disabled ? '0.5' : '1';
    }

    function goToSlide(index) {
        // Ensure index is within bounds
        currentIndex = Math.max(0, Math.min(index, totalCards - visibleCards));
        updateCarousel();
    }

    function nextSlide() {
        if (currentIndex < totalCards - visibleCards) {
            currentIndex++;
            updateCarousel();
        }
    }

    function prevSlide() {
        if (currentIndex > 0) {
            currentIndex--;
            updateCarousel();
        }
    }

    // Event listeners for buttons
    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') nextSlide();
        if (e.key === 'ArrowLeft') prevSlide();
    });

    // Handle window resize
    let resizeTimeout;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(() => {
            // Recalculate card width after resize
            const newCardWidth = cards[0].offsetWidth + 30;
            // Update position based on new width
            track.style.transform = `translateX(-${currentIndex * newCardWidth}px)`;
        }, 250);
    });

    // Initialize carousel
    updateCarousel();

    // Auto-rotate carousel (optional)
    let autoRotate = setInterval(nextSlide, 5000);

    // Pause auto-rotate on hover
    track.parentElement.addEventListener('mouseenter', () => {
        clearInterval(autoRotate);
    });

    track.parentElement.addEventListener('mouseleave', () => {
        autoRotate = setInterval(nextSlide, 5000);
    });
});



// Testimonial Carousel
document.addEventListener('DOMContentLoaded', function () {
    const track = document.getElementById('testimonialTrack');
    const slides = document.querySelectorAll('.testimonial-slide');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const dotsContainer = document.getElementById('carouselDots');

    let currentSlide = 0;
    const totalSlides = slides.length;

    // Create dots
    for (let i = 0; i < totalSlides; i++) {
        const dot = document.createElement('div');
        dot.classList.add('dot');
        if (i === 0) dot.classList.add('active');
        dot.addEventListener('click', () => goToSlide(i));
        dotsContainer.appendChild(dot);
    }

    const dots = document.querySelectorAll('.dot');

    // Update carousel
    function updateCarousel() {
        track.style.transform = `translateX(-${currentSlide * 100}%)`;

        // Update dots
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentSlide);
        });
    }

    function goToSlide(slideIndex) {
        currentSlide = slideIndex;
        updateCarousel();
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % totalSlides;
        updateCarousel();
    }

    function prevSlide() {
        currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
        updateCarousel();
    }

    // Event listeners
    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') nextSlide();
        if (e.key === 'ArrowLeft') prevSlide();
    });

    // Auto-rotate every 8 seconds
    let autoRotate = setInterval(nextSlide, 8000);

    // Pause auto-rotate on hover
    track.parentElement.addEventListener('mouseenter', () => {
        clearInterval(autoRotate);
    });

    track.parentElement.addEventListener('mouseleave', () => {
        autoRotate = setInterval(nextSlide, 8000);
    });

    // Initialize
    updateCarousel();
});