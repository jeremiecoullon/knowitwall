#Knowitwall technical specifications

##Annotations (ie: Knowits)

**annotations specs:**

- users log in, highlight a section of text, create a note with a character limit (say 200 characters)
- note must have a hyperlink to a 3rd party content (can use markdown for example to not have the URL)
- annotations must be approved by admin before being published
- When a user clicks on a hyperlink in an annotation, they are redirected to that article/site, but viewed in an iframe. Users can repeat the whole process: create annotation and link to other 3rd party content.

**Annotation library: Annotator.js (link)**

- backend 
	- backend store **(link)**: 
		- stores the annotations
		- needs to keep track of the link between annotated content (for the Wall of Knowledge)
	- `views.py`: generates the token and exposes to knowitwall/token/??
- frontend:
	- When a user is logged in, an OAuth token is exposed to knowitwall.com/token/??**link**
	- token is used to set permissions for current user
	- if user isn't logged in, default is anonymous user



**User permissions**

- user not logged in:
	- can view annotations
	- cannot create/edit annotations
- user logged in:
	- can create annotations (need to be approved by admin before being published)
- admin logged in:
	- can edit/create/delete all annotations
	- has to approve user created annotations

##Wall of Knowledge: a graph of all Knowits

- each node is an article/video 
	- all Knowitwall content
	- any 3rd party content that has an annotation linking to it 
- Edges show nodes linked together with an annotation
	- maybe represent direction (ie: on which text was the annotation made)
- clustered into disciplines (physics, history etc..)
	- either:
		- defined by users (via tags in the annotations)
		- NLP: parse every received article page, find the article text, topic modelling. Wouldn't be possible for videos though.
- gets updated as users add knowits

## Steps

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
		- look into: need to modify a `div` within the iframe **(link)**
4. Wall of Knoweldge:

	- visualise the graph well (ex: **link to quanta magazine**)
	- backend store for annotations feeding the content into is

##developers:

have:

- backend: Flask, backend store for annotator.js
- designer/UX


**need:**

- frontend/javascript: 
	- deal with annotator.js: modify permission for anonymous, set up admin persmissions etc..
	- frontend stuff on the site: follow specs from designer 
- javascript (Visualisation): for the wall of knowledge