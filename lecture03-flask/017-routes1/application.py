from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello, world!"

@app.route("/<string:name>")
def hello(name):
	name = name.capitalize()
	# return f"Hello, {name}!"				# Python ver 3.6- string literals
	return f"<h1>Hello, {name}!</h1>"		# Python ver 3.6- string literals
	# return "Hello, {}!".format(name)		# Python ver 3.5