from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	headline = "Hello, world!"
	return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
	headline = "Goodbye!"
	return render_template("index.html", headline=headline)

@app.route("/<string:name>")
def hello(name):
	name = name.capitalize()
	headline = "Hello, " + name + "!"
	return render_template("index.html", headline=headline)