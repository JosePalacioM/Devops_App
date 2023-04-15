from flaskr import create_app
from flaskr.models import db
from flask_restful import Api
from flaskr.views import ViewCreateMail, ViewGetMail, ViewHealthCheck

application = create_app('default')
app_context = application.app_context()
app_context.push()

db.init_app(application)
db.create_all()

api = Api(application)

api.add_resource(ViewHealthCheck, '/healthcheck')
api.add_resource(ViewCreateMail, '/blacklists')
api.add_resource(ViewGetMail, '/blacklists/<string:blacklist_email>')

if __name__ == "__main__":
    application.run(port = 5000, debug = True)