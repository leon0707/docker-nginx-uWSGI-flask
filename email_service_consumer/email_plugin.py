import smtplib
from os import environ
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


if environ.get('SMTP_SERVER') is None:
    raise ValueError('SMTP_SERVER is not configured')

if environ.get('SMTP_PORT') is None:
    raise ValueError('SMTP_PORT is not configured')

if environ.get('SENDER_EMAIL') is None:
    raise ValueError('SENDER_EMAIL is not configured')

if environ.get('SENDER_PASSWORD') is None:
    raise ValueError('SMTP_PASSWORD is not configured')


def send_email(email_json):
    server = smtplib.SMTP(host=environ['SMTP_SERVER'], port=environ['SMTP_PORT'])
    server.starttls()
    server.login(environ['SENDER_EMAIL'], environ['SENDER_PASSWORD'])

    msg = MIMEMultipart()

    msg['From']=environ['SENDER_EMAIL']
    msg['To']=email_json['To']
    msg['Subject']=email_json['Subject']
    msg.attach(MIMEText(email_json['Content'], 'plain'))
    server.send_message(msg)

    del msg
    server.quit()
    del server
