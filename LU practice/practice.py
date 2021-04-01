import flask

application = flask.Flask(__name__)


@application.route('/')
def index():
    return 'Hello World'


@application.route('/hello/')
def hello():
    name = flask.request.form['name']

    return f'Hello, {name}'

