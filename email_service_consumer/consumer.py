import traceback
from celery import Celery, states
from celery.utils.log import get_task_logger
from celery.exceptions import Ignore
from email_plugin import send_email

logger = get_task_logger('Send Email')

# module is 'email'
app = Celery('email',
             broker='amqp://rabbitmq_user:password@rabbitmq:5672/my_vhost',
             backend='rpc://')

@app.task(bind=True, rate_limit='200/s')
def send_async_email(self, email_json):
    try:
        send_email(email_json)
        self.update_state(state=states.SUCCESS)
    except Exception as e:
        logger.info(
            'Task: send_async_email \t Task id:{0.id} \t Task kwargs:{0.kwargs!r}\nException:{1}'.format(
                self.request,
                ''.join(traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__))
                ))
        self.update_state(state=states.FAILURE, meta={
            'exception_type': type(e).__name__,
            'exception_message': traceback.format_exc().split('\n')
        })
        raise Ignore()

if __name__ == '__main__':
    argv = [
        'worker',
        '--loglevel=DEBUG',
        '--queues=email'
    ]
    # only work on messages in queue 'email'
    app.worker_main(argv)
