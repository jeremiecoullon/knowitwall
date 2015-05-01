#!/usr/bin/env python
import yagmail

# send email to theknowitwall@gmail.com
yagmail.Connect('emailtoknowitwall', 'startupsarefun').send('theknowitwall@gmail.com', 'hello!', 'this is the body')
