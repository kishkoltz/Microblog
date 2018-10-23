from flask import Blueprint

bp = Blueprint('auth', _name_)

from app.auth import routes
