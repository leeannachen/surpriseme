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

food_image_url = {
    "American" : "/static/pics/American.png",
    "Barbecue" : "/static/pics/Barbecue.png",
    "Chinese" : "/static/pics/Chinese.png",
    "French" : "/static/pics/French.png",
    "Hamburger" : "/static/pics/Hamburger.png",
    "Indian" : "/static/pics/Indian.png",
    "Italian" : "/static/pics/Italian.png",
    "Japanese" : "/static/pics/Japanese.png",
    "Mexican" : "/static/pics/Mexican.png",
    "Pizza" : "/static/pics/Pizza.png",
    "Seafood" : "/static/pics/Seafood.png",
    "Steak" : "/static/pics/Steak.png",
    "Sushi" : "/static/pics/Sushi.png",
    "Thai" : "/static/pics/Thai.png"
}
entertainment_image_url = {
    "Movies" : "/static/pics/movie.png",
    "Music" : "/static/pics/music.png",
    "Performances" : "/static/pics/performances.png",
    "Parks" : "/static/pics/parks.png",
    "Museums" : "/static/pics/museums.png",
    "Shopping Malls" : "/static/pics/mall.png",
    "Game Rooms" : "/static/pics/treasure-map.png",
    "Sports" : "/static/pics/sport.png"
}

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('main.html')
        self.response.write(template.render())  # the response

class Restaurant(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('restaurant.html')
        restaurant_type = self.request.get("type")
        if restaurant_type == "":
            restaurant_type = get_random_restaurant()
        template_vars = {"type" : restaurant_type,
                         "image_url" : food_image_url[restaurant_type],
                         "cost" : self.request.get("price"),
                         "vegetarian" : self.request.get("vegetarian"),
                         "vegan" : self.request.get("vegan"),
                         "halal" : self.request.get("halal"),
                         "kosher" : self.request.get("kosher")
                          }
        self.response.write(template.render(template_vars))  # the response

class Entertainment(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('entertainment.html')
        entertainment_type = get_random_entertainment()
        template_vars = {"type" : entertainment_type,
                         "image_url" : entertainment_image_url[entertainment_type],
                         }
        self.response.write(template.render(template_vars))  # the response



app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/restaurant', Restaurant),
    ('/entertainment', Entertainment),

], debug=True)
