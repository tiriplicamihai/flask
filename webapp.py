import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
	return flask.render_template('home.html')

if __name__ == '__main__':
	app.run()
