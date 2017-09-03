# -*- coding: utf-8 -*-
import mimetypes
import re
import os
import datetime
import jwt
from flask import json, url_for, send_file, flash, redirect, session, g
from flask import render_template, request, send_from_directory, Response
from flask.ext.login import login_user, logout_user, current_user, login_required, AnonymousUserMixin
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User, Episode, Flash_Seminars
from oauth import OAuthSignIn
import time
from config import KiW_MAIL_USERNAME, KiW_MAIL_PASSWORD
from .emails import user_feedback_email

"""----------------------------------------------------------------------------------------------------
To change audio-doc:
1) change path to audio in 'sending files partially' section
2) change path to json file in the relevant audio-doc section
----------------------------------------------------------------------------------------------------"""

# customize anonymouse user



@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.after_request
def after_request(response):
    response.headers.add('Accept-Ranges', 'bytes')
    return response


"----------------------------------------------------------------------------------------------------"
"""
To create a new audio-doc, create a new json file with the links to images,audio etc..
Then add it to the audiodoc_list
"""
all_audiodocs = [
    'carbon_cycle.json', 'captain_america_politics.json', 'GBI_philosopher.json', 'crazy_or_physics.json', 'science_of_attraction.json', 'spanish_forger.json', 'neurons_move_with_you.json',
    'stem_cell_hotel.json', 'blast_injury.json', 'modify_genome.json', 'emotional_expression.json',
    'US_constitution.json', 'migrant_crisis.json', 'earth_habitable.json', 'quantum_computers.json', 'russia_west.json',
    'string_theory.json','quantum_life.json', 'flying_spying.json', 'sport_society.json','dante_750.json',
     'human_language.json', 'higgs_boson.json', 'real_shakespeare.json',
    'neural_cartography.json', 'saharan_dust.json', 'viral_pandemics.json', 'memory_bike.json',
    'antartica_discovery.json', 'stegosaurus.json', 'ganymede.json', 'tate.json'
    ]

"VIEWS"
"----------------------------------------------------------------------------------------------------"
"home page"

@app.route('/')
def index():
    audiodocs = [Episode(ad) for ad in all_audiodocs[:13]]
    return render_template('knowitwall.html', audiodocs=audiodocs)

"----------------------------------------------------------------------------------------------------"
"about page"

@app.route('/about')
def about():
    flash_seminars = [Flash_Seminars('flash_sem_migrant_crisis.json')]
    return render_template('about_page.html', flash_seminars=flash_seminars)



"----------------------------------------------------------------------------------------------------"
" audiodoc page"

@app.route('/episodes/<url>')
@app.route('/audiodoc/<url>')
def audiodoc(url):
    audiodocs = [Episode(url+'.json')]
    return render_template('episode_page.html', audiodocs=audiodocs)


"----------------------------------------------------------------------------------------------------"
" TEST: audiodocs page with annotations "

@app.route('/audiodoc_annotations/<url>')
def audiodoc_annotations(url):
    # put all audiodoc information in the variable audiodoc
    audiodocs = [Episode(url+'.json')]

    # read_only permission
    # set user_nickname variable
    if current_user.is_anonymous():
        user_nickname='anonymous'
    else:
        user_nickname = str(current_user.nickname)

    # if the user is in list of allowed users, then the user can create annotations. Otherwise no
    create_permission = ['jeremie.coullon', 'JeremieCoullon']
    if user_nickname in create_permission:
        read_only = 'false'
    else:
        read_only = 'true'

    return render_template('episode_page_annotations.html', audiodocs=audiodocs, read_only=read_only)


"----------------------------------------------------------------------------------------------------"
" archive page "

@app.route('/all_episodes')
def archive():
    audiodocs = [Episode(ad) for ad in all_audiodocs]
    # sort the episodes alphabetically by title
    audiodocs_alphabetical = sorted(audiodocs, key=lambda k: k.topic_name)

    return render_template('archive_page.html', audiodocs = audiodocs_alphabetical)


"----------------------------------------------------------------------------------------------------"
" terms and conditions "

@app.route('/terms')
def terms():
    return render_template('terms.html')


"----------------------------------------------------------------------------------------------------"
"method for AJAX contact form "

@app.route('/contactform', methods=['POST'])
def contactform():
    """
    Send email to KiW team containing the user feedback
    """
    user_name =  request.form['name'];
    user_email = request.form['email'];
    feedback_overall = request.form['feedback_overall'];
    user_feedback_email(user_name=user_name, user_email=user_email, feedback_overall=feedback_overall)
    return 'user feedback email sent'



"----------------------------------------------------------------------------------------------------"
" login using OAuh (facebook and twitter) "

# authorize route. This redirects the user to Facebook or Twitter to allow KiW to access data
@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous():
        return redirect(url_for('userlogin'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()

# callback route: this is where facebook/twitter send auth info to KiW
@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous():
        return redirect(url_for('userlogin'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('userlogin'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, nickname=username, email=email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('userlogin'))

"----------------------------------------------------------------------------------------------------"
" secret login form "

@app.route('/supersecretlogin')
def userlogin():
    return render_template('secretlogin.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('userlogin'))


"----------------------------------------------------------------------------------------------------"
" AnnotateIt token generation "

# old keys
# CONSUMER_KEY = 'd4c108122b51434aab1d27ad4ebd2b02'
# CONSUMER_SECRET = '36977e7b-be7f-4b57-a9eb-9617e4740b6a'

# new keys
CONSUMER_KEY =  '6a0f096a1e4347a8bbddfc3f1857f71b'
CONSUMER_SECRET =  '1f489b5a-d218-4f7e-b132-bfbe16a69519'

# Only change this if you're sure you know what you're doing
CONSUMER_TTL = 86400


# anonymous shizzle


@app.route('/api/token')
def generate_token():
    if current_user.is_anonymous():
        user_id='0'
    else:
        user_id = str(current_user.id)
        # user_nickname = str(current_user.nickname)
    return jwt.encode({
      'consumerKey': CONSUMER_KEY,
      'userId': user_id,
	  'isAdmin': 1,    """'TODO:' == 'Put bool here',"""
	  'displayName': "TODO: put user nickname",
      'issuedAt': _now().isoformat() + 'Z',
      'ttl': CONSUMER_TTL
    }, CONSUMER_SECRET)

def _now():
    return datetime.datetime.utcnow().replace(microsecond=0)
