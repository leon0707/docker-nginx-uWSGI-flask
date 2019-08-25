from flask import Flask, request

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return '<h1>Hello There! You IP is {}</h1>'.format(
            request.environ.get('X-Real-IP', request.remote_addr))

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
