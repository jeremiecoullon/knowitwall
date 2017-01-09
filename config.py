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

# mail stuff
# it doesn't work online though for some reason..
# KiW_MAIL_USERNAME = os.environ.get('KiW_MAIL_USERNAME', '')
# KiW_MAIL_PASSWORD = os.environ.get('KiW_MAIL_PASSWORD', '')

# HACK, as os.environ.get isn't reading the environment variables for some reason
with open('../email_stuff.txt','r') as f:
    email_stuff = f.read().split('\n')
KiW_MAIL_USERNAME = email_stuff[0]
KiW_MAIL_PASSWORD = email_stuff[1]
