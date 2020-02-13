import datetime
import jwt

from django.utils import timezone
from django.conf import settings

from core.constants import JWT_DEFAULTS


class TimeZone:
    @staticmethod
    def datetime():
        return timezone.now()

    @staticmethod
    def time():
        return timezone.datetime.time(timezone.now())

    @staticmethod
    def date():
        return timezone.datetime.date(timezone.now())

    @staticmethod
    def timestamp():
        return timezone.now().timestamp()


def get_user_agent(request):
    return 'FAHIM'


def generate_jwt_payload(request, user=None, days=14):
    payload = {
        'user': user,
        'user_agent': get_user_agent(request),
        'iss': JWT_DEFAULTS['JWT_ISSUER'],
        'iat': TimeZone.datetime(),
        'exp': TimeZone.datetime() + datetime.timedelta(days=days)
    }
    return payload


def jwt_get_user_from_payload(payload):
    return payload.get('user')


def jwt_encode_handler(payload):
    key = settings.SECRET_KEY
    return jwt.encode(
        payload,
        key,
        JWT_DEFAULTS['JWT_ALGORITHM']
    ).decode('utf-8')


def jwt_decode_handler(token):
    options = {
        'verify_exp': JWT_DEFAULTS['JWT_VERIFY_EXPIRATION'],
    }
    secret_key = JWT_DEFAULTS['JWT_SECRET_KEY']
    return jwt.decode(
        token,
        secret_key,
        options=options,
        leeway=JWT_DEFAULTS['JWT_LEEWAY'],
        audience=JWT_DEFAULTS['JWT_AUDIENCE'],
        issuer=JWT_DEFAULTS['JWT_ISSUER'],
        algorithms=[JWT_DEFAULTS['JWT_ALGORITHM']]
    )


def generate_jwt_token(request, user_id):
    payload = generate_jwt_payload(request, user=user_id)
    jwt_token = jwt_encode_handler(payload)
    return jwt_token
