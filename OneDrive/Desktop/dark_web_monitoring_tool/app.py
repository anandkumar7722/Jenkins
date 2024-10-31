# app.py
from flask import Flask, request, jsonify, render_template
from models.user import User
from dark_web_scanner import DarkWebScanner
from alert_manager import AlertManager

app = Flask(__name__)

# User Registration Route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    # Check if user already exists
    if User.find_by_email(email):
        return jsonify({"error": "User already exists"}), 400
    
    # Create new user and save to database
    new_user = User(email, password)
    new_user.save()
    
    return jsonify({"message": "User registered successfully"}), 201

# User Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    user = User.find_by_email(email)
    if not user or not User.verify_password(password, user['password']):
        return jsonify({"error": "Invalid credentials"}), 400
    
    return jsonify({"message": "Login successful"}), 200

# Dark Web Scan Route
@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    email = data['email']
    
    # Perform dark web scan for the provided email
    breaches = DarkWebScanner.check_leaked_data(email)
    if breaches:
        # Send alert to the user if any breaches are found
        AlertManager.send_alert(email, breaches)
        return jsonify({"message": "Alert sent. Breach found!"}), 200
    
    return jsonify({"message": "No breach found for this email."}), 200

# Dashboard (Frontend)
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
