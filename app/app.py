import requests
from flask import Flask, request


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def main():
        return '<h1>Hello There! You IP is {}</h1>'.format(
            request.environ.get('X-Real-IP', request.remote_addr))

    @app.route('/test')
    def test_email():
        res = requests.post('http://email_service_producer/send_async_email',
                            json={
                                'To': 'best.sum@gmail.com',
                                'Subject': 'Hi test',
                                'Content': 'Just a test'
                            })
        return 'all good', 201

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
