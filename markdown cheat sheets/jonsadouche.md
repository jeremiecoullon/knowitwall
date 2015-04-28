

## Passing Variables:

I've put in some variables, like {{author\_name}}, and {{author\_bio}}. When the client requests the index page, the server returns index.html with these variables filled in. I've also included the variable {{audio}} in the first audio tag: the server passes to this variable the link to the .mp3 file at "https://jeremiestest.herokuapp.com/audio/science_ganymede.mp3". It does this because of the partial content thing that wasn't working before. When we put it up on your server, we'll replace this link (check out /json\_files/ganymede.json) with "static/audio/science\_ganymede.mp3" and it should work hopefully!

## stuff missing

- stylise the players (obvs). I put audio tags, so whats left is styling it like that link we liked.
- the smooth scroll isn't working for some reason. Also, I wasn't a huge fan of the scrolling speed (I dislike that way of scrolling that's very slow at first, then speeds up. it annoys me on other sites). anyways I'm guessing thats easy to change (I have a smooth scroll javascript thing in earlier commits).

## nav bar

The highlighting is cool (to tell you where you are!), but it spazes out a bit when you change, and sometimes highlights home when you're actually scrolled down.

## to do in Sublime:

###Indenting:

- Look at the bottom right of the editor, and click on 'Spaces: 4'.
- select: 'tab width: 2', and 'indenting using spaces'

This is because: Having only spaces (rather than a mix of spaces and tabs) is more consistent. To indent you can now either press TAB or type 2 spaces and it's the same thing. Also, 2 spaces is the default apparently (though sublime text gives 4 by default). I've had to convert from 2 to 4 when copying stuff from online and it's annoying so let's follow conventions :)

###Fold buttons:

These are the little triangles in sublime that allow you to minimise a section. I think they're not enabled by default. To enable them, go to "Sublime Text 2" (in the nav bar), "Preferences", and then "Settings-Default".

Go to "Fold buttons" (line 34) and set it to 'true'.

And if line numbers aren't enabled by default then set that to true as well :)

###Moar on indenting:

- **Indent properly**. ie: if you start a div at a certain position (namely, verticly aligned at a certain point), then end it at that exact same point. This is especially useful if you use the fold buttons.
- **Comments:** This is also valid for comments. Also, put a comment for a section *before* that section.
- **Nested tags:** When creating nested tags, put *one* indent only. Don't pull any of this shit:


```html
<div class="col-lg-12">
						<audio id="music" preload="true">
						<source src="http://www.alexkatz.me/codepen/music/interlude.mp3">
						<source src="http://www.alexkatz.me/codepen/music/interlude.ogg">
						</audio>
				<div id="audioplayer">
					<button id="pButton" class="play" onclick="play()"></button>
							  <div id="timeline">
									  <div id="playhead"></div>
							  </div>
				</div>

</div>
```

- Seriously, don't indent like a douchebag.

I