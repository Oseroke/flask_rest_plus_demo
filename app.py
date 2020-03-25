import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask, Blueprint
import routes
#from routes import ns as task_namespace, api
#import routes.ns as task_namespace
from routes import api


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

def initialize_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(routes.ns)
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
    flask_app.config['RESTPLUS_VALIDATE'] = True
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = False
    flask_app.register_blueprint(blueprint)

def main():
    initialize_app(app)
    
    app.run(debug=True)

if __name__ == '__main__':
    main()
