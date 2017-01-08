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
le_username = os.environ.get('KiW_MAIL_USERNAME', '')
le_password = os.environ.get('KiW_MAIL_PASSWORD', '')
