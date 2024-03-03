from flask import Flask
from dotenv import dotenv_values
from .utils.helpers import response

ENV = dotenv_values()

def create_app():
  app = Flask(__name__)

  # CONFIGS
  app.config["APP_SECRET"] = ENV['APP_SECRET']


  #ROUTES
  from .routes import routes
  app.register_blueprint(routes)  
  

  # ERROR ROUTES
  app.errorhandler(404)
  def invalid_route(error):
    return response("Invalid route", None, False)
  
  app.errorhandler(Exception)
  def server_error(error):
    return response("Something went wrong, please try again", None, False)

  return app