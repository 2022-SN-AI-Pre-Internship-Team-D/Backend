from .models import letter, anniversary
from users.models import User

def get_user_id(user_uuid):
    return User.objects.get(uuid = user_uuid).id

def get_event_id(event_uuid):
    return anniversary.objects.get(uuid = event_uuid).id