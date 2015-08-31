# -*- coding: utf-8 -*-
import mimetypes
import re
import os
import yagmail
from flask import json, url_for, send_file, flash, redirect, session, g
from flask import render_template, request, send_from_directory, Response
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User
from oauth import OAuthSignIn

"""----------------------------------------------------------------------------------------------------
To change audio-doc:
1) change path to audio in 'sending files partially' section
2) change path to json file in the relevant audio-doc section
----------------------------------------------------------------------------------------------------"""


@app.before_request
def before_request():
    g.user = current_user

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
def static_from_root():
    return send_file_partial(request.path[1:])




"----------------------------------------------------------------------------------------------------"
"audiodoc function"

# complete list of audiodocs
all_audiodocs = ['antartica_discovery.json', 'stegosaurus.json', 'ganymede.json', 'tate.json']

# input list of json files, outputs list of dictionaries of variables paths & unicode to pass to templates
def ad_fun(audiodoc_list):
    audiodocs =[]
    for audiodoc_json in audiodoc_list:

        with open('app/static/json_files/' + audiodoc_json, "r") as json_file:
            ad_dictionary = json.load(json_file)

        with open(ad_dictionary.get('author_bio'), "r") as f:
            author_bio = f.read().decode('utf-8')
        ad_dictionary['author_bio'] = author_bio

        with open(ad_dictionary.get('transcript'), "r") as f:
            transcript = f.read().decode('utf-8')
        ad_dictionary['transcript'] = transcript

        audiodocs.append(ad_dictionary.copy())
    return audiodocs

""" Can do ad[author_name] or ad.get('author_name', DEFAULTVALUE)
    the second option is safer (if the key doesnt exist) """



@app.route('/')
def index():
    return render_template('index.html')


"VIEWS"
"----------------------------------------------------------------------------------------------------"
"home page"

@app.route('/home')
@login_required
def home():

    """
    To change audio-doc, simply create a new json file with the links to images,audio etc..
    Then add it to the audiodoc_list
    """
    audiodoc_list = all_audiodocs

    audiodocs = ad_fun(audiodoc_list)

    user = g.user

    return render_template('knowitwall.html', audiodocs=audiodocs, user = user)



"----------------------------------------------------------------------------------------------------"
" audiodocs on seperate page "

@app.route('/audiodoc/<url>')
def audiodoc(url):

    audiodoc_list = [url+'.json']  # list only has the selected audiodoc

    audiodoc = ad_fun(audiodoc_list)

    return render_template('audiodoc.html', audiodoc=audiodoc)


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
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()

# callback route: this is where facebook/twitter send auth info to KiW
@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous():
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, nickname=username, email=email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))

"----------------------------------------------------------------------------------------------------"
" secret login form "

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
