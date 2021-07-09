from flask import Flask

app = Flask(__name__)


@app.route('/')
def view():
    return 'WebChat!'


if __name__ == '__main__':
    app.run()