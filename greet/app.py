from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    welcome = '''           
            <html>
                <body>
                  <h1>Welcome<h1>
                </body>  
            </html>'''
    return welcome

@app.route('/welcome/home')
def home():
    welcome = '''           
            <html>
                <body>
                  <h1>Welcome Home<h1>
                </body>  
            </html>'''
    return welcome

@app.route('/welcome/back')
def back():
    welcome = '''           
            <html>
                <body>
                  <h1>Welcome Back<h1>
                </body>  
            </html>'''
    return welcome
