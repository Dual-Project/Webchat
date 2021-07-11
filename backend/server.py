from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__, template_folder='../frontend/dist', static_folder='../frontend/dist/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def view():
    return render_template('index.html')


@socketio.on('message')
def handle_message(message):
    print('message: ' + message)
    send(message, broadcast=True)


@socketio.on('connect')
def test_connect():
    print('Client connected')


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
