import os
basedir = os.path.abspath(os.path.dirname(__file__))

# login stuff
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'


OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '125492684468652',
        'secret': 'ac27e7025d4047ce9722d89a0ed045f0'
    },
    'twitter': {
        'id': 'xIStL0E3bf6v6nyUw3g89pGeu',
        'secret': 'lUjEtyqRIb1d5Le0MruxQZGJIzj7eaLxN5jA8hc0rGNM6mgIyL'
    }}

# SQLalchemy stuff
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
# HACK: as os.environ.get isn't reading the environment variables for some reason
with open('../email_stuff.txt','r') as f:
    email_stuff = f.read().split('\n')
KiW_MAIL_USERNAME = email_stuff[0]
KiW_MAIL_PASSWORD = email_stuff[1]

MAIL_USERNAME = email_stuff[0]
MAIL_PASSWORD = email_stuff[1]
# administrator list
ADMINS = ['emailtoknowitwall@gmail.com']
KIW_TEAM = ['jeremie.coullon@gmail.com', 'mfdsantos86@gmail.com','anguswaite@gmail.com', 'team@knowitwall.com']
