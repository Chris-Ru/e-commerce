import projects
from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy 

#create a Flask instance
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']

#connects default URL to a function
@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html", projects=projects.setup())

@app.route('/amazon/')
def amazon():
    return render_template("amazon.html", projects=projects.setup())

@app.route('/template1')
def testing():
    return render_template("template1.html", projects=projects.setup())

@app.route('/selfgrade/')
def selfgrade():
    return render_template("selfgrade.html", projects=projects.setup())

@app.route('/navbarrotation/')
def navbarrotation():
    return render_template("navbarrotation.html", projects=projects.setup())

@app.route('/test')
def test():
    return render_template("test.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='127.0.0.1')


