# Disqus

to add a new disqus comment thread, you must have 3 variables in the thread:

- disqus_identifier
- disqus_url	
- disqus_title


These are defined in the .json files for each audiodoc. the identifier is the *"unique_id"*, the url is *"knowitwall.com/unique\_id"*, and the *disqus\_title* is also the *'unique\_id'*

To start a new thread, you use the app.route commented out in app.py with the url *"localhost:5000/unique'_id"* and start a new thread with the desired variables. This will start an empty thread that you can place in any page you want. 
