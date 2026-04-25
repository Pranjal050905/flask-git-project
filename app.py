from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return "About Page"

@app.route('/login')          # ← ADD THIS
def login():                  # ← ADD THIS
    return "Login Page - Feature Branch"   # ← ADD THIS

if __name__ == '__main__':
    app.run(debug=True)