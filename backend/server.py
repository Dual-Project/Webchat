from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask_sqlalchemy import SQLAlchemy

# App Configs
app = Flask(__name__, template_folder='../frontend/dist', static_folder='../frontend/dist/js')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/webchat'
app.config['SECRET_KEY'] = 'secret!'
io = SocketIO(app)
db = SQLAlchemy(app)


# Routes
@app.route('/')
def view():
    return render_template('index.html')


@io.on('message')
def handle_message(message):
    print('message: ' + message)
    send(message, broadcast=True)


@io.on('connect')
def test_connect():
    print('Client connected')


@io.on('disconnect')
def test_disconnect():
    print('Client disconnected')


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    io.run(app)
