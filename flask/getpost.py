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

@app.route("/form", methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template("form.html")
@app.route("/form", methods=['GET', 'POST'])
def sub():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Hello {name}!"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)