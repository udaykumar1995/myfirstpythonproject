from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, fields
from .models import UserItem


class UserItemSchema(SQLAlchemySchema):

    class Meta:
        model = UserItem
        load_instance = True

    id = fields.fields.String()
    name = fields.fields.String()
    password = fields.fields.String()
    age = fields.fields.Int()
    gender = fields.fields.String()
    address = fields.fields.String()
