from flask_mail import Message
from app import app, mail
from flask import render_template
from config import ADMINS, KIW_TEAM
from .decorators import async

@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(app, msg)



def user_feedback_email(user_name, user_email, feedback_overall):
    send_email("Knowitwall contact form, message by: {}".format(user_name),
               ADMINS[0],
               KIW_TEAM,
               render_template("user_feedback_email.txt",user_name=user_name, user_email=user_email, feedback_overall=feedback_overall),
               render_template("user_feedback_email.html",user_name=user_name, user_email=user_email, feedback_overall=feedback_overall))
