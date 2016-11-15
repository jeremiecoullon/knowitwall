Knowitwall
==========
Know it Wall (KiW) is a newly founded public engagement website, based at UCL, that aims to popularise research across all disciplines from arts to sciences.
KiW takes 1,000-word scripts that academics write on research worth sharing with the wider public and turns these into short audio-documentaries (less than 10 minutes long). Once produced, both audio-documentaries and scripts are published on KiW’s website – [knowitwall.com](http://knowitwall.com/) – as well as on iTunes, Soundcloud and Medium.

The overarching aim is use these documentaries as a starting point for interactive storytelling.

# Contributing


To get Knowitwall running locally:

- install packages in `requirements.txt`
- run `run.py`


Drop me an email at jeremie.coullon@gmail.com if you're interested in contributing. Most of the stuff to do (in the list below) have a design component which needs to be discussed before coding !

# Development milestones

## Content management stuff

- team & 'about' page: we need an entire page for this - design & code up
- [all episodes](http://knowitwall.com/all_episodes): need a button that filters episodes by discipline (like on mobile). However the blocks need to re-arrange themselves to still be in the current pattern after the clicking on the filter. Having this happen client side might be the best solution (Ajax and [nunjucks](https://mozilla.github.io/nunjucks/) sounds good). 
- [Episode pages](http://knowitwall.com/episodes/spanish_forger): need to design and code an audioplayer like Soundcloud. Namely, a player that is in a sticky footer and that keeps playing as you navigate to different pages within the site.

## Annotations

#### What are they ?

**The first step is to allow users to annotate on our texts**

There are 2 requirements for each annotations (an example [here](http://knowitwall.com/audiodoc_annotations/ganymede)):
- they must have a URL linking to a article on the internet that's relevant to the annotated bit of text.
- they must have a short description of the article/why it's relevant

The whole point is that they correspond to the reaction: "the article I'm reading reminds me of this other article I read last week - here's a hyperlink to it."

_So essentially annotations are hyperlinks created by users (and the academic who wrote the episode)_


**The second step is to allow users to annotate on 3rd party content**


- This will be done using a browser extension: if you click on the extension you can see the various annotations that are on the page you're visiting. (like [Hypothes.is](http://hypothes.is/))
- You can also create more annotations in exactly the same way as in the first step. As before, an annotation on 3rd party content must have a URL linking to a relevant article on the internet & a short description of the article
- As all the annotations much have a URL to a relevant article on the web, a network is created (specifically a [connected graph](http://mathworld.wolfram.com/ConnectedGraph.html))
- When a sufficient number of annotations have been created, we can visualise this network and see the links between the various articles/disciplines.
- An example of a cool visualision that corresponds to what we're aiming for is [here](https://www.quantamagazine.org/20150803-physics-theories-map/). For Knowitwall, the different sections will correspond to disciplines, and each node corresponds to an annotated article

#### Milestones to hit

1. Annotations written by the academics & KiW (an example [here](http://knowitwall.com/audiodoc_annotations/ganymede)). There are some stuff to finish:
    - responsive: for certain screen sizes (ipad-ish) the vertical yellow bar covers the text
    - the small 'kappa' at the end of the annotated line should rather be a speech bubble which shows there's a comment (some user testing suggested that the point of the kappa wasn't obvious)
    - need to get annotations for each episode
2. User generated annotations:
    - design & code up the login page
    - design the UI for creating an annotation; have 1 box for the ULR and 1 box for the message
    - set up the [backend store](https://github.com/openannotation/annotator-store) and modify: it needs to take an extra input from the annotation (the URL as well as the message)
3. Browser extension: Set up the browser extension with a similar design for the annotations as before (code is also on [Hypothes.is's Github](https://github.com/hypothesis/browser-extension))
4. Visualisation: Design and code the visualisation of all the annotations on the site and on 3rd party content

### Tech

[AnnotateIt](http://annotateit.org/) [Hypothes.is](https://hypothes.is/) are 2 projects to annotate the web (that share features and contributors). We used the softwware by AnnotateIt for our annotations at our [test page](http://knowitwall.com/audiodoc_annotations/ganymede). They open source most of their code and encourage developers to use it for their projects.
