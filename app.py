import os
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route('/')
@app.route('/index/')
def index():
    """
    This method is a controller. a method is function with side-effects. python just has methods.
    """
    return render_template('index.jade')

@app.route('/about/')
def about():
    return render_template('about.jade')

""" for academic contributors"""
@app.route('/contribute/')
def contribute():
    return render_template('contribute.jade')

""" contact information """
@app.route('/contact/')
def contact():
    return render_template('contact.jade')

""" audio-doc 1 (science)"""
@app.route('/ad1/')
def ad1():
    print "@@@@@@@@@"
    with open("static/texts/science_ganymede.txt", "r") as f:
        transcript = f.read()
    return render_template('ad1.jade', transcript=transcript)

""" audio-doc 2 (humanities) """
@app.route('/ad2/')
def ad2():
    return render_template('ad2.jade')

'''@app.route('/test/')
def test():
        return render_template('test')
    '''
""" comment box for user feedback"""
@app.route('/comment/', methods=['POST'])
def comment():
    print("@@@@@@@@@@@@@@@@@@")
    print(request.form)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
