%Knowitwall - Coding

Here is a quick overview of how web pages are build. First I go over a static site (the code is in the `bootstrap_theme` folder) and then explain how to make a dynamic site (linking to a tutorial)

#Static site
_ie: front-end only_

##Bootstrap


- The `bootstrap_theme` folder has a nice template for a static site (we used one of these for Knowitwall!) taken from [here](http://startbootstrap.com/template-overviews/grayscale/)

The important bits to play around are:

- `index.html`: this is the html for the page (ie: the content). Open the file in your browser, and also open it in a text editor. Change stuff in the editor and refresh the browser to see the changes! #fun
- `css/grayscale.css`: this is the CSS file that has the styling unique to this page. Similarly, make changes to this in a text editor and see the changes in how the html is styled in the browser.
- `vendor/bootstrap/css/bootstrap.min.css`: this is a popular CSS library that has lots of built in functionality for CSS (including resizing stuff on mobile automatically which is practical!). It's good practice to not modify this and rather modify your own CSS file (in this case `grayscale.css`). If you want you can check out `bootstrap.css` (which is an [un-minified](https://en.wikipedia.org/wiki/Minification_(programming)) version of it) to see what's inside.

The other stuff is less important (some of which I don't really understand...)

##Servers

A quick refresher on servers:

1. A client (for example a browser) makes a request to a server for a file (ex: html & CSS)
2. The relevant server responds with the requested content and a code saying what happened (ex: 200: 'OK'; 404: 'page not found')

That's pretty much how the internet works :)

Moar details [here](http://computer.howstuffworks.com/web-server1.htm)

#Dynamic site

_ie: also includes a back-end_

**Problem:** what if you have lots of pages on your site that have a lot in common and with only a few bits changing ? For example the episode pages on Knowitwall are pretty much the same except for a few elements (title, images, audio, transcript...). It would be nice not to have to re-code an entire html page every time we add another episode!

**Solution:** Have a template html page for the episode page, and every time the client makes a request, the server builds the relevant page by inserting the relevant info for the requested episode.

To 'build' html in this way (and do other stuff) we need to code a backend for our site. To do this we need a framework (which handles details of http and other stuff). Moar info on what frameworks are and why we should use them are [here](http://stackoverflow.com/questions/18240052/what-is-the-purpose-of-a-web-framework) and [also here](https://jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/).


**TODO:**

The best way to understand a bit about how this works is to try it yourself! Here is a great tutorial that I used when starting on Knowitwall (and that I'll need to come back to again as there's loads of stuff in it that I don't understand yet): [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Just doing Part 1 and 2 is enough to understand how to use them (though feel free to go further if you want of course!)
