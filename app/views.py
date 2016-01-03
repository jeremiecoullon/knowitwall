# -*- coding: utf-8 -*-
import mimetypes
import re
import os
import yagmail
from flask import json, url_for, send_file
from flask import render_template, request, send_from_directory, Response
from app import app



"""----------------------------------------------------------------------------------------------------
To change audio-doc:
1) change path to audio in 'sending files partially' section
2) change path to json file in the relevant audio-doc section
----------------------------------------------------------------------------------------------------"""

@app.after_request
def after_request(response):
    response.headers.add('Accept-Ranges', 'bytes')
    return response

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
def static_from_root():
    return send_file_partial(request.path[1:])




"----------------------------------------------------------------------------------------------------"
"audiodoc function "

# complete list of audiodocs
all_audiodocs = ['higgs_boson.json', 'real_shakespeare.json', 'neural_cartography.json', 'saharan_dust.json', 'viral_pandemics.json', 'memory_bike.json', 'antartica_discovery.json', 'stegosaurus.json', 'ganymede.json', 'tate.json']

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



"----------------------------------------------------------------------------------------------------"
"home page"

@app.route('/')
def index():

    """
    To change audio-doc, simply create a new json file with the links to images,audio etc..
    Then add it to the audiodoc_list
    """
    audiodoc_list = all_audiodocs

    audiodocs = ad_fun(audiodoc_list)

    return render_template('knowitwall.html', audiodocs=audiodocs)



"----------------------------------------------------------------------------------------------------"
" audiodocs on seperate page "

@app.route('/audiodoc/<url>')
def audiodoc(url):

    audiodoc_list = [url+'.json']  # list only has the selected audiodoc

    audiodocs = ad_fun(audiodoc_list)

    return render_template('audiodoc.html', audiodocs=audiodocs)


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
