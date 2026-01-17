import os
import json
import re
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

class TranslationManager:
    """Manages loading and accessing translations"""
    
    def __init__(self, translation_paths=None):
        self.translation_paths = translation_paths or [
            'translations/',
            'static/js/translations.json',
            'static/js/translations.js'
        ]
        self.translations = {}
        self.load_all_translations()
    
    def load_all_translations(self):
        """Load translations from all configured paths"""
        for path in self.translation_paths:
            if os.path.isdir(path):
                self._load_from_directory(path)
            elif os.path.isfile(path):
                self._load_from_file(path)
        
        if not self.translations:
            logger.warning("No translations loaded!")
            self.translations = {'en': {}}
    
    def _load_from_directory(self, directory_path: str):
        """Load translations from directory of JSON files (en.json, es.json, etc.)"""
        try:
            for filename in os.listdir(directory_path):
                if filename.endswith('.json'):
                    lang_code = filename.split('.')[0]
                    filepath = os.path.join(directory_path, filename)
                    
                    with open(filepath, 'r', encoding='utf-8') as f:
                        self.translations[lang_code] = json.load(f)
                        logger.info(f"Loaded translations for '{lang_code}' from {filepath}")
                        
        except Exception as e:
            logger.error(f"Error loading translations from directory {directory_path}: {e}")
    
    def _load_from_file(self, filepath: str):
        """Load translations from a single file (JSON or legacy JS)"""
        if not os.path.exists(filepath):
            return
        
        try:
            if filepath.endswith('.json'):
                self._load_json_file(filepath)
            elif filepath.endswith('.js'):
                self._load_js_file(filepath)
                
        except Exception as e:
            logger.error(f"Error loading translations from {filepath}: {e}")
    
    def _load_json_file(self, filepath: str):
        """Load translations from JSON file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # Handle both formats: {lang: {...}} and {...} (single language)
            if isinstance(data, dict):
                if all(key in data for key in ['en', 'es', 'fr']):  # Multi-language format
                    self.translations.update(data)
                else:  # Single language format
                    # Try to detect language from filename
                    lang = os.path.basename(filepath).split('.')[0]
                    if lang in ['translations', 'translation']:
                        lang = 'en'  # Default
                    self.translations[lang] = data
    
    def _load_js_file(self, filepath: str):
        """Load translations from legacy JS file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Remove JS comments
            content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
            content = re.sub(r'//.*', '', content)
            
            # Extract JSON object
            match = re.search(r'translations\s*=\s*({.*?})\s*;', content, re.DOTALL)
            if match:
                json_str = match.group(1)
                
                # Fix common JS JSON issues
                json_str = re.sub(r',\s*([}\]])', r'\1', json_str)  # Remove trailing commas
                json_str = re.sub(r'([{,])\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*:', r'\1"\2":', json_str)  # Quote keys
                
                try:
                    data = json.loads(json_str)
                    self.translations.update(data)
                except json.JSONDecodeError as e:
                    logger.error(f"Failed to parse JS translations: {e}")
    
    def get_translations(self, language: str) -> Dict:
        """Get translations for a specific language"""
        return self.translations.get(language, self.translations.get('en', {}))
    
    def get_available_languages(self) -> List[str]:
        """Get list of available language codes"""
        return list(self.translations.keys())
    
    def reload_translations(self):
        """Reload translations (useful for development)"""
        self.translations.clear()
        self.load_all_translations()