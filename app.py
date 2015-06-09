# -*- coding: utf-8 -*-
import mimetypes
import re
import os
import yagmail
from flask import Flask, json, url_for, send_file
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
@app.route('/audio/could_there_be_life_around_Jupiter.mp3')
def static_from_root():
    return send_file_partial(request.path[1:])




"----------------------------------------------------------------------------------------------------"
"home page"

@app.route('/')
def index():


    """
    To change audio-doc, simply create a new json file with the links to images,audio etc..
    Then add it to the audiodoc_list
    """
    audiodoc_list = ['tate.json']
    audiodocs =[]
    for audiodoc_json in audiodoc_list:

        with open('json_files/' + audiodoc_json, "r") as json_file:
            ad_dictionary = json.load(json_file)

        with open(ad_dictionary.get('author_bio'), "r") as f:
            author_bio = f.read().decode('utf-8')
        ad_dictionary['author_bio'] = author_bio

        with open(ad_dictionary.get('transcript'), "r") as f:
            transcript = f.read().decode('utf-8')
        ad_dictionary['transcript'] = transcript

        audiodocs.append(ad_dictionary.copy())

    return render_template('knowitwall.html', audiodocs=audiodocs)

""" I can just do ad[author_name] or ad.get('author_namr', DEFAULTVALUE) rather
than define the Struct class. the second option is safer (if the key doesnt exist) """





"----------------------------------------------------------------------------------------------------"
"testing the 2 audiodoc styling "



@app.route('/testingz')
def testings():


    """
    To change audio-doc, simply create a new json file with the links to images,audio etc..
    Then add it to the audiodoc_list
    """
    audiodoc_list = ['ganymede.json', 'tate.json']
    audiodocs =[]
    for audiodoc_json in audiodoc_list:

        with open('json_files/' + audiodoc_json, "r") as json_file:
            ad_dictionary = json.load(json_file)

        with open(ad_dictionary.get('author_bio'), "r") as f:
            author_bio = f.read().decode('utf-8')
        ad_dictionary['author_bio'] = author_bio

        with open(ad_dictionary.get('transcript'), "r") as f:
            transcript = f.read().decode('utf-8')
        ad_dictionary['transcript'] = transcript

        audiodocs.append(ad_dictionary.copy())

    return render_template('test_2audiodocs.html', audiodocs=audiodocs)


"----------------------------------------------------------------------------------------------------"
"method for AJAX contact form "

@app.route('/contactform', methods=['POST'])
def contactform():
    name =  request.form['name'];
    email = request.form['email'];
    message = request.form['message'];
    jeremie ='jeremie.coullon@gmail.com'
    miguel = 'mfdsantos86@gmail.com'
    KIW = 'theknowitwall@gmail.com'
    angus = 'anguswaite@gmail.com'
    subject = 'Knowitwall contact form, message by: '+str(name)
    body = "Someone loves us! Here's their info: \n \n--------------------------------------------------------\nname: " + str(name)+ "\nemail: " + str(email) + "\nmessage: \n\n" + str(message) + "\n--------------------------------------------------------"
    yagmail.Connect('emailtoknowitwall', 'startupsarefun').send([jeremie, miguel, angus, KIW], subject, body)
    return name


@app.route('/test')
def test():
    d_identifier = 'test_disqus'
    d_url = 'http://localhost:5000/test'
    return render_template('test.html', d_identifier=d_identifier, d_url=d_url)



@app.route('/test2')
def test2():
    return render_template('test2.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
