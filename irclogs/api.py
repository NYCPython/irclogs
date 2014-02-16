from .core import api
from .models import Message

api.create_api(Message, url_prefix='/api/v1')
