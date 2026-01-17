# """
#  /$$$$$$$                                                             /$$   /$$                /$$$$$$   /$$$$$$   /$$$$$$                                                                        
# | $$__  $$                                                           |__/  | $$               /$$__  $$ /$$__  $$ /$$$_  $$                                                                       
# | $$  \ $$ /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$  /$$ /$$$$$$   /$$   /$$|__/  \ $$| $$  \__/| $$$$\ $$                                                                       
# | $$$$$$$//$$__  $$ /$$__  $$ /$$_____/ /$$__  $$ /$$__  $$ /$$__  $$| $$|_  $$_/  | $$  | $$   /$$$$$/| $$$$$$$ | $$ $$ $$                                                                       
# | $$____/| $$  \__/| $$  \ $$|  $$$$$$ | $$  \ $$| $$$$$$$$| $$  \__/| $$  | $$    | $$  | $$  |___  $$| $$__  $$| $$\ $$$$                                                                       
# | $$     | $$      | $$  | $$ \____  $$| $$  | $$| $$_____/| $$      | $$  | $$ /$$| $$  | $$ /$$  \ $$| $$  \ $$| $$ \ $$$                                                                       
# | $$     | $$      |  $$$$$$/ /$$$$$$$/| $$$$$$$/|  $$$$$$$| $$      | $$  |  $$$$/|  $$$$$$$|  $$$$$$/|  $$$$$$/|  $$$$$$/                                                                       
# |__/     |__/       \______/ |_______/ | $$____/  \_______/|__/      |__/   \___/   \____  $$ \______/  \______/  \______/                                                                        
#                                        | $$                                         /$$  | $$                                                                                                     
#                                        | $$                                        |  $$$$$$/                                                                                                     
#                                        |__/                                         \______/                                                                                                      
#  /$$$$$$$                                /$$                                                         /$$           /$$$$$$           /$$   /$$     /$$             /$$     /$$                    
# | $$__  $$                              | $$                                                        | $$          |_  $$_/          |__/  | $$    |__/            | $$    |__/                    
# | $$  \ $$  /$$$$$$  /$$    /$$ /$$$$$$ | $$  /$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$  /$$$$$$          | $$   /$$$$$$$  /$$ /$$$$$$   /$$  /$$$$$$  /$$$$$$   /$$ /$$    /$$ /$$$$$$ 
# | $$  | $$ /$$__  $$|  $$  /$$//$$__  $$| $$ /$$__  $$ /$$__  $$| $$_  $$_  $$ /$$__  $$| $$__  $$|_  $$_/          | $$  | $$__  $$| $$|_  $$_/  | $$ |____  $$|_  $$_/  | $$|  $$  /$$//$$__  $$
# | $$  | $$| $$$$$$$$ \  $$/$$/| $$$$$$$$| $$| $$  \ $$| $$  \ $$| $$ \ $$ \ $$| $$$$$$$$| $$  \ $$  | $$            | $$  | $$  \ $$| $$  | $$    | $$  /$$$$$$$  | $$    | $$ \  $$/$$/| $$$$$$$$
# | $$  | $$| $$_____/  \  $$$/ | $$_____/| $$| $$  | $$| $$  | $$| $$ | $$ | $$| $$_____/| $$  | $$  | $$ /$$        | $$  | $$  | $$| $$  | $$ /$$| $$ /$$__  $$  | $$ /$$| $$  \  $$$/ | $$_____/
# | $$$$$$$/|  $$$$$$$   \  $/  |  $$$$$$$| $$|  $$$$$$/| $$$$$$$/| $$ | $$ | $$|  $$$$$$$| $$  | $$  |  $$$$/       /$$$$$$| $$  | $$| $$  |  $$$$/| $$|  $$$$$$$  |  $$$$/| $$   \  $/  |  $$$$$$$
# |_______/  \_______/    \_/    \_______/|__/ \______/ | $$____/ |__/ |__/ |__/ \_______/|__/  |__/   \___/        |______/|__/  |__/|__/   \___/  |__/ \_______/   \___/  |__/    \_/    \_______/
#                                                       | $$                                                                                                                                        
#                                                       | $$                                                                                                                                        
#                                                       |__/               

#  _____                                          _____ 
# ( ___ )----------------------------------------( ___ )
#  |   |                                          |   | 
#  |   |                                          |   | 
#  |   |           Authors GitHub Handle:         |   | 
#  |   |              AridsWolfgangX              |   | 
#  |   |               Zanonymous24               |   | 
#  |___|                                          |___| 
# (_____)----------------------------------------(_____)                                               
# """
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, g
import os
import json
import re
from datetime import timedelta
import logging
from typing import Dict, List

# ============================================================================
# CONFIGURATION
# ============================================================================
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "prosperity-must-flow")
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    DEFAULT_LANGUAGE = 'en'
    SUPPORTED_LANGUAGES = ['en', 'es', 'fr', 'pt', 'ar']

# ============================================================================
# TRANSLATION MANAGER (All in-memory)
# ============================================================================
class TranslationManager:
    def __init__(self):
        self.translations = self._build_translations()
    
    def _build_translations(self) -> Dict:
        """Build translations dictionary directly in code"""
        return {
            'en': {
               "welcome": "Welcome to Prosperity360",
               "home": "Home",
                "programs": "Strategic Pillars",
                "impact": "Our Impact",
                "about": "About Us",
                "contact": "Contact Us",
                "get_involved": "Get Involved",
                "hero_title": "Transforming Lives, Systems, and Economies",
                "hero_description": "A Pan-African, Global South–rooted development institution and alliance-based delivery mechanism dedicated to accelerating multidimensional wellbeing, local systems transformation, and community-driven sustainable development in contexts where human potential is abundant, but opportunity remains uneven.",
                "our_programs": "Our Programs",
                "subscribe_newsletter": "Subscribe to Our Newsletter",
                "stay_updated": "Stay updated with the latest news, events, and insights from Prosperity360 Development Initiative.",
                "enter_email": "Enter your email address",
                "subscribe": "Subscribe",
                "mission_1": "Prosperity360 Foundation is a Pan-African, Global South–rooted development institution that accelerates multi-dimensional prosperity, systems transformation, and community-driven development across Africa, Latin America, South Asia, and other emerging regions.",
                "mission_2": "Our mission is to create sustainable prosperity through innovation, economic empowerment, and community transformation across the Global South.",
                "mission_3": "We believe in building systems that empower communities, transform institutions, and create lasting impact for generations to come.",
                "strategic_pillars": "Strategic Pillars",
                "pillars_subtitle": "Six comprehensive programs driving multi-dimensional prosperity, systems transformation, and community-driven development across the Global South.",
                "innovation": "Innovation & Systems",
                "economic": "Economic Empowerment",
                "agriculture": "Food Systems",
                "energy": "Clean Energy",
                "health": "Health & WASH",
                "education": "Education",
                "quick_links": "Quick Links",
                "privacy_policy": "Privacy Policy",
                "terms_service": "Terms of Service",
                "all_rights_reserved": "All rights reserved",
                "transforming_lives": "Transforming Lives, Systems, and Economies.",
                "who_we_are": "Who We Are",
                "our_identity": "Our Identity",
                "our_philosophy": "Our Philosophy",
                "philosophy_quote": "\"Prosperity grows when people, systems, and institutions work in harmony.\"",
                "case_for_foundation": "The Case for an African/Global South Prosperity Foundation",
                "multi_dimensional_framework": "Our Multi-Dimensional Prosperity Framework",
                "framework_subtitle": "Measuring prosperity across six dimensions for holistic development",
                "ten_year_ambition": "Ten-Year Impact Ambition (2025–2035)",
                "impact_subtitle": "Our bold targets for transforming lives and systems across the Global South",
                "reach": "Reach",
                "deliver": "Deliver",
                "transform": "Transform",
                "million_households": "Million Households",
                "thousand_communities": "Thousand Communities",
                "countries": "Countries",
                "million_entrepreneurs": "Million Entrepreneurs",
                "million_stem_learners": "Million STEM Learners",
                "million_clean_energy": "Million with Clean Energy",
                "prosperity_zones": "Prosperity Zones",
                "national_systems": "National Systems",
                "farmers_supported": "Farmers Supported",
                "delivery_architecture": "Our Delivery Architecture",
                "architecture_subtitle": "Globally inspired, locally rooted implementation model",
                "community_level": "Community/Ward Level",
                "district_hubs": "District/LGA Hubs",
                "state_platforms": "Provincial/State Platforms",
                "national_platforms": "National Impact Platforms",
                "regional_hubs": "Global South Regional",
                "contact_us": "Contact Us",
                "contact_subtitle": "Get in touch with our team to learn more, partner with us, or support our work.",
                "get_in_touch": "Get in Touch",
                "wed_love_to_hear": "We'd love to hear from you",
                "email_us": "Email Us",
                "general_inquiries": "General Inquiries",
                "call_us": "Call Us",
                "visit_us": "Visit Us",
                "connect_online": "Connect Online",
                "send_us_message": "Send Us a Message",
                "follow_social": "Follow us on social media",
                "key_team_contacts": "Key Team Contacts",
                "frequently_asked": "Frequently Asked Questions",
                "global_presence": "Our Global Presence",
                "ways_to_engage": "Ways to Engage",
                "engage_subtitle": "Multiple pathways to contribute to inclusive prosperity",
                "donate": "Donate",
                "partner": "Partner",
                "volunteer": "Volunteer",
                "advocate": "Advocate",
                "make_donation": "Make a Donation",
                "donation_subtitle": "Your support transforms lives and builds prosperity",
                "volunteer_application": "Volunteer Application",
                "volunteer_subtitle": "Join our team of change-makers and contribute your skills",
                "corporate_partnerships": "Corporate Partnerships",
                "corporate_subtitle": "Strategic opportunities for businesses to drive social impact",
            },
            "fr": {
                "welcome": "Bienvenue à Prosperity360",
                "home": "Accueil",
                "programs": "Piliers Stratégiques",
                "impact": "Notre Impact",
                "about": "À Propos",
                "contact": "Contactez-nous",
                "get_involved": "Impliquez-vous",
                "hero_title": "Transformer les Vies, les Systèmes et les Économies",
                "hero_description": "Une institution de développement panafricaine, ancrée dans le Sud global, et un mécanisme de prestation basé sur une alliance, dédiés à l'accélération du bien-être multidimensionnel, de la transformation des systèmes locaux et du développement durable dirigé par les communautés.",
                "our_programs": "Nos Programmes",
                "subscribe_newsletter": "Abonnez-vous à notre Newsletter",
                "stay_updated": "Restez informé des dernières nouvelles, événements et perspectives de l'Initiative de Développement Prosperity360.",
                "enter_email": "Entrez votre adresse email",
                "subscribe": "S'abonner",
                "mission_1": "Prosperity360 Foundation est une institution de développement panafricaine, ancrée dans le Sud global, qui accélère la prospérité multidimensionnelle, la transformation des systèmes et le développement communautaire à travers l'Afrique, l'Amérique latine, l'Asie du Sud et d'autres régions émergentes.",
                "mission_2": "Notre mission est de créer une prospérité durable grâce à l'innovation, l'autonomisation économique et la transformation communautaire à travers le Sud global.",
                "mission_3": "Nous croyons en la construction de systèmes qui autonomisent les communautés, transforment les institutions et créent un impact durable pour les générations à venir.",
                "strategic_pillars": "Piliers Stratégiques",
                "pillars_subtitle": "Six programmes complets qui stimulent la prospérité multidimensionnelle, la transformation des systèmes et le développement communautaire à travers le Sud global.",
                "innovation": "Innovation & Systèmes",
                "economic": "Autonomisation Économique",
                "agriculture": "Systèmes Alimentaires",
                "energy": "Énergie Propre",
                "health": "Santé & Eau-Assainissement",
                "education": "Éducation",
                "quick_links": "Liens Rapides",
                "privacy_policy": "Politique de Confidentialité",
                "terms_service": "Conditions d'Utilisation",
                "all_rights_reserved": "Tous droits réservés",
                "transforming_lives": "Transformer les Vies, les Systèmes et les Économies.",
                "who_we_are": "Qui Nous Sommes",
                "our_identity": "Notre Identité",
                "our_philosophy": "Notre Philosophie",
                "philosophy_quote": "La prospérité croît lorsque les personnes, les systèmes et les institutions travaillent en harmonie.",
                "case_for_foundation": "Le Cas d'une Fondation de Prospérité Africaine/Sud Global",
                "multi_dimensional_framework": "Notre Cadre de Prospérité Multidimensionnelle",
                "framework_subtitle": "Mesurer la prospérité à travers six dimensions pour un développement holistique",
                "ten_year_ambition": "Ambition d'Impact sur Dix Ans (2025–2035)",
                "impact_subtitle": "Nos objectifs audacieux pour transformer les vies et les systèmes à travers le Sud global",
                "reach": "Atteindre",
                "deliver": "Fournir",
                "transform": "Transformer",
                "million_households": "Millions de Ménages",
                "thousand_communities": "Milliers de Communautés",
                "countries": "Pays",
                "million_entrepreneurs": "Millions d'Entrepreneurs",
                "million_stem_learners": "Millions d'Apprenants STEM",
                "million_clean_energy": "Millions avec Énergie Propre",
                "prosperity_zones": "Zones de Prospérité",
                "national_systems": "Systèmes Nationaux",
                "farmers_supported": "Agriculteurs Soutenus",
                "delivery_architecture": "Notre Architecture de Mise en Œuvre",
                "architecture_subtitle": "Modèle de mise en œuvre mondialement inspiré, localement enraciné",
                "community_level": "Niveau Communautaire/Quartier",
                "district_hubs": "Centres de District",
                "state_platforms": "Plates-formes Provinciales/Étatiques",
                "national_platforms": "Plates-formes d'Impact National",
                "regional_hubs": "Centres Régionaux Sud Global",
                "contact_us": "Contactez-nous",
                "contact_subtitle": "Contactez notre équipe pour en savoir plus, vous associer à nous ou soutenir notre travail.",
                "get_in_touch": "Entrer en Contact",
                "wed_love_to_hear": "Nous aimerions avoir de vos nouvelles",
                "email_us": "Écrivez-nous",
                "general_inquiries": "Renseignements Généraux",
                "call_us": "Appelez-nous",
                "visit_us": "Visitez-nous",
                "connect_online": "Connectez-vous en Ligne",
                "send_us_message": "Envoyez-nous un Message",
                "follow_social": "Suivez-nous sur les réseaux sociaux",
                "key_team_contacts": "Contacts Clés de l'Équipe",
                "frequently_asked": "Questions Fréquemment Posées",
                "global_presence": "Notre Présence Mondiale",
                "ways_to_engage": "Modes d'Engagement",
                "engage_subtitle": "Plusieurs voies pour contribuer à la prospérité inclusive",
                "donate": "Faire un Don",
                "partner": "Devenir Partenaire",
                "volunteer": "Bénévolat",
                "advocate": "Défendre",
                "make_donation": "Faire un Don",
                "donation_subtitle": "Votre soutien transforme des vies et construit la prospérité",
                "volunteer_application": "Candidature de Bénévole",
                "volunteer_subtitle": "Rejoignez notre équipe d'acteurs du changement et contribuez vos compétences",
                "corporate_partnerships": "Partenariats d'Entreprise",
                "corporate_subtitle": "Opportunités stratégiques pour les entreprises de générer un impact social"
            }, 
            "es": {
                "welcome": "Bienvenido a Prosperity360",
                "home": "Inicio",
                "programs": "Pilares Estratégicos",
                "impact": "Nuestro Impacto",
                "about": "Sobre Nosotros",
                "contact": "Contáctenos",
                "get_involved": "Involúcrate",
                "hero_title": "Transformando Vidas, Sistemas y Economías",
                "hero_description": "Una institución de desarrollo panafricana, arraigada en el Sur Global, y un mecanismo de entrega basado en alianzas dedicado a acelerar el bienestar multidimensional, la transformación de sistemas locales y el desarrollo sostenible impulsado por la comunidad.",
                "our_programs": "Nuestros Programas",
                "subscribe_newsletter": "Suscríbete a nuestro Boletín",
                "stay_updated": "Mantente actualizado con las últimas noticias, eventos y perspectivas de la Iniciativa de Desarrollo Prosperity360.",
                "enter_email": "Ingresa tu dirección de correo",
                "subscribe": "Suscribirse",
                "mission_1": "Prosperity360 Foundation es una institución de desarrollo panafricana, arraigada en el Sur Global, que acelera la prosperidad multidimensional, la transformación de sistemas y el desarrollo impulsado por la comunidad en África, América Latina, Asia del Sur y otras regiones emergentes.",
                "mission_2": "Nuestra misión es crear prosperidad sostenible a través de la innovación, el empoderamiento económico y la transformación comunitaria en todo el Sur Global.",
                "mission_3": "Creemos en la construcción de sistemas que empoderen a las comunidades, transformen instituciones y creen un impacto duradero para las generaciones venideras.",
                "strategic_pillars": "Pilares Estratégicos",
                "pillars_subtitle": "Seis programas integrales que impulsan la prosperidad multidimensional, la transformación de sistemas y el desarrollo impulsado por la comunidad en todo el Sur Global.",
                "innovation": "Innovación & Sistemas",
                "economic": "Empoderamiento Económico",
                "agriculture": "Sistemas Alimentarios",
                "energy": "Energía Limpia",
                "health": "Salud & Agua-Saneamiento",
                "education": "Educación",
                "quick_links": "Enlaces Rápidos",
                "privacy_policy": "Política de Privacidad",
                "terms_service": "Términos de Servicio",
                "all_rights_reserved": "Todos los derechos reservados",
                "transforming_lives": "Transformando Vidas, Sistemas y Economías.",
                "who_we_are": "Quiénes Somos",
                "our_identity": "Nuestra Identidad",
                "our_philosophy": "Nuestra Filosofía",
                "philosophy_quote": "La prosperidad crece cuando las personas, los sistemas y las instituciones trabajan en armonía.",
                "case_for_foundation": "El Caso para una Fundación de Prosperidad Africana/Sur Global",
                "multi_dimensional_framework": "Nuestro Marco de Prosperidad Multidimensional",
                "framework_subtitle": "Midiendo la prosperidad a través de seis dimensiones para un desarrollo holístico",
                "ten_year_ambition": "Ambición de Impacto a Diez Años (2025–2035)",
                "impact_subtitle": "Nuestros objetivos audaces para transformar vidas y sistemas en todo el Sur Global",
                "reach": "Alcance",
                "deliver": "Entregar",
                "transform": "Transformar",
                "million_households": "Millones de Hogares",
                "thousand_communities": "Miles de Comunidades",
                "countries": "Países",
                "million_entrepreneurs": "Millones de Emprendedores",
                "million_stem_learners": "Millones de Estudiantes STEM",
                "million_clean_energy": "Millones con Energía Limpia",
                "prosperity_zones": "Zonas de Prosperidad",
                "national_systems": "Sistemas Nacionales",
                "farmers_supported": "Agricultores Apoyados",
                "delivery_architecture": "Nuestra Arquitectura de Entrega",
                "architecture_subtitle": "Modelo de implementación globalmente inspirado, localmente arraigado",
                "community_level": "Nivel Comunitario/Barrio",
                "district_hubs": "Centros Distritales",
                "state_platforms": "Plataformas Provinciales/Estatales",
                "national_platforms": "Plataformas de Impacto Nacional",
                "regional_hubs": "Centros Regionales del Sur Global",
                "contact_us": "Contáctenos",
                "contact_subtitle": "Ponte en contacto con nuestro equipo para obtener más información, asociarte con nosotros o apoyar nuestro trabajo.",
                "get_in_touch": "Ponte en Contacto",
                "wed_love_to_hear": "Nos encantaría saber de ti",
                "email_us": "Escríbenos",
                "general_inquiries": "Consultas Generales",
                "call_us": "Llámanos",
                "visit_us": "Visítanos",
                "connect_online": "Conéctate en Línea",
                "send_us_message": "Envíanos un Mensaje",
                "follow_social": "Síguenos en las redes sociales",
                "key_team_contacts": "Contactos Clave del Equipo",
                "frequently_asked": "Preguntas Frecuentes",
                "global_presence": "Nuestra Presencia Global",
                "ways_to_engage": "Formas de Participar",
                "engage_subtitle": "Múltiples caminos para contribuir a la prosperidad inclusiva",
                "donate": "Donar",
                "partner": "Asociarse",
                "volunteer": "Voluntariado",
                "advocate": "Abogar",
                "make_donation": "Hacer una Donación",
                "donation_subtitle": "Tu apoyo transforma vidas y construye prosperidad",
                "volunteer_application": "Solicitud de Voluntariado",
                "volunteer_subtitle": "Únete a nuestro equipo de agentes de cambio y contribuye con tus habilidades",
                "corporate_partnerships": "Asociaciones Corporativas",
                "corporate_subtitle": "Oportunidades estratégicas para que las empresas impulsen el impacto social"
            },
             "pt": {
                "welcome": "Bem-vindo à Prosperity360",
                "home": "Início",
                "programs": "Pilares Estratégicos",
                "impact": "Nosso Impacto",
                "about": "Sobre Nós",
                "contact": "Contate-nos",
                "get_involved": "Envolva-se",
                "hero_title": "Transformando Vidas, Sistemas e Economias",
                "hero_description": "Uma instituição de desenvolvimento pan-africana, enraizada no Sul Global, e um mecanismo de entrega baseado em alianças dedicado a acelerar o bem-estar multidimensional, a transformação de sistemas locais e o desenvolvimento sustentável impulsionado pela comunidade.",
                "our_programs": "Nossos Programas",
                "subscribe_newsletter": "Assine nossa Newsletter",
                "stay_updated": "Mantenha-se atualizado com as últimas notícias, eventos e insights da Iniciativa de Desenvolvimento Prosperity360.",
                "enter_email": "Digite seu endereço de email",
                "subscribe": "Assinar",
                "mission_1": "A Prosperity360 Foundation é uma instituição de desenvolvimento pan-africana, enraizada no Sul Global, que acelera a prosperidade multidimensional, a transformação de sistemas e o desenvolvimento liderado pela comunidade em toda a África, América Latina, Sul da Ásia e outras regiões emergentes.",
                "mission_2": "Nossa missão é criar prosperidade sustentável por meio da inovação, empoderamento econômico e transformação comunitária em todo o Sul Global.",
                "mission_3": "Acreditamos na construção de sistemas que capacitam comunidades, transformam instituições e criam impacto duradouro para as gerações futuras.",
                "strategic_pillars": "Pilares Estratégicos",
                "pillars_subtitle": "Seis programas abrangentes que impulsionam a prosperidade multidimensional, a transformação de sistemas e o desenvolvimento liderado pela comunidade em todo o Sul Global.",
                "innovation": "Inovação & Sistemas",
                "economic": "Empoderamento Econômico",
                "agriculture": "Sistemas Alimentares",
                "energy": "Energia Limpa",
                "health": "Saúde & Saneamento",
                "education": "Educação",
                "quick_links": "Links Rápidos",
                "privacy_policy": "Política de Privacidade",
                "terms_service": "Termos de Serviço",
                "all_rights_reserved": "Todos os direitos reservados",
                "transforming_lives": "Transformando Vidas, Sistemas e Economias.",
                "who_we_are": "Quem Somos",
                "our_identity": "Nossa Identidade",
                "our_philosophy": "Nossa Filosofia",
                "philosophy_quote": "A prosperidade cresce quando as pessoas, os sistemas e as instituições trabalham em harmonia.",
                "case_for_foundation": "O Caso para uma Fundação de Prosperidade Africana/Sul Global",
                "multi_dimensional_framework": "Nosso Marco de Prosperidade Multidimensional",
                "framework_subtitle": "Medindo a prosperidade em seis dimensões para o desenvolvimento holístico",
                "ten_year_ambition": "Ambição de Impacto de Dez Anos (2025–2035)",
                "impact_subtitle": "Nossas metas ousadas para transformar vidas e sistemas em todo o Sul Global",
                "reach": "Alcançar",
                "deliver": "Entregar",
                "transform": "Transformar",
                "million_households": "Milhões de Lares",
                "thousand_communities": "Milhares de Comunidades",
                "countries": "Países",
                "million_entrepreneurs": "Milhões de Empreendedores",
                "million_stem_learners": "Milhões de Alunos STEM",
                "million_clean_energy": "Milhões com Energia Limpa",
                "prosperity_zones": "Zonas de Prosperidade",
                "national_systems": "Sistemas Nacionais",
                "farmers_supported": "Agricultores Apoiados",
                "delivery_architecture": "Nossa Arquitetura de Entrega",
                "architecture_subtitle": "Modelo de implementação globalmente inspirado, localmente enraizado",
                "community_level": "Nível Comunitário/Bairro",
                "district_hubs": "Centros Distritais",
                "state_platforms": "Plataformas Provinciais/Estaduais",
                "national_platforms": "Plataformas de Impacto Nacional",
                "regional_hubs": "Centros Regionais do Sul Global",
                "contact_us": "Contate-nos",
                "contact_subtitle": "Entre em contato com nossa equipe para saber mais, fazer parceria conosco ou apoiar nosso trabalho.",
                "get_in_touch": "Entre em Contato",
                "wed_love_to_hear": "Adoraríamos ouvir de você",
                "email_us": "Envie-nos um Email",
                "general_inquiries": "Consultas Gerais",
                "call_us": "Ligue para Nós",
                "visit_us": "Visite-nos",
                "connect_online": "Conecte-se Online",
                "send_us_message": "Envie-nos uma Mensagem",
                "follow_social": "Siga-nos nas redes sociais",
                "key_team_contacts": "Contatos Principais da Equipe",
                "frequently_asked": "Perguntas Frequentes",
                "global_presence": "Nossa Presença Global",
                "ways_to_engage": "Formas de Envolver-se",
                "engage_subtitle": "Múltiplos caminhos para contribuir com a prosperidade inclusiva",
                "donate": "Doar",
                "partner": "Tornar-se Parceiro",
                "volunteer": "Voluntariado",
                "advocate": "Defender",
                "make_donation": "Faça uma Doação",
                "donation_subtitle": "Seu apoio transforma vidas e constrói prosperidade",
                "volunteer_application": "Aplicação de Voluntário",
                "volunteer_subtitle": "Junte-se à nossa equipe de agentes de mudança e contribua com suas habilidades",
                "corporate_partnerships": "Parcerias Corporativas",
                "corporate_subtitle": "Oportunidades estratégicas para empresas impulsionarem o impacto social"
            },
        "ar": {
                "welcome": "مرحبًا بكم في بروسبيريتي 360",
                "home": "الرئيسية",
                "programs": "الركائز الاستراتيجية",
                "impact": "تأثيرنا",
                "about": "من نحن",
                "contact": "اتصل بنا",
                "get_involved": "شارك معنا",
                "hero_title": "تحويل الأرواح والأنظمة والاقتصادات",
                "hero_description": "مؤسسة تنمية إفريقية، متجذرة في الجنوب العالمي، وآلية تقديم قائمة على التحالف مكرسة لتسريع الرفاهية متعددة الأبعاد، وتحول الأنظمة المحلية، والتنمية المستدامة التي تقودها المجتمعات.",
                "our_programs": "برامجنا",
                "subscribe_newsletter": "اشترك في نشرتنا الإخبارية",
                "stay_updated": "ابق على اطلاع بأحدث الأخبار والأحداث والرؤى من مبادرة تنمية بروسبيريتي 360.",
                "enter_email": "أدخل عنوان بريدك الإلكتروني",
                "subscribe": "اشترك",
                "quick_links": "روابط سريعة",
                "privacy_policy": "سياسة الخصوصية",
                "terms_service": "شروط الخدمة",
                "all_rights_reserved": "جميع الحقوق محفوظة",
                "transforming_lives": "تحويل الأرواح والأنظمة والاقتصادات."
            }
            # Add more languages as needed...
        }
    
    def get_translations(self, language: str) -> Dict:
        """Get translations for specific language, fallback to English"""
        return self.translations.get(language, self.translations.get('en', {}))
    
    def get_available_languages(self) -> List[str]:
        """Get list of available language codes"""
        return list(self.translations.keys())
    
    def add_language(self, lang_code: str, translations: Dict):
        """Dynamically add a new language"""
        self.translations[lang_code] = translations

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================
def is_valid_email(email: str) -> bool:
    """Simple email validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def setup_logging():
    """Configure basic logging"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

# ============================================================================
# FLASK APPLICATION
# ============================================================================
app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.permanent_session_lifetime = Config.PERMANENT_SESSION_LIFETIME

# Initialize components
logger = setup_logging()
translation_manager = TranslationManager()

# ============================================================================
# REQUEST HANDLERS
# ============================================================================
@app.before_request
def before_request():
    """Set global variables for all templates"""
    g.current_language = session.get('language', Config.DEFAULT_LANGUAGE)
    g.all_languages = translation_manager.get_available_languages()
    g.translations = translation_manager.get_translations(g.current_language)

@app.after_request
def after_request(response):
    """Add security headers"""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

# ============================================================================
# LANGUAGE ROUTES
# ============================================================================
@app.route('/set-language/<lang>')
def set_language(lang):
    """Set user's preferred language"""
    if lang in translation_manager.get_available_languages():
        session['language'] = lang
        session.permanent = True
        logger.info(f"Language set to: {lang}")
    return redirect(request.referrer or url_for('home'))

@app.route('/api/languages')
def get_languages_api():
    """API endpoint to get available languages"""
    return jsonify({
        'available_languages': translation_manager.get_available_languages(),
        'current_language': session.get('language', Config.DEFAULT_LANGUAGE)
    })

# ============================================================================
# MAIN ROUTES
# ============================================================================
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

# Program subroutes
@app.route('/programs/innovation')
def innovation():
    return render_template('programs/innovation.html')

@app.route('/programs/economic')
def economic():
    return render_template('programs/economic.html')

@app.route('/programs/agriculture')
def agriculture():
    return render_template('programs/agriculture.html')

@app.route('/programs/energy')
def energy():
    return render_template('programs/energy.html')

@app.route('/programs/health')
def health():
    return render_template('programs/health.html')

@app.route('/programs/education')
def education():
    return render_template('programs/education.html')

@app.route('/impact')
def impact():
    return render_template('impact.html')

@app.route('/getinvolved')
def get_involved():
    return render_template('getinvolved.html')

# ============================================================================
# FORM HANDLING ROUTES
# ============================================================================
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return _handle_contact_form()
    return render_template('contact.html')

def _handle_contact_form():
    """Process contact form submission"""
    try:
        data = request.form.to_dict()
        
        # Validate required fields
        required_fields = ['name', 'email', 'message']
        missing_fields = [field for field in required_fields if not data.get(field)]
        
        if missing_fields:
            return jsonify({
                'success': False,
                'message': f"Missing fields: {', '.join(missing_fields)}"
            }), 400
        
        # Validate email
        if not is_valid_email(data['email']):
            return jsonify({
                'success': False,
                'message': 'Invalid email address'
            }), 400
        
        # Process form data (in production, save to DB or send email)
        logger.info(f"Contact form: {data['name']} ({data['email']}) - {data.get('subject', 'No subject')}")
        
        return jsonify({
            'success': True,
            'message': g.translations.get('contact_success', 'Thank you for your message!')
        })
        
    except Exception as e:
        logger.error(f"Contact form error: {str(e)}")
        return jsonify({
            'success': False,
            'message': g.translations.get('error_general', 'An error occurred')
        }), 500

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Process newsletter subscription"""
    try:
        email = request.form.get('email', '').strip()
        
        if not email:
            return jsonify({
                'success': False,
                'message': g.translations.get('required_field', 'Email is required')
            }), 400
        
        if not is_valid_email(email):
            return jsonify({
                'success': False,
                'message': g.translations.get('invalid_email', 'Invalid email address')
            }), 400
        
        # Process subscription (in production, save to DB)
        logger.info(f"New subscription: {email}")
        
        return jsonify({
            'success': True,
            'message': g.translations.get('subscribe_success', 'Thank you for subscribing!')
        })
        
    except Exception as e:
        logger.error(f"Subscription error: {str(e)}")
        return jsonify({
            'success': False,
            'message': g.translations.get('error_general', 'An error occurred')
        }), 500

# ============================================================================
# ERROR HANDLERS
# ============================================================================
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Server error: {str(error)}")
    return render_template('500.html'), 500

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        'success': False,
        'message': 'Method not allowed'
    }), 405

# ============================================================================
# UTILITY ROUTES
# ============================================================================
@app.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'healthy',
        'service': 'prosperity-foundation',
        'languages_loaded': len(translation_manager.translations)
    })

@app.route('/current-language')
def current_language():
    """Get current language info"""
    return jsonify({
        'current_language': g.current_language,
        'translations': g.translations
    })

# ============================================================================
# DYNAMIC LANGUAGE MANAGEMENT (Optional API)
# ============================================================================
@app.route('/api/add-language', methods=['POST'])
def add_language():
    """Dynamically add a new language (for admin use)"""
    try:
        data = request.json
        lang_code = data.get('code')
        lang_translations = data.get('translations')
        
        if not lang_code or not lang_translations:
            return jsonify({
                'success': False,
                'message': 'Language code and translations are required'
            }), 400
        
        translation_manager.add_language(lang_code, lang_translations)
        logger.info(f"Added new language: {lang_code}")
        
        return jsonify({
            'success': True,
            'message': f'Language {lang_code} added successfully',
            'available_languages': translation_manager.get_available_languages()
        })
        
    except Exception as e:
        logger.error(f"Add language error: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Failed to add language'
        }), 500

# ============================================================================
# APPLICATION ENTRY POINT
# ============================================================================
if __name__ == '__main__':
    # Configuration from environment
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 'yes')
    
    # Print startup info
    print(f"🚀 Starting Prosperity Foundation")
    print(f"   Port: {port}")
    print(f"   Debug: {debug}")
    print(f"   Available languages: {translation_manager.get_available_languages()}")
    print(f"   Default language: {Config.DEFAULT_LANGUAGE}")
    
    # Run the application
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug,
        use_reloader=debug
    )