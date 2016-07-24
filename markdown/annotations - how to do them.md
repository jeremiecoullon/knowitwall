#Annotations

**The important stuff is in this section; everything after that is details**

So at long last, the annotations/Know-its are (pretty much) ready. There are just some
more tweaks to do (namely, some final styling for mobile and possibly some bugs) but overall it's there.

In the first instance, we'll create Know-its ourselves and put them on the site (at least one for each episode). We can then show them to academics and ask them to write something (it's easier to explain to them what they are if we simply show them).

Let's aim to release them on the site by Friday 22nd (2 weeks before Jisc) so that we have time to get data on how well they're working before the sprint (namely: track whether people click on them). It's a bit ambitious but let's try to hit that!

The main thing to do now is to come up with annotations! There are more of us now on the team so everyone has to think of 2 and we have 1 per episode :).

If we all agree with this plan, let's maybe each create Know-its in our area of expertise. Of course, that could be (in my case) having a science Know-it on a humanities episode. But you think of a good one in another subject don't hold back ;)


**Now for the details**:

_Let's recall the requirements for an annotation:_

###Requirements for a Know-it

- A URL linking to an _article_ on another website with interesting content that's relevant to the highlighted section of the episode. At first let's just do articles (so text) and worry about other mediums later.
- A short message explaining why the article is interesting/relevant. This would have some character limit (ex: 200/300)
- At least one (or 2?) Know-its on each article so it's interesting, and that the text to the left doesn't look odd (for example [here](http://knowitwall.com/audiodoc_annotations/flying_spying); that being said it doesn't look that bad).
- An upper limit on the number of Know-its of an episode (or it'll end up looking like Genius!).
- For the moment, no overlapping Know-its (ie: 2 annotations on the same portion of text). I think it'll be possible later to figure out how to allow this in a way that works nicely, but for now let's keep it simple
- For the moment, the Know-its are only created by the author of the episode and ourselves.



###Process

To create an annotation, you log in (I'll allow Knowitwall's twitter account to create Know-its for example), highlight a section of text and insert the following HTML in the box:

```html
<div class="entire_knowit">
  <div class='knowit_author'>
    by KiW Team
  </div>
  <div class='knowit'>
    <div class='knowit_message'>
      There is actually an argument by philosopher Nick Bostrom from Oxford
      according to which it would be bad to find alien life in our Solar System:
    </div>
    <a href="https://www.technologyreview.com/s/409936/where-are-they/" target='_blank'>
      <div class='knowit_link'>
        <img src="http://goo.gl/OgZzbP" class='knowit_image'>
        <p class='knowit_title'>
          Where are they?
        </p>
        <p class='knowit_url'>
          TECHNOLOGYREVIEW.COM
        </p>
      </div>
    </a>
  </div>
</div>
```

It should be pretty self-explanatory what everything does. Each elem within the triangular brackets `< >` is called a tag. A tag states how the text within should look.

Just type in the correct Know-it message (replacing the current one), replace the correct link to the article in the `<a>` tag, and replace the correct the link to the thumbnail image in the `<img>` tag. I explain way at the bottom of the document how to get the thumbnail image. If you're scared of code, I can do it of course :p (but it's really not hard, and this means that you can edit/create a Know-it yourself rather than ask me). Also, note that I actually didn't use the `og:image` in this Bostrom example, as it was a really bad resolution..

If the academic created the Know-it, then replace 'by KiW Team' by the academic's name.

###Contacting academics

####Previous academics
We would like academics to suggest Know-its. So we should contact all those who've already written a text, explain what they are,  show an example, and ask for them to suggest some.

####Current/future academics

We could add Know-its to the guidelines/requirements (in the same was as we ask them to suggest an image to add to their text), but we should probably do this in the middle/end of the process of creating an episode, as it might feel overwhelming if we ask everything at once (though maybe in some cases it wouldn't be). In any case we can play this by ear (namely: do we think the academic will get the idea quickly or not).



###How to get the thumnail image

The thumbnail image is the image that gets shown when you post a link to a website (for example on Facebook). To get the URL to this image you do the following steps:

####1.
 Go on the site you want the thumbnail image of.

####2.
 Right-click anywhere on the page, and choose 'view page source' (Figure 1)

![View page source](view_page_source.png)

####3.
Find the `<meta>` tag at the top of the page that is called `property="og:image"`. This corresponds to the thumbnail that Facebook uses. `og` stands for 'Open Graph' which is a set of tools/protocols that allows webpages to be part of a network (and it's run by Facebook) (see Figure 2)

![Knowitwall source code](KiW_source_code.png)

####4.
You then get the thumnbail image! It's a valid URL so you can view it in the browser. Simply copy the url in the annotation at the correct location (namely in the `img` tag))  (Figure 3).

![Ganymede thumbnail](ganymede_thumbnail.png)


When users will be creating their own Know-its, this whole process will obviously happen automatically. When you try this out, you'll see that not all site have this `og:image` (and actually some sites make it difficult to automate this kind of stuff). So it should a fun challenge!
