#Server problems 

##issues and how to fix them

- 502 bad gateway: 
	- Try out **./run.py**: on 2nd May: lxml was not installed so run.py didn't work. This means that gunicorn app:app didn't work either
	- if ./run.py works, the problem may be with config files (check out [this](http://stackoverflow.com/questions/26211267/nginx-flask-gunicorn-502-error) stackoverflow question)
- To refresh the python script: `~/knowitwall$ killall -HUP gunicorn`
- If nginx config files were changed, you need to reload nginx: `~/knowitwall$ service nginx reload`

## to do

- set up access and error log files for server (gunicorn)

