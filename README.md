 Knowitwall
==========

To get Knowitwall running locally:

- install packages in `requirements.txt`
- run `run.py`

If on the **`user_login_OAuth` branch:**

*The annotation library: [Annotator.js](http://annotatorjs.org/)*

- to get the annotations working with this [backend store](http://annotateit.org/):
  - make sure that `annotator-full-1.2.7-modified.js` is pointing to the that backend store. Namely, modify line 3019:

  ```javascript
  prefix: config.storeUrl || 'http://annotateit.org/api',
  ```
  - log in via Facebook or twitter at `http://localhost:5000/supersecretlogin`
  - add your account to admin group in `views.py`:

  ```python
  create_permission = ['jeremie.coullon']
  ```

###Annotator design:

- The first step is to get a simple design and play with to see how it is (in terms of usability) and what needs to be done next.

**Simple design:**

<img src="knowitwall_annotation_1.png"  style="width:700px; margin-left:10%; margin-right:10%" ></img>




**Stuff to do:**
- <del>have the vertical yellow line like in the image above</del>
- display the URL to the 3rd party content nicely (dunno how this should look...)
- get the image for the article (like the thumbnail when you post articles on facebook) and display it above the text (like in the image above).
- <del>have the adder (the square that appears when you highlight text) appear next to the mouse.</del>
- <del>be able to click on the highlighted section of text and have the annotation stay visible. Click again to hide it.</del>
- <del>when creating an annotations we need to display 2 boxes. This needs to be setup in the backend store though..</del>
  - <del>one box for the text (with a character limit, say 200)</del>
  - <del>one box for the URL to the 3rd party content</del>
- **Displaying URLs:** copy any hyperlink into the message, and the entire annotation become clickable


###Annotator frontend

- when a user creates an annotation, `annotator-full-1.2.7-modified.js` creates the html tags with the annotator classes (as an unordered list) and positions them relative to where the annotation was created.
- the position of the adder and the annotation is determined in the `div` with classes `annotator-outer annotator-viewer annotator-invert-x annotator-hide`. These classes are defined in `annotator-KIW.css`.
