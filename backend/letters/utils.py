from .models import letter, anniversary
from users.models import User
import boto3
from backend.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME

def get_user(user_uuid):
    return User.objects.get(uuid = user_uuid)

def get_event(event_uuid):
    return anniversary.objects.get(uuid = event_uuid)

def get_user_id(user_uuid):
    return User.objects.get(uuid = user_uuid).id

def get_event_name(event_id):
    return anniversary.objects.get(id = event_id).name

def get_event_id(event_uuid):
    return anniversary.objects.get(uuid = event_uuid).id

def get_file_url(data, uuid, input_type="file"):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    if input_type == "file":
        type = "jpg"
    elif input_type == "media":
        type = "mp3"
    s3_client.put_object(Body=data, Bucket=AWS_STORAGE_BUCKET_NAME, Key=uuid + "." + type)
    url = "http://"+AWS_STORAGE_BUCKET_NAME+".s3.ap-northeast-2.amazonaws.com/" + \
                uuid + "." + type
    url = url.replace(" ", "/")
    return url