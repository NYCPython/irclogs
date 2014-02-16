from datetime import datetime, timedelta

from flask import Blueprint, abort, current_app, send_from_directory

from .models import Message

angular_blueprint = Blueprint('irclogs', __name__, static_folder='static', template_folder='templates', url_prefix='/')

@angular_blueprint.route('/')
def angular_resources(filename='/'):
    '''Handles sending angular resources to the browser

    Note: this should be used only when a static webserver 
    is not available (ex. local development). When deployed, 
    point your webserver to the angular resource directory 
    instead of allowing flask to handle the files. Performance 
    will be greatly improved.

    '''
    if not filename or filename == '/':
        filename = 'index.html'
    print(current_app.config['ANGULAR_RESOURCE_DIRECTORY'])
    return send_from_directory(current_app.config['ANGULAR_RESOURCE_DIRECTORY'], filename)
