from flaskr import create_app
from .models import db, MailBlacklist, MailBlacklistSchema
from datetime import datetime
from flask_restful import Api
from .views import ViewCreateMail, ViewGetMail



app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(ViewCreateMail, '/blacklists')
api.add_resource(ViewGetMail, '/blacklists/<string:blacklist_email>')


# #Test
# datet = datetime(1961, 4, 12, 6, 8)
# with app.app_context():
#     t = MailBlacklist(id = 2,email = 'alex2@gmail.com',app_uuid = '2',blocked_reason = 'Bad reason',ip =  '10.125.25.15',created_at = datet)
#     db.session.add(t)
#     db.session.commit()
#     print(MailBlacklist.query.all())
