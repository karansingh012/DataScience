from flask import Flask,render_template

"""
It creates an instance of the flask class 
which will be WSGI (Web server gateway interface) application.
"""
## WSGI Application
app = Flask(__name__)

@app.route("/")
def Welcome():
    # return "<html><h1>Welcome to my new page</h1></html>"
    return 
@app.route("/index")
def Index_page():
    return render_template("index.html")
@app.route("/about")
def about_page():
    return render_template("about.html")

if __name__=="__main__":
    # app.run()
    app.run(debug=True) ## age hum isse likhte hai toh hum site pr jaise hi refresh krnege turnt yha pr update kiya hua vha show hone lagege

