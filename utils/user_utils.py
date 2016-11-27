from google.appengine.ext import ndb
import json

from models import User
import logging

UNIVERSAL_PARENT = ndb.Key("Entity", 'DARTH_VADER')


def get_user_from_rosefire_user(rf_user):
    #     logging.info("Hit get user from rose fire" + rf_user)
    rf_user = json.loads(rf_user)
    user = User.query(ancestor=UNIVERSAL_PARENT).filter(User.email == rf_user["email"]).fetch(limit=1)
    # get_by_id(parent=get_parent_key_from_email(rf_user["email"]))
    if len(user) == 0:
        #         logging.info("Failed to find player by id, creating new user")
        user = User(parent=UNIVERSAL_PARENT, ID=rf_user["email"],
                    username=rf_user["username"], email=rf_user["email"], name=rf_user["name"])
        user.put()
        return user
    else:
        return user[0]


def get_user_from_username(username):
    return User.query(ancestor=UNIVERSAL_PARENT).filter(User.username == username).fetch(limit=1)[0]


def get_parent_key_from_email(email):
    return ndb.Key("Entity", email.lower())
