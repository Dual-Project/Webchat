from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.template_folder = "../frontend/dist"
app.static_folder = "../frontend/dist/css"
socketio = SocketIO(app)


@app.route('/')
def view():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app)
