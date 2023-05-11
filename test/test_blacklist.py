import json
from unittest import TestCase
from faker import Faker
from application import application
from flaskr.models import MailBlacklist, db


class TestUsuario(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = application.test_client()
        self.bloqued_email = self.data_factory.email()
        self.bloqued_app_uuid = self.data_factory.uuid4()
        self.blocked_reason = self.data_factory.text()

        bloqued_email = {
            'email': self.bloqued_email,
            'app_uuid':  self.bloqued_app_uuid,
            'blocked_reason': self.blocked_reason
        }

        self.client.post('/blacklists', data=json.dumps(bloqued_email), headers={
            'Content-Type': 'application/json', "Authorization": "Bearer {}".format('KeyWord')})

    def tearDown(self):

        mails = MailBlacklist.query.all()
        for mail in mails:
            db.session.delete(mail)

        db.session.commit()

    def test_bloquear_email(self):

        new_block = {
            'email': self.data_factory.email(),
            'app_uuid': self.data_factory.uuid4(),
            'blocked_reason': self.data_factory.text()
        }

        response = self.client.post('/blacklists', data=json.dumps(new_block), headers={
                                    'Content-Type': 'application/json', "Authorization": "Bearer {}".format('KeyWord')})

        self.assertEqual(response.status_code, 300)

    def test_bloquear_email_existente(self):

        new_block = {
            'email': self.bloqued_email,
            'app_uuid': self.data_factory.uuid4(),
            'blocked_reason': self.data_factory.text()
        }

        response = self.client.post('/blacklists', data=json.dumps(new_block), headers={
                                    'Content-Type': 'application/json', "Authorization": "Bearer {}".format('KeyWord')})

        self.assertEqual(response.status_code, 412)

    def test_bloquear_email_sin_app_uuid(self):

        new_block = {
            'email': self.data_factory.email(),
            'app_uuid': '',
            'blocked_reason': self.data_factory.text()
        }

        response = self.client.post('/blacklists', data=json.dumps(new_block), headers={
                                    'Content-Type': 'application/json', "Authorization": "Bearer {}".format('KeyWord')})

        self.assertEqual(response.status_code, 400)

    def test_bloquear_email_sin_token(self):

        new_block = {
            'email': self.data_factory.email(),
            'app_uuid': self.data_factory.uuid4(),
            'blocked_reason': self.data_factory.text()
        }

        response = self.client.post('/blacklists', data=json.dumps(new_block), headers={
                                    'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 401)

    def test_bloquear_email_con_token_invalido(self):

        new_block = {
            'email': self.data_factory.email(),
            'app_uuid': self.data_factory.uuid4(),
            'blocked_reason': self.data_factory.text()
        }

        response = self.client.post('/blacklists', data=json.dumps(new_block), headers={
                                    'Content-Type': 'application/json', "Authorization": "Bearer {}".format('KeyWordInvalid')})

        self.assertEqual(response.status_code, 401)

    def test_consultar_email_bloqueado(self):

        response = self.client.get('/blacklists/{}'.format(self.bloqued_email), headers={
                                   'Content-Type': 'application/json', "Authorization": "Bearer {}".format('KeyWord')})

        self.assertEqual(response.status_code, 300)

    def test_consultar_email_bloqueado_sin_token(self):

        response = self.client.get('/blacklists/{}'.format(self.bloqued_email), headers={
                                   'Content-Type': 'application/json', "Authorization": "Bearer {}".format('KeyWordInvalid')})

        self.assertEqual(response.status_code, 401)

    def test_consultar_email_errado(self):

        response = self.client.get('/blacklists/{}'.format(self.data_factory.email()), headers={
                                   'Content-Type': 'application/json', "Authorization": "Bearer {}".format('KeyWord')})

        self.assertEqual(response.status_code, 404)

    def test_healthcheck(self):

        response = self.client.get('/',
                                   headers={'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 300)
