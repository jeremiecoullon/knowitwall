
import re
import mimetypes
from flask import Flask, json
from flask import render_template, request, send_from_directory, Response

app = Flask(__name__, static_folder='static')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')


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

@app.route('/audio/humanities_tate.mp3')
@app.route('/audio/science_ganymede.mp3')
def static_from_root():
    return send_file_partial(request.path[1:])


@app.route('/help/')
def help():
    return render_template('help.html')




"----------------------------------------------------------------------------------------------------"
"index page"


@app.route('/')
@app.route('/index/')
def index():
    """
    This method is a controller. a method is function with side-effects. python just has methods.
    """
    return render_template('/index/index.html')



"----------------------------------------------------------------------------------------------------"
"science page"

@app.route('/science/')
def ad1():

    class Struct(dict):
        def __getattr__(self, name):
            return self[name]

        def __setattr__(self, name, value):
            self[name] = value

        def __delattr__(self, name):
            del self[name]

    """
    To change audio-doc, simply create a new json file with the links to images,audio etc..
    Then replace the following path with the path to the new json file
    """
    with open('json_files/ganymede.json') as json_file:
        ad = json.load(json_file, object_hook=Struct)

    transcript_path=ad.transcript
    with open(transcript_path, "r") as f:
        transcript = f.read()

    bio_path=ad.author_bio
    with open(bio_path, "r") as f:
        author_bio = f.read()

    return render_template('audio_doc.jade', transcript=transcript, author_image=ad.author_image, topic_image=ad.topic_image,
        author_bio=author_bio, author_name=ad.author_name, audio=ad.audio, discipline=ad.discipline, form=ad.form)



"----------------------------------------------------------------------------------------------------"
"humanities page"



@app.route('/humanities/')
def ad2():

    class Struct(dict):
        def __getattr__(self, name):
            return self[name]

        def __setattr__(self, name, value):
            self[name] = value

        def __delattr__(self, name):
            del self[name]

    """
    To change audio-doc, simply create a new json file with the links to images,audio etc..
    Then replace the following path with the path to the new json file
    """
    with open('json_files/tate.json') as json_file:
        ad = json.load(json_file, object_hook=Struct)
    bio_path=ad.author_bio

    with open(bio_path, "r") as f:
        author_bio = f.read()

    transcript_path=ad.transcript
    with open(transcript_path, "r") as f:
        transcript = f.read()

    return render_template('audio_doc.jade', transcript=transcript, author_image=ad.author_image, topic_image=ad.topic_image,
        author_bio=author_bio, author_name=ad.author_name, audio=ad.audio, discipline=ad.discipline, form=ad.form)






if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
