# coding:utf-8
from flask_mail import Mail

mail = Mail()

def init_mail(app):
    mail.init_app(app)