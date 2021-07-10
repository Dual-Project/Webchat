from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO

app = Flask(__name__, template_folder='../frontend/dist', static_folder='../frontend/dist/js')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def view():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app)
