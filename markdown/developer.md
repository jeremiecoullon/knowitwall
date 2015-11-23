#Knowitwall

[Knowitwall site](http://knowitwall.com/)
****
**Summary of the project:**

Know it Wall is a website that spreads knowledge. It does this through content creation as well as content aggregation. On the content creation side of it, our community of academics write engaging texts in any subject – from physics to history – which we then turn into short documentaries (less than 10 minutes long). Each piece of content written by an academic works as a ​*pivot*​ around which something akin to a tree of knowledge emerges. So, after a pivot is published on the website in the form of text, audio and video, its author (the academic) adds in-line annotations to particular parts of the text (or audio or video – they all sync) with links to especially relevant and insightful articles, podcasts or videos in the wider Internet. We call these annotations ​*know-its*​ (after ‘post-its’). Once users have clicked on one of these know-its, the journey begins! They can themselves add know-its to articles, podcasts or videos that are hosted on third-party websites (and even to our pivots) in exactly the same way through Know it Wall's iframe  – linking content to more content. This is the content aggregation side of the project. When a decent number of know-its is added to third-party content, users will be able to take a bird’s eye view on all author- and user-generate know-its, a visual representation of everything on the website: the wall of all know-its – ​*the Know-it Wall*.
****

**tech stack:**

*the code is on [Github](https://github.com/jeremiecoullon/knowitwall)*

 - [Flask](http://flask.pocoo.org/) web framework 
 - [Digitalocean](https://www.digitalocean.com/) for hosting
 - [gunicorn](http://gunicorn.org/) and [nginx](https://www.nginx.com/resources/wiki/) web servers
 - sqlite for the user database



###Annotations (ie: Knowits)

*currently on the 'user\_login\_OAuth' branch on [github](https://github.com/jeremiecoullon/knowitwall)*

**annotations specs:**

- users log in, highlight a section of text, create a note with a character limit (say 200 characters)
- note must have a hyperlink to a 3rd party content (can use markdown for example to not have the URL)
- annotations must be approved by admin before being published
- When a user clicks on a hyperlink in an annotation, they are redirected to that article/site, but viewed in an iframe. 
- Users can repeat the whole process on this 3rd party content: create annotation and link to other 3rd party content.
- end up with a directed graph of related article/videos/podasts with the root articles being content produced by Knowitwall.

**Annotation library: [Annotator.js](http://annotatorjs.org/)**

- backend 
	- *storing the annotations:*
		- we're temporarily using this [backend store](http://annotateit.org/) for development: it stores the annotations, and sends to them to the client.
		- we're also currently setting up our own [store](https://github.com/openannotation/annotator-store) for annotations as we'll need to keep track of the link between annotated content send them back to the client (for the Wall of Knowledge).
	- *interaction with the client*
		- generates a token for the currently logged in user and exposes it to `knowitwall.com/token/`. The token has the annotator permissions for that user.
- frontend:
	- When a user is logged in, an OAuth token is exposed to `knowitwall.com/token/`
	- this token is used to set permissions for current user
	- if user isn't logged in, default is 'anonymous user' (has read-only permissions)


**User permissions needed**

- user not logged in (ie: 'anonymous user'):
	- can view annotations
	- cannot create/edit annotations
- user logged in:
	- can create annotations (need to be approved by admin before being published)
- admin logged in:
	- can edit/create/delete all annotations
	- has to approve user created annotations before they get published

###Wall of Knowledge: a graph of all Knowits

- each node is an article/video 
	- includes all Knowitwall content
	- includes any 3rd party content that has an annotation linking to it 
- The edges show which nodes are linked together by an annotation
	- maybe represent direction (ie: on which text was the annotation made)
- the nodes are clustered into disciplines (physics, history etc..)
	- these disciplines are either:
		- defined by users (via tags in the annotations) -  this will happen in a first step in any case
		- NLP: parse every received article page, find the article text, topic modelling. This wouldn't be possible for videos or podcasts though. This method might also be overkill, compare to the easier option of having users tag the discipline of the article. It would be pretty cool to have though.
- The wall gets updated as users add knowits

## Timeline

1. **Author annotations:**

	-  annotations given to us by the author of the audio-doc
	-  we put the annotation on the site:
		-  we login via a 'secret' login form (on `knowitwall.com/secretloginform/` for example)
		-  we have all permissions for creating annotations
		-  anonymous user (ie: users not logged in) have read-only permissions, and can't create 
	-  need to style how the annotations look
	-  need to set up the backend store as migrating from the AnnotateIt.com store to our store might be tedious
	- **problems:** annotator.js doesn't allow (out of the box) the 'anonymous' permissions that we need (ie: can view annotations without creating new ones): we need to go digging into the javascript to allow that.

2. **iframe:**

	- clicking on annotation hyperlink redirects to 3rd party via iframe

3. **user generated knowits:**

	- user login system (through facebook and twitter) is already set up (though not in production)
	- need to add the option of logging in with an email account
	- desing & code a login form page (or in the nav bar)
	- users can then login and create annotations on 3rd party content
	- **problems:** 
		- how can annotator.js annotate on content within iframes? Look into [this question](https://forum.jquery.com/topic/changing-elements-in-an-iframe): need to modify a `div` within the iframe
		- user generated annotations must be approved by 'admin'. How to do this?
		
4. **Wall of Knoweldge:**

	- visualise the graph well. Example of good design: [physics theories map](https://www.quantamagazine.org/20150803-physics-theories-map/)
	- backend store for annotations feeding the content into the visualisation
	- visualisation is continuously updated with new annotations? would need real-time communication; see the [socket.io integration](https://flask-socketio.readthedocs.org/en/latest/) for flask for example
	- how to set up the annotations (in the previous sections) such that the this is possible ? Should the database be set up in a specific way?

##developers:

**We have:**

- backend: python & databases
- designer/UX
- recently: javascript developer 


**We need:** 

more frontend/javascript developers: 

- deal with annotator.js: modify permission for anonymous, set up admin permissions etc..
- frontend stuff on the site: follow specs from designer 
- javascript (Visualisation): for the wall of knowledge

backend - Python: would be helpful as well! but the difficulty at the moment is mainly javascript 

*You don't have to commit to working on the entirety of the project; even helping out with a small aspect of it would be helpful! Generally, anyone keen to help build this is welcome!*

