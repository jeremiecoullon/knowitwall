#Knowitwall technical specifications

##Annotations (ie: Knowits)

**annotations specs:**

- users log in, highlight a section of text, create a note with a character limit (say 200 characters)
- note must have a hyperlink to a 3rd party content (can use markdown for example to not have the URL)
- annotations must be approved by admin before being published
- When a user clicks on a hyperlink in an annotation, they are redirected to that article/site, but viewed in an iframe. 
- Users can repeat the whole process on this 3rd party content: create annotation and link to other 3rd party content.
- end up with a directed graph of related article/videos/podasts with the root articles being content produced by Knowitwall.

**Annotation library: [Annotator.js](http://annotatorjs.org/)**

- backend 
	- [backend store](http://annotateit.org/): 
		- stores the annotations
		- needs to keep track of the link between annotated content (for the Wall of Knowledge). 
	- `views.py`: generates a token for the currently logged in user and exposes it to `knowitwall.com/token/`. The token has the annotator permissions for that user.
- frontend:
	- When a user is logged in, an OAuth token is exposed to `knowitwall.com/token/`
	- token is used to set permissions for current user
	- if user isn't logged in, default is 'anonymous user' (has read-only permissions)


**User permissions**

- user not logged in (ie: 'anonymous user'):
	- can view annotations
	- cannot create/edit annotations
- user logged in:
	- can create annotations (need to be approved by admin before being published)
- admin logged in:
	- can edit/create/delete all annotations
	- has to approve user created annotations

##Wall of Knowledge: a graph of all Knowits

- each node is an article/video 
	- includes all Knowitwall content
	- includes any 3rd party content that has an annotation linking to it 
- The edges show which nodes are linked together by an annotation
	- maybe represent direction (ie: on which text was the annotation made)
- the nodes are clustered into disciplines (physics, history etc..)
	- these disciplines are either:
		- defined by users (via tags in the annotations)
		- NLP: parse every received article page, find the article text, topic modelling. This wuldn't be possible for videos or podcasts though. This method might also be overkill, compare to the easier option of having users tag the discipline of the article.
- The wall gets updated as users add knowits

# To Do list

1. **Author annotations:**

	-  annotations given to us by the author of the audio-doc
	-  we put the annotation on the site:
		-  we login via a 'secret' login form (on `knowitwall.com/secretloginform/` for example)
		-  we have all permissions for creating annotations
		-  anonymous user (ie: users not logged in) have read-only permissions, and can't create 
	-  need to style how the annotations look
	-  need to set up the backend store as migrating from the AnnotateIt.com store to our store might be tedious
	- **problems:** annotator.js doesn't allow (out of the box) the 'anonymous' permissions that we need (ie: can view annotations without creating new ones): need to go digging into the javascript to allow that.

2. **iframe:**

	- clicking on annotation hyperlink redirects to 3rd party via iframe

3. **user generated knowits:**

	- make a nice login form page 
	- users can login and create annotations on 3rd party content
	- **problems:** how can annotator.js annotate on content within iframes? 
		- look into [this question](https://forum.jquery.com/topic/changing-elements-in-an-iframe): need to modify a `div` within the iframe
4. **Wall of Knoweldge:**

	- visualise the graph well; for example [this](https://www.quantamagazine.org/20150803-physics-theories-map/)
	- backend store for annotations feeding the content into is

##developers:

**We have:**

- backend: python (we use Flask) & databases
- designer/UX


**We need:**

- frontend/javascript: 
	- deal with annotator.js: modify permission for anonymous, set up admin persmissions etc..
	- frontend stuff on the site: follow specs from designer 
- javascript (Visualisation): for the wall of knowledge

##finding a developer

### Center for Digital Humanities:

These courses are relevant. Contact the lecturers: do they know students (Msc, PhD, other) who would be interested?

- [introduction to programming and scripting](http://www.ucl.ac.uk/dis/taught/pg/INSTG018)
- [internet technologies](http://www.ucl.ac.uk/dis/taught/pg/INSTG017)
- [server programming and structured data](http://www.ucl.ac.uk/dis/taught/pg/INSTG033)

### Amy Okuno

her, or people on her masters?

### UCL public engagement unit

- [contact list](https://www.ucl.ac.uk/public-engagement/contact) for public engagement unit

- contact the representative for [BEAM](http://www.ucl.ac.uk/research/beamsfunding):
Lizzy Baddeley: e.baddeley@ucl.ac.uk

###Ucl Advances
