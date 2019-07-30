import webapp2
import jinja2
import os
import random


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/main.html')
        self.response.write(template.render())  # the response

class Restaurant(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/restaurant.html')
        types1 = ["American", "Barbecue", "Chinese", "French", "Hamburger", "Indian", "Italian", "Japanese", "Mexican", "Pizza", "Seafood", "Steak", "Sushi", "Thai"]
        restaurant_type = random.choice(types1)
        template_vars = {"type" : restaurant_type}
        self.response.write(template.render(template_vars))  # the response

class Entertainment(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/entertainment.html')
        types2 = ["Movies", "Music", "Performances", "Parks", "Museums", "Shopping Malls", "Game Rooms", "Sports"]
        entertainment_type = random.choice(types2)
        template_vars = {"type" : entertainment_type}
        self.response.write(template.render(template_vars))  # the response

class Locations(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/locations.html')
        self.response.write(template.render())  # the response

app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/restaurant', Restaurant),
    ('/entertainment', Entertainment),
    ('/locations', Locations)

], debug=True)
