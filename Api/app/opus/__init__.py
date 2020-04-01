from flask import Blueprint
opus = Blueprint('opus', __name__)
from ..opus import urls