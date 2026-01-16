// translation-controller.js - Main Translation System

document.addEventListener('DOMContentLoaded', function () {
    // Initialize translation system
    initTranslationSystem();

    // Load saved language preference
    loadLanguagePreference();
});

// Global translation state
let currentLanguage = 'en';
let isRTL = false;

// Initialize translation system
function initTranslationSystem() {
    // Setup language selector
    setupLanguageSelector();

    // Setup click events for translation
    setupTranslationEvents();

    // Setup RTL detection
    setupRTLCheck();
}

// Setup language selector dropdown
function setupLanguageSelector() {
    const translateBtn = document.getElementById('translateBtn');
    const languageDropdown = document.getElementById('languageDropdown');
    const languageList = document.getElementById('languageList');
    const currentLang = document.getElementById('currentLang');

    if (!translateBtn || !languageDropdown || !languageList) return;

    // Create language list items
    Object.entries(languageNames).forEach(([code, name]) => {
        const li = document.createElement('li');
        li.setAttribute('data-lang', code);
        li.innerHTML = `
            <i class="flag-icon">${getFlagEmoji(code)}</i>
            <span>${name}</span>
        `;

        if (code === currentLanguage) {
            li.classList.add('active');
        }

        li.addEventListener('click', () => {
            changeLanguage(code);

            // Close dropdown
            languageDropdown.classList.remove('show');
            translateBtn.classList.remove('active');
        });

        languageList.appendChild(li);
    });

    // Toggle dropdown
    translateBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        languageDropdown.classList.toggle('show');
        translateBtn.classList.toggle('active');

        // Update active state in dropdown
        updateLanguageDropdown();
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
        if (!translateBtn.contains(e.target) && !languageDropdown.contains(e.target)) {
            languageDropdown.classList.remove('show');
            translateBtn.classList.remove('active');
        }
    });

    // Close dropdown on Escape
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && languageDropdown.classList.contains('show')) {
            languageDropdown.classList.remove('show');
            translateBtn.classList.remove('active');
        }
    });
}

// Get flag emoji for language
function getFlagEmoji(langCode) {
    const flagMap = {
        'en': '🇺🇸',
        'fr': '🇫🇷',
        'es': '🇪🇸',
        'pt': '🇵🇹',
        'ar': '🇸🇦',
        'sw': '🇰🇪'
    };
    return flagMap[langCode] || '🌐';
}

// Update language dropdown active state
function updateLanguageDropdown() {
    const languageItems = document.querySelectorAll('#languageList li');
    languageItems.forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('data-lang') === currentLanguage) {
            item.classList.add('active');
        }
    });
}

// Setup translation events
function setupTranslationEvents() {
    // Listen for language changes from other components
    document.addEventListener('languageChanged', (e) => {
        if (e.detail && e.detail.language) {
            changeLanguage(e.detail.language);
        }
    });

    // Listen for page changes (for SPA)
    window.addEventListener('popstate', () => {
        setTimeout(() => {
            applyTranslations();
        }, 100);
    });
}

// Setup RTL check
function setupRTLCheck() {
    // Check if current language is RTL
    isRTL = rtlLanguages.includes(currentLanguage);

    // Apply RTL styles if needed
    if (isRTL) {
        document.body.classList.add('rtl');
        document.documentElement.setAttribute('dir', 'rtl');
    } else {
        document.body.classList.remove('rtl');
        document.documentElement.setAttribute('dir', 'ltr');
    }
}

// Load language preference from localStorage
function loadLanguagePreference() {
    const savedLang = localStorage.getItem('prosperity360_language');
    if (savedLang && translations[savedLang]) {
        changeLanguage(savedLang, false); // false = don't save again
    }

    // Update UI to show current language
    updateLanguageUI();
}

// Change language
function changeLanguage(langCode, savePreference = true) {
    if (!translations[langCode]) {
        console.warn(`Language "${langCode}" not supported`);
        return;
    }

    // Update current language
    currentLanguage = langCode;

    // Update RTL status
    isRTL = rtlLanguages.includes(langCode);

    // Save preference
    if (savePreference) {
        localStorage.setItem('prosperity360_language', langCode);
    }

    // Apply translations
    applyTranslations();

    // Update UI
    updateLanguageUI();

    // Apply RTL/LTR direction
    applyTextDirection();

    // Dispatch event for other components
    document.dispatchEvent(new CustomEvent('languageChanged', {
        detail: { language: langCode }
    }));

    // Show notification
    showLanguageChangeNotification(langCode);
}

// Apply translations to the entire page
function applyTranslations() {
    const translation = translations[currentLanguage];
    if (!translation) return;

    // 1. Translate elements with data-translate attribute
    document.querySelectorAll('[data-translate]').forEach(element => {
        const key = element.getAttribute('data-translate');
        if (translation[key]) {
            // Handle different element types
            if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
                element.placeholder = translation[key];
            } else if (element.hasAttribute('title')) {
                element.title = translation[key];
            } else if (element.hasAttribute('alt')) {
                element.alt = translation[key];
            } else {
                element.textContent = translation[key];
            }
        }
    });

    // 2. Translate elements with data-translate-html (for HTML content)
    document.querySelectorAll('[data-translate-html]').forEach(element => {
        const key = element.getAttribute('data-translate-html');
        if (translation[key]) {
            element.innerHTML = translation[key];
        }
    });

    // 3. Special handling for complex content
    translateComplexContent();

    // 4. Update any dynamic content (like counters, dates, etc.)
    updateDynamicContent();
}

// Update language UI elements
function updateLanguageUI() {
    // Update language button text
    const currentLangElement = document.getElementById('currentLang');
    if (currentLangElement) {
        currentLangElement.textContent = languageNames[currentLanguage] || 'English';
    }

    // Update language dropdown active state
    updateLanguageDropdown();
}

// Apply text direction based on language
function applyTextDirection() {
    if (isRTL) {
        document.body.classList.add('rtl');
        document.documentElement.setAttribute('dir', 'rtl');
        document.body.style.direction = 'rtl';
        document.body.style.textAlign = 'right';
    } else {
        document.body.classList.remove('rtl');
        document.documentElement.setAttribute('dir', 'ltr');
        document.body.style.direction = 'ltr';
        document.body.style.textAlign = 'left';
    }

    // Adjust specific elements for RTL
    if (isRTL) {
        // Adjust carousels and sliders
        document.querySelectorAll('.carousel-btn').forEach(btn => {
            if (btn.classList.contains('prev')) {
                btn.style.left = 'auto';
                btn.style.right = '0';
            } else if (btn.classList.contains('next')) {
                btn.style.right = 'auto';
                btn.style.left = '0';
            }
        });
    }
}

// Translate complex content (like mission statements, paragraphs)
function translateComplexContent() {
    const translation = translations[currentLanguage];

    // Example: Update mission statement
    const missionElement = document.getElementById('typewriter');
    if (missionElement) {
        // You can implement logic here for rotating mission statements
        // or use data attributes to store which mission to show
    }

    // Update page titles if they have specific IDs
    const pageTitles = {
        'hero_title': '.indexhero-heading h1',
        'hero_description': '.indexhero-description',
        'strategic_pillars': '.pillars-container h2',
        // Add more as needed
    };

    Object.entries(pageTitles).forEach(([key, selector]) => {
        const element = document.querySelector(selector);
        if (element && translation[key]) {
            element.textContent = translation[key];
        }
    });
}

// Update dynamic content (counters, dates, etc.)
function updateDynamicContent() {
    // Update any number formatting based on language
    const numberElements = document.querySelectorAll('.stat-number');
    numberElements.forEach(element => {
        const number = parseInt(element.textContent.replace(/,/g, ''));
        if (!isNaN(number)) {
            element.textContent = formatNumber(number);
        }
    });

    // Update dates based on locale
    updateDates();
}

// Format numbers based on language
function formatNumber(number) {
    if (currentLanguage === 'ar') {
        // Arabic numerals
        return number.toLocaleString('ar-EG');
    } else if (currentLanguage === 'fr') {
        // French formatting (space as thousand separator)
        return number.toLocaleString('fr-FR');
    } else {
        // Default: English formatting
        return number.toLocaleString('en-US');
    }
}

// Update dates based on language
function updateDates() {
    const dateElements = document.querySelectorAll('[data-date]');
    dateElements.forEach(element => {
        const date = new Date(element.getAttribute('data-date'));
        if (!isNaN(date)) {
            element.textContent = formatDate(date);
        }
    });
}

// Format date based on language
function formatDate(date) {
    const options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    };

    const locales = {
        'en': 'en-US',
        'fr': 'fr-FR',
        'es': 'es-ES',
        'pt': 'pt-PT',
        'ar': 'ar-SA'
    };

    return date.toLocaleDateString(locales[currentLanguage] || 'en-US', options);
}

// Show language change notification
function showLanguageChangeNotification(langCode) {
    // Remove existing notification
    const existingNotification = document.querySelector('.language-notification');
    if (existingNotification) {
        existingNotification.remove();
    }

    // Create notification
    const notification = document.createElement('div');
    notification.className = 'language-notification';
    notification.innerHTML = `
        <div class="notification-content">
            <i class="fas fa-language"></i>
            <div>
                <strong>${languageNames[langCode]}</strong>
                <p>Language changed successfully</p>
            </div>
            <button class="notification-close">&times;</button>
        </div>
    `;

    // Add styles
    notification.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: var(--primary-color);
        color: white;
        padding: 15px 20px;
        border-radius: 8px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        z-index: 10000;
        animation: slideInRight 0.3s ease;
        max-width: 300px;
    `;

    notification.querySelector('.notification-content').style.cssText = `
        display: flex;
        align-items: center;
        gap: 15px;
    `;

    notification.querySelector('.notification-close').style.cssText = `
        background: none;
        border: none;
        color: white;
        font-size: 1.5rem;
        cursor: pointer;
        margin-left: 10px;
    `;

    document.body.appendChild(notification);

    // Add close functionality
    notification.querySelector('.notification-close').addEventListener('click', () => {
        notification.remove();
    });

    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.style.animation = 'fadeOut 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }
    }, 5000);
}

// Get current language
function getCurrentLanguage() {
    return currentLanguage;
}

// Get translation for a specific key
function getTranslation(key, lang = currentLanguage) {
    const langTranslations = translations[lang];
    if (!langTranslations) return key;

    const keys = key.split('.');
    let value = langTranslations;

    for (const k of keys) {
        if (value && typeof value === 'object' && k in value) {
            value = value[k];
        } else {
            return key; // Return key if translation not found
        }
    }

    return value || key;
}

// Export functions for use in other scripts
window.TranslationController = {
    changeLanguage,
    getCurrentLanguage,
    getTranslation,
    applyTranslations
};