from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return "About Page"

 
@app.route('/login')          
def login():                  
    return "Login Page - Feature Branch"   

@app.route('/login')
def login():
    return "Login Page - Feature Branch"

@app.route('/contact')          
def contact():                  
    return "Contact Page - Feature Contact Branch" 


if __name__ == '__main__':
    app.run(debug=True)