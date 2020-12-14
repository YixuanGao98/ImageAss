from flask import Blueprint

bp = Blueprint('iqa', __name__)

from app.iqa import routes