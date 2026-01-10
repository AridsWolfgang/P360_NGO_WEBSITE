from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        # Here you would typically save to database or send email
        print(f"Contact form submitted: {data}")
        return jsonify({'success': True, 'message': 'Thank you for your message!'})
    return render_template('contact.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    if email:
        # Here you would typically save to database
        print(f"New subscription: {email}")
        return jsonify({'success': True, 'message': 'Thank you for subscribing!'})
    return jsonify({'success': False, 'message': 'Please provide a valid email'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)