from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy import fields

db = SQLAlchemy()

class MailBlacklist(db.Model):
    __tablename__ = 'MailBlacklist'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    app_uuid = db.Column(db.String(100), nullable = False)
    blocked_reason = db.Column(db.String(500), nullable = True)
    ip =  db.Column(db.String(100))
    created_at = db.Column(db.DateTime())

    def __repr__(self):
        return '<id: {}> - <email: {}> - <app_uuid: {}> - <blocked_reason: {}> - <ip: {}> - <created_at: {}>'.format(self.id, self.email, self.app_uuid, self.blocked_reason, self.ip, self.created_at)
    


class MailBlacklistSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = MailBlacklist
         include_relationships = True
         load_instance = True