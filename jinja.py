## Building url dynamically 
## variable rule 
## Jinja 2 template engine 
from flask import Flask, render_template, request

"""
It creates an instance of the flask class 
which will be WSGI (Web server gateway interface) application.
"""
## WSGI Application
app = Flask(__name__)

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
def success(score):
    return "the marks you got is " + str(score)

if __name__ == "__main__":
    app.run(debug=True)