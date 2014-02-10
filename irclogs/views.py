from datetime import datetime, timedelta

from flask import Blueprint, abort, render_template

from .models import Message

bp = Blueprint('irclogs', __name__, static_folder='static', template_folder='templates')

@bp.route('/')
def index():
    messages = Message.query.all()
    return render_template('irclogs/index.html', messages=messages)

@bp.route('/<int:year>/<int:month>/<int:day>/')
def date_view(year, month, day):
    try:
        date = datetime(year=year, month=month, day=day)
    except ValueError:
        abort(404)

    messages = Message.query.filter(Message.created >= date, Message.created < (date + timedelta(days=1)))
    return render_template('irclogs/index.html', messages=messages)
