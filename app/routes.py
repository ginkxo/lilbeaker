from app import app

@app.route('/')
@app.route('/home')
def home():
    return "Test output!"

# this is how we do routing
# we use @ which are DECORATORS 
# @app.route('blahblah') and the following def function basically just means
# this REGISTERS THE SUBSEQUENT FUNCTION as a CALLBACK for the subsequent event
# .route does the following: in our app if we reach the blahblah.url/ or
# blahblah.url/home then it'll execute and return the home() located right after

