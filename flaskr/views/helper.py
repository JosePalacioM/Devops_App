from requests import Response, get
from ..models import db


class Helper():

    def get_client_ip(self):
        ip_address = get('https://api.ipify.org').content.decode('utf8')
        return ip_address
