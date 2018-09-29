from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('index.html')
    return template.render()

@app.route("/", methods=['POST', 'GET'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verifyPassword = request.form['verifyPassword']
    email = request.form['email']

    if username and password and verifyPassword:
        if (len(username)<20 and len(username)>3 and (' ' in username) == False) and (len(password)<20 and len(password)>3 and (' ' in password) == False) and (len(verifyPassword)<20 and len(verifyPassword)>3 and (' ' in verifyPassword) == False):
            template = jinja_env.get_template('hello.html') 
        # else:
        #     template = jinja_env.get_template('index.html') 
        #     warning1 = "Fields empty"
                   
       
    return template.render(name=username, passw=password, veri=verifyPassword, email=email, )


app.run()

    #    if (len(username)<20 and len(username)>3 and (username.isspace() == True)) and (len(password)<20 and len(password)>3 and (password.isspace() == True)) and (len(verifyPassword)<20 and len(verifyPassword)>3 and (verifyPassword.isspace() == True)):
    # warning1=warning1