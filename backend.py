import depen
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)


if not os.path.exists('emails.json'):
    with open('emails.json', 'w') as file:
        json.dump([], file)

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/submit', methods=['POST'])
def submit_email():
    email_with_flag = request.form['email']
    email, flag = email_with_flag.split(';')
    
   
    with open('emails.json', 'r') as file:
        emails = json.load(file)
    
    # Check if email already exists
    email_exists = False
    for i, existing_email_with_flag in enumerate(emails):
        existing_email, existing_flag = existing_email_with_flag.split(';')
        
        if existing_email == email:
            # Update flag if it differs
            if existing_flag != flag:
                emails[i] = email_with_flag
            email_exists = True
            break
    
    # Append the new email if it doesn't exist
    if not email_exists:
        emails.append(email_with_flag)
    
    # Save the updated emails list
    with open('emails.json', 'w') as file:
        json.dump(emails, file, indent=4)
    
    return jsonify({"message": "Vielen Dank für Ihre Anmeldung!"})

if __name__ == '__main__':
    app.run(debug=True)
