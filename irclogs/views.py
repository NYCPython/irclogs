from datetime import datetime, timedelta

from flask import Blueprint, render_template

from .models import Message

frontend = Blueprint('frontend', __name__, static_folder='static', template_folder='templates')

@frontend.route('/')
def index():
    return render_template('irclogs/index.html')
