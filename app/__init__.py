from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask.ext.login import LoginManager, UserMixin
from flask.ext.openid import OpenID
from config import basedir
from flask_mail import Mail

app = Flask(__name__, static_folder='static')
app.config.from_object('config')

mail = Mail(app)
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
lm.login_view = 'login'



from app import views, models, oauth
