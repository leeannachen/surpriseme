import webapp2
import jinja2
import os
import random

<<<<<<< HEAD

=======
>>>>>>> c9944e90386a9e9113d6b39e0bd908c4c22c43c3
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('main.html')
        self.response.write(template.render())  # the response

class Restaurant(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('restaurant.html')
        types1 = ["American", "Barbecue", "Chinese", "French", "Hamburger", "Indian", "Italian", "Japanese", "Mexican", "Pizza", "Seafood", "Steak", "Sushi", "Thai"]
        restaurant_type = random.choice(types1)
        template_vars = {"type" : restaurant_type}
        self.response.write(template.render(template_vars))  # the response

class Entertainment(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('entertainment.html')
        types2 = ["Movies", "Music", "Performances", "Parks", "Museums", "Shopping Malls", "Game Rooms", "Sports"]
        entertainment_type = random.choice(types2)
        template_vars = {"type" : entertainment_type}
        self.response.write(template.render(template_vars))  # the response

class Locations(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('locations.html')
        self.response.write(template.render())  # the response

app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/restaurant', Restaurant),
    ('/entertainment', Entertainment),
    ('/locations', Locations)

], debug=True)
