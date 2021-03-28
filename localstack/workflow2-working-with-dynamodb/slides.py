import os

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

TABLE_NAME = os.getenv("TABLE_NAME")
LOCALSTACK_ENDPOINT = os.getenv("LOCALSTACK_ENDPOINT", None)

class UserModel(Model):
    class Meta:
        host = TABLE_NAME

    if LOCALSTACK_ENDPOINT:
        setattr(Meta, "host", LOCALSTACK_ENDPOINT)

    email = UnicodeAttribute(hash_key=True)

    name_given = UnicodeAttribute()
    name_family = UnicodeAttribute()
