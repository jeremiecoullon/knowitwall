# -*- coding: utf-8 -*-
import mimetypes
import re
import os
import yagmail
from flask import Flask, json, url_for
from flask import render_template, request, send_from_directory, Response

app = Flask(__name__, static_folder='static')



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

    new_path=os.path.join('static/',path)

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
@app.route('/audio/its_at_tate.ogg')
@app.route('/audio/its_at_tate.wav')
@app.route('/audio/science_ganymede.mp3')
def static_from_root():
    return send_file_partial(request.path[1:])




"----------------------------------------------------------------------------------------------------"
"home page"

@app.route('/')
def index():


    """
    To change audio-doc, simply create a new json file with the links to images,audio etc..
    Then replace the following path with the path to the new json file
    """
    with open('json_files/tate.json') as json_file:
        ad = json.load(json_file)

    transcript_path=ad.get('transcript')
    with open(transcript_path, "r") as f:
        transcript = f.read()

    bio_path=ad.get('author_bio')
    with open(bio_path, "r") as f:
        author_bio = f.read()

    return render_template('knowitwall.html', transcript=transcript, author_image=ad.get('author_image'),
        topic_image=ad.get('topic_image'), author_bio=author_bio, author_name=ad.get('author_name'),
        audio_mp3=ad.get('audio_mp3'), audio_wav=ad.get('audio_wav'), audio_ogg=ad.get('audio_ogg'),
        discipline=ad.get('discipline'), topic_name=ad.get('topic_name'),
        topic_description=ad.get('topic_description'))

""" I can just do ad[author_name] or ad.get('author_namr', DEFAULTVALUE) rather
than define the Struct class. the second option is safer (if the key doesnt exist) """




"----------------------------------------------------------------------------------------------------"
"method for AJAX contact form "

@app.route('/contactform', methods=['POST'])
def contactform():
    name =  request.form['name'];
    email = request.form['email'];
    message = request.form['message'];
    print name, email, message
    yagmail.Connect('emailtoknowitwall', 'startupsarefun').send('theknowitwall@gmail.com',
        'Knowitwall contact form, message by: '+str(name), """Someone loves us! Here's their info: \n \n--------------------------------------------------------\nname: """ + str(name)
        + "\nemail: " + str(email) + "\nmessage: \n\n" + str(message) + "--------------------------------------------------------")
    return name






if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
