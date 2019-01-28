from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello, world!"	# change to return "Hello, world!!!" and refresh browser to see updated web apps