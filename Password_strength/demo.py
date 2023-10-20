




from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password_strength', methods=['POST'])
def check_password_strength():
    password = request.form['password']
    strength = calculate_password_strength(password)
    return jsonify({'strength': strength})

def calculate_password_strength(password):
    length = len(password)
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special_char = any(c in "!@#$%^&*()-_=+[]{};:'\"<>,.?/" for c in password)

    if length >= 8 and has_lowercase and has_uppercase and has_digit and has_special_char:
        return 'strong'
    elif length >= 6:
        return 'medium'
    else:
        return 'weak'

if __name__ == '__main__':
    app.run()
