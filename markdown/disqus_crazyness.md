# Disqus

to add a new disqus comment thread, you must have 3 variables in the thread:

- disqus_identifier
- disqus_url	
- disqus_title


These are defined in the .json files for each audiodoc. For the comment thread of each audio-doc, we set the identifier as the *"unique_id"*, the url as *"knowitwall.com/unique\_id"*, and the *disqus\_title* as the *'unique\_id'*

To initalise a new thread: use the `@app.route` (which is commented out) in app.py with the url *"localhost:5000/unique_id"* and start a new thread with the desired variables. This will start an empty thread (within localhost) that you can then place in any page you want. 
