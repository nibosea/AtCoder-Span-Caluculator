import os
from flask import Flask, url_for

#app = Flask(__name__, static_folder='.', static_url_path='')
app = Flask(__name__)

#ルーティング
@app.route("/hello")
def hello_world():
	return "Hello world"

@app.route('/')
def index():
	return url_for("show_user_profile", username="ai_academy")
	return app.send_static_file('index.html')

@app.route("/post/<int:post_id>")
def show_post(post_id):
	return "Post" + str(post_id)

if __name__ == "__main__":
	app.run(port=8000,debug=True)
