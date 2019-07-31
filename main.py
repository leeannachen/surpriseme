import webapp2
import jinja2
import os
import random

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def get_random_restaurant():
    types1 = ["American", "Barbecue", "Chinese", "French", "Hamburger", "Indian", "Italian", "Japanese", "Mexican", "Pizza", "Seafood", "Steak", "Sushi", "Thai"]
    restaurant_type = random.choice(types1)
    return restaurant_type

def get_random_entertainment():
    types2 = ["Movies", "Music", "Performances", "Parks", "Museums", "Shopping Malls", "Game Rooms", "Sports"]
    entertainment_type = random.choice(types2)
    return entertainment_type

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('main.html')
        self.response.write(template.render())  # the response

class Restaurant(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('restaurant.html')
        restaurant_type = get_random_restaurant()
        template_vars = {"type" : restaurant_type}
        self.response.write(template.render(template_vars))  # the response

class Entertainment(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('entertainment.html')
        entertainment_type = get_random_entertainment()
        template_vars = {"type" : entertainment_type}
        self.response.write(template.render(template_vars))  # the response


app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/restaurant', Restaurant),
    ('/entertainment', Entertainment),

], debug=True)
