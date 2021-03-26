from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class UserModel(Model):
    class Meta:
        host = "http://0.0.0.0:4566"
        table_name = "User"

    email = UnicodeAttribute(hash_key=True)

    name_given = UnicodeAttribute()
    name_family = UnicodeAttribute()
