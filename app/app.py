from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return '<h1>Hello There!</h1>'

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
