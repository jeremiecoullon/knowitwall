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



OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

# SQLalchemy stuff
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
