from .models import letter, anniversary
from users.models import User

def get_user(user_uuid):
    return User.objects.get(uuid = user_uuid)

def get_event(event_uuid):
    return anniversary.objects.get(uuid = event_uuid)