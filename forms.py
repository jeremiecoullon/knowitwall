from wtforms import Form, TextField, SubmitField, validators, TextAreaField


class ContactForm(Form):
  name = TextField("Name",  [validators.Required()])
  email = TextField("Email",  [validators.Required(), validators.Email()])
  subject = TextField("Subject",  [validators.Required()])
  message = TextAreaField("Message",  [validators.Required()])
  submit = SubmitField("Send")
