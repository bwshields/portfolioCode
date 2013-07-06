import os
import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)
    
class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'name': 'SomeGuy',
            'verb': 'extremely enjoy'
        }

        template = jinja_env.get_template('index.html')
      self.response.out.write(template.render(template_values))
app = webapp2.WSGIApplication(routes=[ 
    ( r'/', MainPage ),
    # ... other paths ...
], debug=True)
