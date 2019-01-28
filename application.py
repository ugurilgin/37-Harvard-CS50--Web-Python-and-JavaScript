from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello, world!"

@app.route("/<string:name>")
def hello(name):
	name = "Budi" + name.capitalize()
	headline = "Hello, " + name
	# return f"<h1>{headline}!</h1>"
	# headline = "Hello, " + name + "!"
	# return f"<h1> Bebek, {name}</h1>"
	return render_template("index.html", headline=headline)