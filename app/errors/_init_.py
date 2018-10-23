from flask import Blueprint

bp = Blueprint('errors', _name_)

from app.errors import handlers
