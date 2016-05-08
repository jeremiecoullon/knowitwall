                                                                                                                                                              Knowitwall
==========

To get Knowitwall running locally:

- install packages in `requirements.txt`
- run `run.py`

Annotations
===========

##Current Annotator design:

Here is the current annotation design.

![annotation Design](annotation_design.png)

To reproduce this annotation, create an annotation and copy the html below into it. We'll first get annotations on the site in this way before allowing users to add them themselves (which will need a nice interface).

```html
<div class="entire_knowit">
<div class='knowit_author'>by KiW Team</div>
<div class='knowit'><div class='knowit_message'>There is actually an argument by philosopher Nick Bostrom from Oxford according to which it would be bad to find alien life in our Solar System:
 </div><a href="https://www.technologyreview.com/s/409936/where-are-they/" target='_blank' ><div class='knowit_link'><img src="http://goo.gl/OgZzbP" class='knowit_image'>
<p class='knowit_title'>Where are they?</p><p class='knowit_url'>TECHNOLOGYREVIEW.COM</p></div></a></div>
</div>
```

###TODO

- **Kappa logo (ie: knowit button):** For every annotation, place the small kappa logo at the end of the line (the 'knowit button'):
  - in the above screenshot the knowit button was put there manually (line 404 in `audiodoc_annotations.html`). However, the annotator library should put it there automatically. This should happen at the same time that it adds the yellow highlight to the text (which is `<span class='annotator-hl'>...</span> `)
- **Toggle:** add method that toggles the annotation as visible/not-visible
  - only one annotation open at once: for 2 annotations `A` and `B`, opening annotation `B` closes annotation `A` if `A` is already open
  - method toggles _only_ when you click on the yellow highlighted text _or_ on the knowit_button. Namely: clicking elsewhere on the page shouldn't open/close the annotation
  - annotation closes when you click on the 'close' cross on the top right hand corner of the annotation
  - currently: annotations opens and closes when you click on the yellow highlight, but there are bugs:
    - annotation closes randomly when you hover the mouse over it (but not all the time; there seem to be some weird conditions for this to happen)
    - when you click anywhere on the page (on the text for example), the annotation closes. You then need to click on the highlighted bit twice to open it again (once to 'close' it (as far as the toggle method is concerned) and once to open it again.)
    - `knowit_button` needs to also open/close it.
- **on mobile:**
  - Must have no 'knowit button'
  - The annotation (same design) appears above (or below) the highlighted bit of text
  - Open/close the annotation by clicking on the highlighted text. Close by clicking on the 'close' button (the black cross)

###Useful details about the annotator library

_in `app/static/js/annotator-full-1.2.7-modified.js`_

######Events:
_line 728_

define jQuery methods that go with certain CSS classes, and assign them to an Annotator method (`onAdderClick`, `onAdderMousedown`, etc..)

```javascript
Annotator.prototype.events = {

  ".annotator-adder button click": "onAdderClick",
  ".annotator-adder button mousedown": "onAdderMousedown",
  // modification: show annotation on click
  ".annotator-hl click": "toggleAnnotationViewer"
  // original methods: show annotation on hover
  // ".annotator-hl mouseover": "onHighlightMouseover",
  // ".annotator-hl mouseout": "startViewerHideTimer"
};
```

######add knowit button

_line 736_

add relevant html to the page, including the knowit button

```javascript
Annotator.prototype.html = {
  adder: '<div class="annotator-adder"><button>' + _t('Annotate') + '</button></div>',
  knowit_button: '<div class="knowit_button"><svg> (svg for button)</svg></div>',
  wrapper: '<div class="annotator-wrapper"></div>'
};
```

######my shitty toggle function

_line 1129_

I just reuse the same original methods (`onHighlightMouseover` and `startViewerHideTimer`). The latter has a delay (namely, the timer) to close the annotation (that I set to 0 seconds).

```javascript
// KIW modif: toggle opening and closing on click. kinda works but still buggy
Annotator.prototype.toggleAnnotationViewer = function(event) {
  if (this.toggleOn ===true){
    this.onHighlightMouseover(event);
    return this.toggleOn = false;
  }
  if (this.toggleOn ===false){
  this.startViewerHideTimer(event);
  return this.toggleOn = true;
  }
}
```

######position the knowit button

_line 1151_

Here I place the knowit button at the level on the highlighted text, but this is only happens when you open the annotation.

```javascript
// show the knowit_button at the level of the mouse posiiton
this.knowit_button.css({"top": Util.annotationPosition(event, this.wrapper[0]).top,"right": "700px"});
this.knowit_button.show();
```

###Set up Annotation library
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
