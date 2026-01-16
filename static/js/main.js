/* 
 /$$$$$$$                                                             /$$   /$$                /$$$$$$   /$$$$$$   /$$$$$$                                                                        
| $$__  $$                                                           |__/  | $$               /$$__  $$ /$$__  $$ /$$$_  $$                                                                       
| $$  \ $$ /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$  /$$ /$$$$$$   /$$   /$$|__/  \ $$| $$  \__/| $$$$\ $$                                                                       
| $$$$$$$//$$__  $$ /$$__  $$ /$$_____/ /$$__  $$ /$$__  $$ /$$__  $$| $$|_  $$_/  | $$  | $$   /$$$$$/| $$$$$$$ | $$ $$ $$                                                                       
| $$____/| $$  \__/| $$  \ $$|  $$$$$$ | $$  \ $$| $$$$$$$$| $$  \__/| $$  | $$    | $$  | $$  |___  $$| $$__  $$| $$\ $$$$                                                                       
| $$     | $$      | $$  | $$ \____  $$| $$  | $$| $$_____/| $$      | $$  | $$ /$$| $$  | $$ /$$  \ $$| $$  \ $$| $$ \ $$$                                                                       
| $$     | $$      |  $$$$$$/ /$$$$$$$/| $$$$$$$/|  $$$$$$$| $$      | $$  |  $$$$/|  $$$$$$$|  $$$$$$/|  $$$$$$/|  $$$$$$/                                                                       
|__/     |__/       \______/ |_______/ | $$____/  \_______/|__/      |__/   \___/   \____  $$ \______/  \______/  \______/                                                                        
                                       | $$                                         /$$  | $$                                                                                                     
                                       | $$                                        |  $$$$$$/                                                                                                     
                                       |__/                                         \______/                                                                                                      
 /$$$$$$$                                /$$                                                         /$$           /$$$$$$           /$$   /$$     /$$             /$$     /$$                    
| $$__  $$                              | $$                                                        | $$          |_  $$_/          |__/  | $$    |__/            | $$    |__/                    
| $$  \ $$  /$$$$$$  /$$    /$$ /$$$$$$ | $$  /$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$  /$$$$$$          | $$   /$$$$$$$  /$$ /$$$$$$   /$$  /$$$$$$  /$$$$$$   /$$ /$$    /$$ /$$$$$$ 
| $$  | $$ /$$__  $$|  $$  /$$//$$__  $$| $$ /$$__  $$ /$$__  $$| $$_  $$_  $$ /$$__  $$| $$__  $$|_  $$_/          | $$  | $$__  $$| $$|_  $$_/  | $$ |____  $$|_  $$_/  | $$|  $$  /$$//$$__  $$
| $$  | $$| $$$$$$$$ \  $$/$$/| $$$$$$$$| $$| $$  \ $$| $$  \ $$| $$ \ $$ \ $$| $$$$$$$$| $$  \ $$  | $$            | $$  | $$  \ $$| $$  | $$    | $$  /$$$$$$$  | $$    | $$ \  $$/$$/| $$$$$$$$
| $$  | $$| $$_____/  \  $$$/ | $$_____/| $$| $$  | $$| $$  | $$| $$ | $$ | $$| $$_____/| $$  | $$  | $$ /$$        | $$  | $$  | $$| $$  | $$ /$$| $$ /$$__  $$  | $$ /$$| $$  \  $$$/ | $$_____/
| $$$$$$$/|  $$$$$$$   \  $/  |  $$$$$$$| $$|  $$$$$$/| $$$$$$$/| $$ | $$ | $$|  $$$$$$$| $$  | $$  |  $$$$/       /$$$$$$| $$  | $$| $$  |  $$$$/| $$|  $$$$$$$  |  $$$$/| $$   \  $/  |  $$$$$$$
|_______/  \_______/    \_/    \_______/|__/ \______/ | $$____/ |__/ |__/ |__/ \_______/|__/  |__/   \___/        |______/|__/  |__/|__/   \___/  |__/ \_______/   \___/  |__/    \_/    \_______/
                                                      | $$                                                                                                                                        
                                                      | $$                                                                                                                                        
                                                      |__/               

*/


// Header & Footer Interactive Features
document.addEventListener('DOMContentLoaded', function () {
    // Initialize all interactive components
    initMobileMenu();
    initLanguageSelector();
    initSmoothScroll();
    initActiveNavLinks();
    initHoverEffects();
});

// Mobile Menu Toggle
function initMobileMenu() {
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const nav = document.querySelector('nav');
    const navLinks = document.querySelectorAll('.nav-links a');
    const body = document.body;

    if (!mobileMenuBtn || !nav) return;

    // Create overlay for mobile menu
    const overlay = document.createElement('div');
    overlay.className = 'nav-overlay';
    document.body.appendChild(overlay);

    // Toggle mobile menu
    function toggleMobileMenu() {
        mobileMenuBtn.classList.toggle('active');
        nav.classList.toggle('active');
        overlay.classList.toggle('active');
        body.classList.toggle('no-scroll');

        // Change icon
        const icon = mobileMenuBtn.querySelector('i');
        if (mobileMenuBtn.classList.contains('active')) {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-times');
        } else {
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        }
    }

    // Close mobile menu when clicking a link
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth <= 768) {
                toggleMobileMenu();
            }

            // Handle dropdown toggle on mobile
            const dropdown = link.nextElementSibling;
            if (dropdown && dropdown.tagName === 'UL') {
                if (window.innerWidth <= 768) {
                    dropdown.classList.toggle('active');
                }
            }
        });
    });

    // Close menu when clicking overlay
    overlay.addEventListener('click', toggleMobileMenu);

    // Toggle menu button
    mobileMenuBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        toggleMobileMenu();
    });

    // Close menu when pressing Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && nav.classList.contains('active')) {
            toggleMobileMenu();
        }
    });

    // Add no-scroll class to body
    const style = document.createElement('style');
    style.textContent = `
        body.no-scroll {
            overflow: hidden;
        }
    `;
    document.head.appendChild(style);
}

// Language Selector
function initLanguageSelector() {
    const translateBtn = document.getElementById('translateBtn');
    const languageDropdown = document.getElementById('languageDropdown');
    const languageList = document.getElementById('languageList');
    const currentLang = document.getElementById('currentLang');

    if (!translateBtn || !languageDropdown || !languageList) return;

    // Available languages
    const languages = [
        { code: 'en', name: 'English', flag: '🇺🇸' },
        { code: 'fr', name: 'Français', flag: '🇫🇷' },
        { code: 'es', name: 'Español', flag: '🇪🇸' },
        { code: 'pt', name: 'Português', flag: '🇵🇹' },
        { code: 'sw', name: 'Swahili', flag: '🇰🇪' },
        { code: 'ar', name: 'العربية', flag: '🇸🇦' }
    ];

    // Create language list items
    languages.forEach(lang => {
        const li = document.createElement('li');
        li.innerHTML = `
            <i class="flag-icon">${lang.flag}</i>
            <span>${lang.name}</span>
        `;

        if (lang.code === 'en') {
            li.classList.add('active');
        }

        li.addEventListener('click', () => {
            // Update current language
            currentLang.textContent = lang.name;

            // Update active state
            document.querySelectorAll('#languageList li').forEach(item => {
                item.classList.remove('active');
            });
            li.classList.add('active');

            // Close dropdown
            languageDropdown.classList.remove('show');
            translateBtn.classList.remove('active');

            // Here you would typically:
            // 1. Save language preference to localStorage
            // 2. Update page content with translations
            // 3. Refresh or update the page
            localStorage.setItem('preferredLanguage', lang.code);

            // Show translation loading message (optional)
            showTranslationMessage(lang.name);
        });

        languageList.appendChild(li);
    });

    // Toggle dropdown
    translateBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        languageDropdown.classList.toggle('show');
        translateBtn.classList.toggle('active');
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
        if (!translateBtn.contains(e.target) && !languageDropdown.contains(e.target)) {
            languageDropdown.classList.remove('show');
            translateBtn.classList.remove('active');
        }
    });

    // Close dropdown when pressing Escape
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && languageDropdown.classList.contains('show')) {
            languageDropdown.classList.remove('show');
            translateBtn.classList.remove('active');
        }
    });

    // Load saved language preference
    const savedLang = localStorage.getItem('preferredLanguage');
    if (savedLang) {
        const selectedLang = languages.find(lang => lang.code === savedLang);
        if (selectedLang) {
            currentLang.textContent = selectedLang.name;
        }
    }
}

// Translation message function
function showTranslationMessage(langName) {
    // Create notification
    const notification = document.createElement('div');
    notification.className = 'translation-notification';
    notification.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: var(--primary-color);
        color: white;
        padding: 15px 20px;
        border-radius: var(--radius);
        box-shadow: 0 10px 30px rgba(0, 128, 128, 0.3);
        z-index: 10000;
        animation: slideInRight 0.3s ease;
        max-width: 300px;
    `;

    notification.innerHTML = `
        <div style="display: flex; align-items: center; gap: 10px;">
            <i class="fas fa-language" style="font-size: 1.2rem;"></i>
            <div>
                <strong>Language Changed</strong>
                <p style="margin: 5px 0 0 0; font-size: 0.9rem;">Switched to ${langName}</p>
            </div>
        </div>
    `;

    document.body.appendChild(notification);

    // Remove notification after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'fadeOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);

    // Add fadeOut animation if not exists
    if (!document.querySelector('#fadeOutStyle')) {
        const style = document.createElement('style');
        style.id = 'fadeOutStyle';
        style.textContent = `
            @keyframes fadeOut {
                from { opacity: 1; transform: translateX(0); }
                to { opacity: 0; transform: translateX(100px); }
            }
        `;
        document.head.appendChild(style);
    }
}

// Smooth Scroll for Internal Links
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;

            const targetElement = document.querySelector(href);
            if (targetElement) {
                e.preventDefault();

                // Close mobile menu if open
                if (window.innerWidth <= 768) {
                    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
                    const nav = document.querySelector('nav');
                    const overlay = document.querySelector('.nav-overlay');

                    if (mobileMenuBtn && mobileMenuBtn.classList.contains('active')) {
                        mobileMenuBtn.classList.remove('active');
                        nav.classList.remove('active');
                        overlay?.classList.remove('active');
                        document.body.classList.remove('no-scroll');

                        // Reset icon
                        const icon = mobileMenuBtn.querySelector('i');
                        icon.classList.remove('fa-times');
                        icon.classList.add('fa-bars');
                    }
                }

                // Scroll to target
                window.scrollTo({
                    top: targetElement.offsetTop - 100,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Active Navigation Links
function initActiveNavLinks() {
    const navLinks = document.querySelectorAll('.nav-links a');
    const currentPath = window.location.pathname;

    function updateActiveNav() {
        navLinks.forEach(link => {
            const linkPath = new URL(link.href).pathname;
            link.classList.remove('active');

            if (linkPath === currentPath) {
                link.classList.add('active');
            }
        });
    }

    // Initial update
    updateActiveNav();

    // Update on navigation (for single page apps)
    window.addEventListener('popstate', updateActiveNav);
}

// Hover Effects
function initHoverEffects() {
    // Add hover effect to logo
    const logo = document.querySelector('.logo');
    if (logo) {
        logo.addEventListener('mouseenter', function () {
            const img = this.querySelector('img');
            if (img) img.style.transform = 'scale(1.05)';
        });

        logo.addEventListener('mouseleave', function () {
            const img = this.querySelector('img');
            if (img) img.style.transform = 'scale(1)';
        });
    }

    // Add hover effect to social links
    const socialLinks = document.querySelectorAll('.social-links a');
    socialLinks.forEach(link => {
        link.addEventListener('mouseenter', function () {
            const icon = this.querySelector('i');
            if (icon) {
                icon.style.transform = 'rotate(10deg) scale(1.2)';
            }
        });

        link.addEventListener('mouseleave', function () {
            const icon = this.querySelector('i');
            if (icon) {
                icon.style.transform = 'rotate(0) scale(1)';
            }
        });
    });
}

// Sticky Header on Scroll
function initStickyHeader() {
    const header = document.querySelector('.header');
    const welcomeBar = document.querySelector('.subheading-container');

    if (!header || !welcomeBar) return;

    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        // Add shadow when scrolled
        if (currentScroll > 10) {
            header.style.boxShadow = '0 5px 20px rgba(0, 0, 0, 0.08)';
        } else {
            header.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.05)';
        }

        // Hide/show header on scroll (optional)
        if (window.innerWidth <= 768) {
            if (currentScroll > lastScroll && currentScroll > 100) {
                // Scrolling down
                header.style.transform = 'translateY(-100%)';
                welcomeBar.style.transform = 'translateY(-100%)';
            } else {
                // Scrolling up
                header.style.transform = 'translateY(0)';
                welcomeBar.style.transform = 'translateY(0)';
            }
        }

        lastScroll = currentScroll;
    });
}

// Initialize sticky header
initStickyHeader();