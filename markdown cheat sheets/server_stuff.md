#Server problems 

##issues and how to fix them

- tutorial on launching flask on digitalocean [here](http://blog.marksteve.com/deploy-a-flask-application-inside-a-digitalocean-droplet)
- to launch gunicorn: `~/knowitwall$ gunicorn app:app`
- 502 bad gateway: 
	- Try out **./run.py**: on 2nd May: lxml was not installed so run.py didn't work. This means that gunicorn app:app didn't work either
	- if ./run.py works, the problem may be with config files (check out [this](http://stackoverflow.com/questions/26211267/nginx-flask-gunicorn-502-error) stackoverflow question)
- To refresh the python script: `~/knowitwall$ killall -HUP gunicorn`. Without this, python variables/scripts will not be updated.
- If nginx config files were changed, you need to reload nginx: `~/knowitwall$ service nginx reload`

## things to do

- set up access and error log files for server (gunicorn)

##good practices

- **never** merge things on the server. 
- **never** modfiy files on the server.
- get the master branch on github to how you want it, and fast-forwards the server branch (pull origin/master to server)
- can put a different test branch from origin to server to try it out (so you can switch from the master to the test branch in the server)