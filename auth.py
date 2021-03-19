from functools import wraps
from flask import request, Response
import bcrypt


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    Password is y7KYAm9Ns8Au
    """
    return username == 'repo_access' \
           and bcrypt.checkpw(password.encode('utf-8'), b'$2b$12$zDimSxEiYwHfJDu5ovkndOtAavwM1IogGj.4.QlDvOa66YslVD4lO')


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required", charset="UTF-8"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated
