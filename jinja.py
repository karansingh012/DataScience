## Building url dynamically 
## variable rule 
## Jinja 2 template engine 
## jinja2 Template engine is used by flask to render templates
'''
{{. .. }} -> expression to print to the template output
{% .. %} -> conditions   statements like for, if, etc
{# .. #} -> comments
{% extends "base.html" %} -> to inherit a base template 
'''

from flask import Flask, render_template, request

"""
It creates an instance of the flask class 
which will be WSGI (Web server gateway interface) application.
"""
## WSGI Application
app = Flask(__name__, template_folder="Templates")

@app.route("/")
def Welcome():
    return "<html><h1>Welcome to my new page</h1></html>"

@app.route("/index", methods=['GET'])
def Index_page():
    return render_template("index.html")

@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/submit", methods=['GET', 'POST'])
def sub():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Hello {name}!"
    return render_template("form.html")

# ## Variable rules
# @app.route("/success/<score>")
# def success(score):
#     return f"the score is {score}"
## Variable rules
@app.route("/success/<int:score>")
@app.route("/successres/<int:score>")
def success(score):
    res = "Pass" if score >= 50 else "Fail"
    exp = {"result": res, "score": score}
    return render_template("result1.html", exp=exp)
## If condition in jinja template
@app.route("/successif/<int:score>")
def success_if(score):
    return render_template("result2.html", results=score)
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'password':
            return "Login Successful!"
        else:
            return "Invalid Credentials. Please try again."
    return render_template("login.html")
# run the application
 
if __name__ == "__main__":
    app.run(debug=True)
