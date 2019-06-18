from flask import Flask
from flask_restful import Api, Resource

from .api.v1.views import RedFlags, RedFlag

def creeate_app():
   app = Flask(__name__)
   api = Api(app)
   api.add_resource(RedFlags, '/api/v1/red-flags')
   api.add_resource(RedFlag, '/api/v1/red-flags/<int:redflag_id>')
   return app

   if__name__ == '__main__':
   	app.run(debug=True)