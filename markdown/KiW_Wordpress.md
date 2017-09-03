# Reproduce the Knowitwall site

_September 2017_

**Task: reproduce [Knowitwall](http://knowitwall.com/) on Wordpress**

### Requirements

- Make an exact replica of the current site on Wordpress. There are 4 types of pages:
    - homepage
    - archive page: under the 'all episodes' button
    - episode page: for each episode/article
    - About page
- The current site is written in Python (using Flask) and is on [Github](https://github.com/jeremiecoullon/knowitwall)
- The site should have the ability for some kind of “admin page”: namely team members at KiW (who don’t know or care about design and web development) should be able to add episodes easily.
- It should be possible to view a draft of an episode (and check that the images work on the episode page, the homepage and the archive page) before publishing it.
- It should be possible to change the order of episodes on the homepage. The archive page should have episodes ordered alphabetically
- As much stuff should be automated as possible. For example, the title of an article should only need to be written once, and it'll appear on the homepage, archive page, episode page, and metadata/opengraph info (for Facebook and twitter thumbnails)
- When the user (ie: admin) uploads a video, they should only have to post the youtube URL. The video is them displayed using youtube's 'embed' URL
- feedback form that sends an email to admin
- Flash Seminar (in the about page): it should be possible to add a new Flash Seminar episode
- The site should be responsive
- Classifications of episodes should be a tag that you can then use later. For example we could then have a filter than says "show all physics articles". It should be possible for an episode to have 2 or more tags.


### Some details

**An episode can have a video, audio, or text-only. This changes the design of several things:**

- Homepage and archive page: a small visual 'tag' appears at the bottom left of the box if the episode has a video or audio
- Meta info (Facebook and Twitter thumbnail): an `[audio]` or `[video]` tag appears if the episode has audio or video
- Episode page:
    - the nav bar has slightly different buttons depending if the episode is text-only, audio, or video
    - abstract is in italics if it's text-only.
    There's an audio player if it's audio & text.
    - If Video:
        - the main cover image has a different design and reveals the youtube video (that plays automatically) if you click on it.
        - The image credits of the main image (bottom left under the image) disappears when you play the video

**Other episode page quirks:**

- the images in the transcripts have 3 possible stylings: to the 'left', in the 'middle', or 'double' (the 'double' option is currently only use for the "Spanish Forger" episode).
- When you click on an image you zoom in (uses the 'fancybox.js' library)
- the audio player on mobile is circular (adapted code found online. The javascript code for this is [here](https://github.com/jeremiecoullon/knowitwall/blob/master/app/static/js/circular_player.js)).
- The cover image for homepage is the same as the one for the episode page. However the cropping isn't great for some of the images, so a separate image can be uploaded to go on the homepage.
- The Disqus comment section uses an id (currently chosen by hand): the comment section for the current episodes should stay the same (ie: we should still have the comments currently on the site!), but maybe new episodes could have an automatically generated ID
- Episode slugs (in the URL): the current ones are chosen manually (ex: `knowitwall.com/episodes/spanish_forger`). It might be easier if they were generated automatically. However the old URL should also work (so that you don't break links that are currently being shared on Facebook and Twitter)
- the author name and discipline (on the cover image) has the "by" and "in" either in white or black. This depends on the cover image, and admin should be able to change that for each episode.
- One of the author names is too long (Jonathan Butterworth, who wrote "Discovering the Higgs boson"), so the size of his name is slightly smaller (line `221` in [episode_page.html](https://github.com/jeremiecoullon/knowitwall/blob/master/app/templates/episode_page.html): `{{ audiodocs[0].name_font_size }}`). This should be a variable that admin can set (for example by default it's the normal size, and they can select to make it smaller if they want to)
- The episode ['emotional expression'](http://knowitwall.com/episodes/emotional_expression) has a gif in the transcript. This is set in some jquery at the bottom of [episode_page.html](https://github.com/jeremiecoullon/knowitwall/blob/master/app/templates/episode_page.html) (line `346` onwards). There's probably a better way of doing this though. Namely this be set by admin rather than hard-coded.
- The 'archive page' (the page with the list of all the episodes) has a filter button on mobile.
