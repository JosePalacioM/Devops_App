from flask_restful import Resource
from ..models import db, MailBlacklist, MailBlacklistSchema
from flask import request
from datetime import datetime
import requests
from .helper import Helper

mailblacklist_schema = MailBlacklistSchema()

KeyWord = "KeyWord"
helper = Helper()


class ViewCreateMail(Resource):

    def post(self):
        try:
            token = request.headers.get('Authorization', None)[7:]
            if token == KeyWord:

                try:
                    exist_email = MailBlacklist.query.filter(
                        MailBlacklist.email == request.json["email"]).first()
                    if (exist_email):
                        return {'mensaje': 'Error ocurrido: El email ya está registrado, si es necesario introduzca otro email.'}, 412

                    if len(request.json['app_uuid'].strip()) == 0:
                        return {'mensaje': 'El app_uuid (id de la app cliente) no puede estar vacío'}, 400

                    blacklist = MailBlacklist(
                        email=request.json["email"],
                        app_uuid=request.json["app_uuid"],
                        blocked_reason=request.json["blocked_reason"],
                        ip=helper.get_client_ip(),
                        created_at=datetime.now()
                    )

                    db.session.add(blacklist)
                    db.session.commit()
                    db.session.refresh(blacklist)

                    return {'mensaje': 'La cuenta ha sido creada', 'cuenta': mailblacklist_schema.dump(blacklist)}, 200

                except Exception as err:
                    return {'mensaje': 'Ha ocurrido un error', 'error': str(err)}, 400

            else:
                return {'mensaje': 'Por favor ingresar un token válido'}, 401

        except Exception as e:
            return {'mensaje': 'Por favor ingresar un token', 'error': str(e)}, 401


class ViewGetMail(Resource):

    def get(self, blacklist_email):
        token = request.headers.get('Authorization', None)[7:]
        if token == KeyWord:
            try:
                query = MailBlacklist.query.filter(
                    MailBlacklist.email == blacklist_email).first()

                if query == None:
                    return {'mensaje': 'No existe ese correo en la lista negra'}, 404
                return [mailblacklist_schema.dump(query)]
            except Exception as err:
                return {'mensaje': 'Ha ocurrido un error', 'error': str(err)}, 400

        else:
            return {'mensaje': 'Por favor ingresar un token válido'}, 401


class ViewHealthCheck(Resource):

    def get(self):
        return {
            "mensaje": "Pipeline de CI/CD funcionando correctamente"
        }, 202
