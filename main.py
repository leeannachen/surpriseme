import webapp2
import jinja2
import os
import random

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def Restaurant():
    types1 = ["American", "Barbecue", "Chinese", "French", "Hamburger", "Indian", "Italian", "Japanese", "Mexican", "Pizza", "Seafood", "Steak", "Sushi", "Thai"]
    restaurant_type = random.choice(types1)
    return restaurant_type

def Location():
    types2 = ["Movies", "Music", "Performances", "Parks", "Museums", "Shopping Malls", "Game Rooms", "Sports"]
    entertainment_type = random.choice(types2)
    template_vars = {"type" : entertainment_type}
    return entertainment_type

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('main.html')
        self.response.write(template.render())  # the response

class Result(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('result.html')

# class Restaurant(webapp2.RequestHandler):
#     def get(self):
#         template = the_jinja_env.get_template('restaurant.html')
#         template_vars = {"type" : restaurant_type}
#         self.response.write(template.render(template_vars))  # the response
#
# class Entertainment(webapp2.RequestHandler):
#     def get(self):
#         template = the_jinja_env.get_template('entertainment.html')
#         self.response.write(template.render(template_vars))  # the response
#

app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/restaurant', Restaurant),
    ('/entertainment', Entertainment),

], debug=True)
