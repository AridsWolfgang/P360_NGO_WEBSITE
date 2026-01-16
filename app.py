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

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
import json
from datetime import timedelta  # Added for session timeout control

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'prosperity-must-flow') 
app.permanent_session_lifetime = timedelta(days=7)  # Set session lifetime

# Load translations - fixed approach
def load_translations():
    translations_path = "static/js/translations.js"
    if os.path.exists(translations_path):
        try:
            with open(translations_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract JSON part from JavaScript file
                # Assuming format: var translations = {...};
                start = content.find('{')
                end = content.rfind('}') + 1
                if start != -1 and end != 0:
                    json_str = content[start:end]
                    return json.loads(json_str)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error loading translations: {e}")
    return {}

# Load translations at startup
translations = load_translations()

@app.route('/set-language/<lang>')
def set_language(lang):
    session['language'] = lang
    session.permanent = True  # Make session permanent
    return redirect(request.referrer or url_for('home'))

@app.context_processor
def inject_language():
    # Get language from session or default to 'en'
    language = session.get('language', 'en')
    # Get translations for current language
    current_translations = translations.get(language, translations.get('en', {}))
    return dict(
        current_language=language,
        translations=current_translations,
        all_languages=translations.keys()
    )

# Helper function to render templates with language
def render_with_language(template_name, **kwargs):
    language = session.get('language', 'en')
    return render_template(template_name, language=language, **kwargs)

@app.route('/')
def home():
    return render_with_language('index.html')

@app.route('/about')
def about():
    return render_with_language('about.html')

@app.route('/programs')
def programs():
    return render_with_language('programs.html')

@app.route('/programs/innovation')
def innovation():
    return render_with_language('programs/innovation.html')

@app.route('/programs/economic')
def economic():
    return render_with_language('programs/economic.html')

@app.route('/programs/agriculture')
def agriculture():
    return render_with_language('programs/agriculture.html')

@app.route('/programs/energy')
def energy():
    return render_with_language('programs/energy.html')

@app.route('/programs/health')
def health():
    return render_with_language('programs/health.html')

@app.route('/programs/education')
def education():
    return render_with_language('programs/education.html')

@app.route('/impact')
def impact():
    return render_with_language('impact.html')

@app.route('/getinvolved')
def get_involved():
    return render_with_language('getinvolved.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # Add validation
            required_fields = ['name', 'email', 'message']
            for field in required_fields:
                if not data.get(field):
                    return jsonify({
                        'success': False, 
                        'message': f'Missing required field: {field}'
                    })
            
            # Here you would typically save to database or send email
            print(f"Contact form submitted: {data}")
            # For production, consider using logging instead of print
            # import logging
            # logging.info(f"Contact form submitted: {data}")
            
            return jsonify({
                'success': True, 
                'message': 'Thank you for your message! We will get back to you soon.'
            })
        except Exception as e:
            print(f"Error processing contact form: {e}")
            return jsonify({
                'success': False, 
                'message': 'An error occurred. Please try again later.'
            }), 500
    
    return render_with_language('contact.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        email = request.form.get('email')
        if not email:
            return jsonify({
                'success': False, 
                'message': 'Please provide a valid email'
            }), 400
        
        # Basic email validation
        if '@' not in email or '.' not in email.split('@')[-1]:
            return jsonify({
                'success': False, 
                'message': 'Please provide a valid email address'
            }), 400
        
        # Here you would typically save to database
        print(f"New subscription: {email}")
        # In production, consider using a proper email subscription service
        
        return jsonify({
            'success': True, 
            'message': 'Thank you for subscribing to our newsletter!'
        })
    except Exception as e:
        print(f"Error processing subscription: {e}")
        return jsonify({
            'success': False, 
            'message': 'An error occurred. Please try again later.'
        }), 500

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_with_language('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_with_language('500.html'), 500

if __name__ == '__main__':
    # For production, use environment variables
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)