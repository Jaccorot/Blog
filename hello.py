from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
	return "This is my python page."

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name = 1):
	return render_template("hello.html",name=name)

@app.route('/name/<username>')
def say_hi(username):
	return "It is %s,is that right?" % username

@app.route('/number/<int:work_id>')
def show_id(work_id):
	return "Your number is %d,is that right?" % work_id



if __name__ == "__main__":
	app.run(debug = True , host = '0.0.0.0')
