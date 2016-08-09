% Knowitwall coding

_The code is on [Github](https://github.com/jeremiecoullon/knowitwall)_


#To get Knowitwall running locally

_for Linux & Mac_

**Setup the environment:**

If you don't have virtualenv install it: `sudo pip install virtualenv` (check out this quick [tutorial](https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/) explaining why virtualenv is useful), then:

- create virtualenv: `virtualenv venv`
- Run `pip install -r requirements.txt`


**Note:** Activate/deactivate the virtual environment before and after use:

- To activate: `source venv/bin/activate`
- To deactivate: `deactivate`

**start server on localhost:** run `run.py`

#Structure of the codebase

We use [Flask](http://flask.pocoo.org/), which a web framework for Python. The point of web frameworks is to solve problems that are common to all web servers (and different frameworks do this in a different way). This [blog post](https://jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/) explains this nicely.

You can also check out this really nice [tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg on Flask (I used this when getting Knowitwall running). It goes through in detail how to get a blog working using Flask as the framework.

**Important stuff in the codebase:**

- the `app` directory has all the static content (images, audio, etc..) as well as the the code that builds the html and sends it to the client (the 'client' is a user's browser)
- `app/static`: directory with all the 'static' files. These are the files that are served to the client (images, javascript, CSS).
- `views.py`: This script has the functions that activates when someone goes to a certain URL on the site. Some important stuff in that script include:
    - Lines `162-173` is the function that deals with serving the home page (ie: "if a user goes to `knowitwall.com`, then return the html for the homepage")
    - Line `105`: the list of all the episodes. This is actually a list of json files, each of which have all the information for an episode
    - Lines `108-141`: function that takes the json file for an episode as input and gathers all the relevant info for that episode.
    - There are some other functions towards the bottom of the script that deal with users logging in (to be able to create the annotations!)
- `app/templates`: this has all the html templates. Notice that they have placeholders to put variables in them. Example in `knowitwall.html`, line `338`: `{{audiodocs[0].topic_name | safe}}`. This is where the the title of the most recent episode goes on the homepage. Notice how this is actually Python code that takes the first element of the list called `audiodocs` and gets from that element the attribute `topic_name`. The `safe` flag means that it's ok to parse the content (it may be HTML for example).
- `app/static/json_files`: this is where all the json files are. They have the paths to all the relevant info for an episode (for example the images, title, author name etc..).


#How we do Hosting & Deployment

- We use [DigitalOcean](https://en.wikipedia.org/wiki/DigitalOcean) for hosting; if you're a student you get $100 free credits for DigitalOcean. Yay!
- Git: I try to have rigorous-ish workflow (which I learnt from breaking stuff... :p). Some rules I have include:
    - The master branch on Github and on my laptop must always be in synch with the master branch on the server
    - If I want to merge a development branch `dev` to the master: first merge `master` to `dev`, fix the conflicts, then merge back to master.
    - Never merge anything on the server; only fast-forward.



#Upcoming milestones:

Here are some of the things that we're working on (in chronological-ish order):

1. Release the annotations by Friday 15th July:
    - an example is on this ['secret' URL](http://knowitwall.com/audiodoc_annotations/ganymede) (ie: it's not linked anywhere from the site)
    - we'd need at least one annotation for every episode.
2. Site redesign: homepage and archive page by Friday 29th July.
    - both are already designed
    - archive is coded up. We're trying it on another 'secret' URL [here](http://knowitwall.com/all_episodes) to see how it works on desktop & mobile . There is some more stuff to do on mobile though!
    - the homepage needs to be coded up: I have a potential new team member working on this. She's done html & CSS before, but is a beginning at coding/command line etc. so I don't know how long she'll take.
3. Design user-generated annotation. We're going to a weeklong 'training' thing in Birmingham early August. While there I'll design some of the following:
    - designing the user sign-in page. How will users interact with it, and how will the code respond to different user actions (ex: what if they forget their password ? etc...)
    - How do users create an annotation ? What error message appear if they don't do it right ?
    - How the wall of knowledge will look concretely (see the video for what this is!)

After this is done, there will lots of coding to do :). Some tools we'll need will be:

  - Javascript for the annotations (this may involve fancy front-end frameworks like Angular.js)
  - Python for the annotations backend
  - Python for the user login stuff (there already are some things on the site that do this, but we'll probably need some more)
  - html/css for the styling of the new login page and other stuff
  - Lots of coffee
4. Adding UCL, Imperial, and some other logos (groups that gave us funding) to the footer of every page.
5. Designing how videos will appear on each episode page & coding it up.

and more..


#Things to do:

If you're still interested in contributing to this, here are some things that need doing depending on what your interests are:

##Archive page on desktop

When one clicks on a title of an episode in the left hand column, the images on the right jump to the relevant one. This should happen smoothly rather than as a jump.

**Tools**:

- javascript
- using the html already written



##User tracking

We'll get out the annotation by the 22nd July (that's the plan at least...), but we need to find out quickly whether this whole annotation is actually a good idea. So this needs testing.

Let's define success as: 'users click on annotations'

We'll need to track how many people click on the annotations and compare it to the number of page views (on that page). We'll also need to wait until we have enough data for the result to be statistically significant. It might also be interesting to see which annotations perform best.

**Task:**

- get tracker on annotations. You can use [Optimizely](https://www.optimizely.com/) for example: they have a free service which is nice.
- Formalise beforehand (rigously) what 'success' is and compare to what actually happens #science
- Ideally track each annotation individually
- _Bonus:_ somehow automate this so that a tracker is automatically placed on an annotation as it's created

**Tools:**

- figuring out how to use Optimizely
- documenting stuff to explain the results to the me and rest of the team


##Hosting static files on Amazon S3

At the moment all the static files (images, audio etc..) are on the same server as the code (and are dealt with by Git/Github). This isn't great for several reasons:

1. Git doesn't like binary files: you can't do version control on them and it slows everything down! Example: cloning the knowitwall repo is really slow because it has loads of images.
2. When you scale a webapp, it's good to keep things separate. It's easier on your server if it only needs to build the html and send it to the client while another server deals with the images/audio etc. So we'll need to host the static stuff (except json files for obvious reasons!) on another server; I've been recommended Amazon S3. This [Stackoverflow Q&A](http://stackoverflow.com/questions/9441390/flask-static-folder-hosted-on-s3) explains a bit how this would work.

**Task**:

Some research on how to do this:

  - Find out how to use S3
  - What pricing (we have some funding for this)?
  - Are there any better options? (ex: DigitalOcean!)
  - How to migrate the files to S3
  - How will this integrate with version control
  - How to deploy everything in one go (writing scripts that automatically update the stuff in S3 when we update the site for example)

Then actually set it up:

- Start up the server
- Migrate the files
- Write scripts to automate everything
- Document how this is done (for new developers)

**Tools/skills:**

- server command line stuff (sysadmin) & devops skills
- python scripting to automate Deployment
- fun with Git

##Annotation Backend store

The annotations need a backend store on a separate server. When a user goes on a page that has annotations, their browser makes a request to:

1. the server that has the HTML/CSS for that page
2. the server that has the annotations on that page

The server that has the annotations replies with a json files: this contains all the info about an annotations (the annotation message itself, the time it was created, the user, the bit of text it's attached to, etc...).

Currently we're using the backend store run by the people who created the annotation library we're using: [Annotateit](http://annotateit.org/). This works fine by default.

However, we'll need to have more info in these annotations (namely a URL) and we'll need to use all this info when we do the wall of knowledge. So we'll need to host our own backend store on a server. Thankfully, Annotateit also open-sourced the code for the [backend store](https://github.com/openannotation/annotator-store)!

**Task:**

- get this backend store running running locally (and passing all the tests!). I made a bit of progress with this but got stuck..
- Get the backend store running on a server somewhere (maybe DigitalOcean to use those free credits!)
- Get the pages on knowitwall that have annotations to point to that server
- Document that shit
- When we move towards user-generated annotations: adding a field to the database for the URL in the annotation and add it to the API

**Tools:**

- Python, Flask
- Server sysadmin
- [command-line bullshittery](http://www.pgbovine.net/command-line-bullshittery.htm)


##CSS and design

### CSS preprocessing

Checkout CSS preprocessing languages (SASS, LESS) and implment.

**Task:**

- Understand how CSS work on knowitwall at the moment (ie: how is it organised?). Hint: it's organised pretty badly..
- Read up on good CSS practices: how should CSS/LESS and other fancy front-end tools be used as a website grows ? This could include:
    - when to add a new stylesheet?
    - How to name css classes properly ?
    - There are several different 'paradigms' for using CSS; we'd need to choose one and stick with it.
- Put this into practice on knowitwall
- Become a CSS pedant and annoy anyone who doesn't follow these good practices
- Document this in a clear, rigorous, and fun way! (yay for documentation). Maybe writing a short CSS style guide.

**Tools:**

- I dunno that what tools we'd need: that's what we need to find out!


### Google Material Design

Checkout [Google Material Design](https://material.google.com/). How to get the shadow stuff, and on elements. What CSS framework to use (that integrates with bootstrap)

### wireframing tools

Check out [these free tools](https://docs.google.com/document/d/1FigxN9uZL3fkWzOzts7WVco6zwEyNIT4hEsih9VQeWU/edit?pref=2&pli=1)
