
#Importing the flask class from flask module
from flask import Flask, render_template

#Create the instance of the flask web application
app = Flask(__name__)

#Define the route for home page
@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/")
def index():
    return render_template("index.html")

#Define the route for register page
@app.route("/register")
def register():
    return render_template("register.html")

#Define the route for the login page
@app.route("/login")
def login():
    return render_template("login.html")

#Start the Flask application in Debug mode
if __name__ == "__main__":
    app.run(debug=True)


