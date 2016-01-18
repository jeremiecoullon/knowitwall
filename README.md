Knowitwall
==========

To get Knowitwall running locally:

- install packages in `requirements.txt`
- run `run.py`

If on the **`user_login_OAuth` branch:**

*The annotation library: [Annotator.js](http://annotatorjs.org/)*

- to get the annotations working with this [backend store](http://annotateit.org/):
  - make sure that `annotator-full-1.2.7.modified.js` is pointing to the that backend store. Namely, modify line 3019:

  ```javascript
  prefix: config.storeUrl || 'http://annotateit.org/api',
  ```
  - log in via Facebook or twitter at `http://localhost:5000/supersecretlogin`
  - add your account to admin group in `views.py`:

  ```python
  create_permission = ['jeremie.coullon']
  ```
