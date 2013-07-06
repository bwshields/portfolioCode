# -*- coding: utf-8 -*-
import cgi
import os
import webapp2

import jinja2
from jinja2 import Environment, PackageLoader
env = Environment(loader = PackageLoader('index', 'templates'))
template = env.get_template('base.html')
                               
class MainPage(webapp2.RequestHandler):
    def get(self):
      self.response.out.write(template.render())

app = webapp2.WSGIApplication(routes=[ 
    ( r'/', MainPage ),
], debug=True)
