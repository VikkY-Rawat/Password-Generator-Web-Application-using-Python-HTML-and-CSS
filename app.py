from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_upper, use_digits, use_symbols):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()_+-=[]{};:,.<>?/|"

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        length = int(request.form.get('length', 8))
        use_upper = 'uppercase' in request.form
        use_digits = 'digits' in request.form
        use_symbols = 'symbols' in request.form
        password = generate_password(length, use_upper, use_digits, use_symbols)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
