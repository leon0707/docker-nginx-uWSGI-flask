broker_url = 'amqp://rabbitmq_user:password@rabbitmq:5672/my_vhost'
enable_utc = True
accept_content = ['json']
accept_content = ['application/json']

# task 'send_async_email' will be delivered to queue 'email'
task_routes = {
    'email.send_async_email': {'queue': 'email'}
}

result_backend = 'rpc://'
# messages will be lost after a broker restart
result_persistent = False
