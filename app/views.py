# -*- coding: utf-8 -*-
import mimetypes
import re
import os
import yagmail
import datetime
import jwt
from flask import json, url_for, send_file, flash, redirect, session, g
from flask import render_template, request, send_from_directory, Response
from flask.ext.login import login_user, logout_user, current_user, login_required, AnonymousUserMixin
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User, Episode
from oauth import OAuthSignIn
import time

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

"FUNCTIONS"
"----------------------------------------------------------------------------------------------------"
"send_file_partial function"

def send_file_partial(path):
    """
        Simple wrapper around send_file which handles HTTP 206 Partial Content
        (byte ranges)
        TODO: handle all send_file args, mirror send_file's error handling
        (if it has any)
    """
    range_header = request.headers.get('Range', None)
    if not range_header: return send_from_directory(app.static_folder, path)

    new_path=os.path.join('app/static/',path)

    size = os.path.getsize(new_path)
    byte1, byte2 = 0, None

    m = re.search('(\d+)-(\d*)', range_header)
    g = m.groups()

    if g[0]: byte1 = int(g[0])
    if g[1]: byte2 = int(g[1])

    length = size - byte1
    if byte2 is not None:
        length = byte2 - byte1+1

    data = None
    with open(new_path, 'rb') as f:
        f.seek(byte1)
        data = f.read(length)

    rv = Response(data,
        206,
        mimetype=mimetypes.guess_type(new_path)[0],
        direct_passthrough=True)
    rv.headers.add('Content-Range', 'bytes {0}-{1}/{2}'.format(byte1, byte1 + length - 1, size))

    return rv

"----------------------------------------------------------------------------------------------------"
"sending files partially"

@app.route('/audio/its_at_tate.mp3')
@app.route('/audio/could_there_be_life_around_Jupiter.mp3')
@app.route('/audio/stegosaurus_spikes.mp3')
@app.route('/audio/antartica_discovery.mp3')
@app.route('/audio/memory_keys.mp3')
@app.route('/audio/viral_pandemics.mp3')
@app.route('/audio/saharan_dust.mp3')
@app.route('/audio/neural_cartography.mp3')
@app.route('/audio/real_shakespeare.mp3')
@app.route('/audio/higgs_boson.mp3')
@app.route('/audio/human_language.mp3')
@app.route('/audio/blast_injury.mp3')
@app.route('/audio/flying_spying.mp3')
@app.route('/audio/migrant_crisis.mp3')
@app.route('/audio/Dante_750.mp3')
@app.route('/audio/sport_society.mp3')
@app.route('/audio/US_constitution.mp3')
@app.route('/audio/spanish_forger.mp3')
@app.route('/audio/quantum_life.mp3')
@app.route('/audio/string_theory.mp3')
@app.route('/audio/russia_west.mp3')
def static_from_root():
    return send_file_partial(request.path[1:])




"----------------------------------------------------------------------------------------------------"
"""
To create a new audio-doc, create a new json file with the links to images,audio etc..
Then add it to the audiodoc_list
"""
all_audiodocs = [
    'emotional_expression.json',
    'earth_habitable.json','modify_genome.json','russia_west.json','string_theory.json','quantum_life.json',
    'flying_spying.json','spanish_forger.json','US_constitution.json', 'sport_society.json','dante_750.json',
    'migrant_crisis.json', 'blast_injury.json', 'human_language.json', 'higgs_boson.json', 'real_shakespeare.json',
    'neural_cartography.json', 'saharan_dust.json', 'viral_pandemics.json', 'memory_bike.json',
    'antartica_discovery.json', 'stegosaurus.json', 'ganymede.json', 'tate.json'
    ]

"VIEWS"
"----------------------------------------------------------------------------------------------------"
"home page"

@app.route('/')
def index():
    audiodocs = [Episode(ad) for ad in all_audiodocs[:9]]
    return render_template('knowitwall.html', audiodocs=audiodocs)


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
    regular expression to remove html tag from ad_name, otherwise the sent message
    is all on one line
    """
    TAG_RE = re.compile(r'<[^>]+>')
    def remove_tags(text):
        return TAG_RE.sub('', text)


    name =  request.form['name'];
    email = request.form['email'];
    feedback_overall = request.form['feedback_overall'];
    ad_name_html = request.form['ad_name'];
    ad_name = remove_tags(ad_name_html)
    jeremie ='jeremie.coullon@gmail.com'
    miguel = 'mfdsantos86@gmail.com'
    KIW = 'team@knowitwall.com'
    angus = 'anguswaite@gmail.com'
    subject = 'Knowitwall contact form, message by: '+str(name)
    body = "Le feedack! Here's their info: \n \n--------------------------------------------------------\naudiodoc name: \n"+ str(ad_name)+"\n\n \nname: " + str(name) + "\nemail: " + str(email) + "\n\n \n feedback: \n" + str(feedback_overall) + "\n\n \n--------------------------------------------------------"
    yagmail.Connect('emailtoknowitwall', 'startupsarefun').send([jeremie, miguel, KIW, angus], subject, body)
    return name



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
