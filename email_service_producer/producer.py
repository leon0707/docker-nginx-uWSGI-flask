from flask import Flask, request
from celery import Celery
from celery.exceptions import OperationalError
from celery.utils.log import get_task_logger

logger = get_task_logger('Send Email')

def create_app():
    app = Flask(__name__)

    celery = Celery()
    # celery config
    celery.config_from_object('celeryconfig')


    @app.route('/send_async_email', methods=['POST'])
    def send_async_email():
        try:
            result = celery.send_task('email.send_async_email',
                                    args=[request.get_json()])
            return 'Succee', 200
        except OperationalError as e:
            logger.exception('Sending task raised: %r', e)
            return 'Something is wrong', 500

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
