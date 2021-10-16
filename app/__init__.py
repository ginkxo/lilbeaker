from flask import Flask

# the entry point
app = Flask(__name__)

# creates an instance of the Flask() object as "app"
# __name__ variable is predefined by Python, name of module in which its used

from app import routes
