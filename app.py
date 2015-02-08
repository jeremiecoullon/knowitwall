import os
from flask import Flask, json
from flask import render_template, send_from_directory

app = Flask(__name__, static_folder='static')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')


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

@app.route('/static/ganymede_transcript')
def send_file(ganymede_transcript):
    return send_from_directory(app.static_folder, ganymede_transcript.txt)


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

    """
    transcript_path=ad.transcript
    with open(transcript_path, "r") as f:
        transcript = f.read()
    """
    ganymede_transcript="/static/texts/ganymede_transcript.txt"



    bio_path=ad.author_bio
    with open(bio_path, "r") as f:
        author_bio = f.read()

    return render_template('audio_doc.jade', transcript=ganymede_transcript, author_image=ad.author_image, topic_image=ad.topic_image,
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
