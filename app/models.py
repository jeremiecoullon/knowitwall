from app import app, db
from app import UserMixin
from flask import json, render_template
import os.path
from config import AWS_URL

class Episode(object):
    """
    Class for all episodes

    Attributes
    ----------
    All attributes in json files containing episode info

    transcript :
        Reads and parses the transcript as html
    author_bio :
        Reads and parses the author_bio as html
    """
    def __init__(self, json_name):
        with open(os.path.join('app/json_files/', json_name), "r") as json_file:
            self.ad_dictionary = json.load(json_file)

        for key, val in self.ad_dictionary.iteritems():
            if key not in ['transcript', 'author_bio']:
                if key in ['topic_image', 'topic_image_box', 'author_image','topic_image_latest']:
                    setattr(self, key, AWS_URL+val)
                elif key in ['audio_mp3']:
                    audio_path = os.path.join(AWS_URL+'/static/audio', val.split('/')[-1])
                    setattr(self, key, audio_path)
                else:
                    setattr(self, key, val)

    @property
    def transcript(self):
        return render_template(self.ad_dictionary.get('transcript', 'no transcript found'))
        # return render_template('texts/real_shakespeare_transcript.html')
        # with open(self.ad_dictionary.get('transcript', 'no transcript found'), "r") as f:
        #     transcript_data = f.read().decode('utf-8')
        # return transcript_data

    @property
    def author_bio(self):
        return render_template(self.ad_dictionary.get('author_bio', 'no author bio found'))
        # with open(self.ad_dictionary.get('author_bio', 'no author bio found'), "r") as f:
        #     author_bio_data = f.read().decode('utf-8')
        # return author_bio_data


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)
