from flask import Flask

"""
It creates an instance of the flask class 
which will be WSGI (Web server gateway interface) application.
"""
## WSGI Application
app = Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to my first page. This is my page"
@app.route("/index")
def Index_page():
    return "Welcome to my index page."

if __name__=="__main__":
    # app.run()
    app.run(debug=True) ## age hum isse likhte hai toh hum site pr jaise hi refresh krnege turnt yha pr update kiya hua vha show hone lagege

