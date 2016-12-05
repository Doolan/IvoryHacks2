import json
import os

import jinja2
import time
import webapp2
from google.appengine.ext import ndb
from webapp2_extras import sessions
import handlers
from models import User
from handlers import BaseHandler, BaseBlobstoreHandler
from rosefire import RosefireTokenVerifier

from google.appengine.api import blobstore
from google.appengine.api.blobstore.blobstore import BlobKey
from google.appengine.ext.webapp import blobstore_handlers
import logging

from utils import post_utils, user_utils

# This normally shouldn't be checked into Git
ROSEFIRE_SECRET = '5LgLSINSUKGVbkwTw0ue'
UNIVERSAL_PARENT = ndb.Key("Entity", 'DARTH_VADER')

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape=True)


class MainHandler(BaseHandler):
    def get(self):
        template = JINJA_ENV.get_template("templates/index.html")
        if "user_info" in self.session:
            #             user_info = json.loads(self.session["user_info"])
            #             print("user_info", user_info)
            #             self.response.out.write(template.render({"user_info": user_info}))
            self.redirect("/register")
            return
        else:
            self.response.out.write(template.render())


class RegisterHandler(BaseHandler):
    def get(self):
        if "user_info" not in self.session:
            #            raise Exception("Missing user!")
            self.redirect("/")
            return

        else:
            user_utils.get_user_from_rosefire_user(self.user())
            # username = self.request.get('username', 'none')
            # if username == 'none':
            user_info = json.loads(self.session.get("user_info"))
            user = user_utils.get_user_from_username(user_info["username"])
            # is_self = True
            print("user info", user_info)
            # else:
            #     userResults = User.query(User.username == username).fetch(limit=1)
            #     if len(userResults) == 0:
            #         self.redirect(uri="/profile")
            #         return
            #     else:
            #         user = userResults[0]

            # print("user", user)
            values = {"user": user}
            values["form_action"] = blobstore.create_upload_url('/update-resume')

            template = JINJA_ENV.get_template("templates/register.html")

            self.response.out.write(template.render(values))


class ViewProfileHandler(BaseHandler):
    # def get_page_title(self):
    #     return "View Post"

    def get(self):
        is_self = False

        if "user_info" not in self.session:
            #            raise Exception("Missing user!")
            self.redirect("/")
            return

        else:
            user_utils.get_user_from_rosefire_user(self.user())
            username = self.request.get('username', 'none')
            if username == 'none':
                user_info = json.loads(self.session.get("user_info"))
                user = user_utils.get_user_from_username(user_info["username"])
                is_self = True
                print("user info", user_info)
            else:
                userResults = User.query(User.username == username).fetch(limit=1)
                if len(userResults) == 0:
                    self.redirect(uri="/profile")
                    return
                else:
                    user = userResults[0]

            print("user", user)

            # query = post_utils.get_query_for_all_nonanonymous_posts_by_user(user)
            values = {  # "post_query": query,
                "user": user,
                "is_self": is_self}

            values["form_action"] = blobstore.create_upload_url('/update-profile')

            template = JINJA_ENV.get_template("templates/profile.html")

            self.response.out.write(template.render(values))


# Auth handlers
class LoginHandler(BaseHandler):
    def get(self):
        if "user_info" not in self.session:
            token = self.request.get('token')
            auth_data = RosefireTokenVerifier(ROSEFIRE_SECRET).verify(token)
            user_info = {"name": auth_data.name,
                         "username": auth_data.username,
                         "email": auth_data.email,
                         "role": auth_data.group}

            self.session["user_info"] = json.dumps(user_info)
        self.redirect(uri="/")


class LogoutHandler(BaseHandler):
    def get(self):
        del self.session["user_info"]
        self.redirect(uri="/")


class UpdateProfileAction(handlers.BaseBlobstoreHandler):
    def post(self):
        logging.info("Received an image blob with this data.")
        userdata = user_utils.get_user_from_rosefire_user(self.user())
        if len(self.get_uploads()) > 0:
            media_blob = self.get_uploads()[0]
            userdata.image_blob_key = media_blob.key()
        userdata.description = self.request.get('profile-description')
        userdata.put()
        # time.sleep(.5)
        self.redirect("/profile")


class UpdateResume(handlers.BaseBlobstoreHandler):
    def post(self):
        logging.info("Received an image blob with this data.")
        userdata = user_utils.get_user_from_rosefire_user(self.user())
        if len(self.get_uploads()) > 0:
            media_blob = self.get_uploads()[0]
            userdata.resume_blob_key = media_blob.key()
        # userdata.description = self.request.get('profile-description')
        userdata.put()
        self.redirect("/logout")


class UpdateRegistration(BaseHandler):
    def post(self):
        if "user_info" not in self.session:
            #            raise Exception("Missing user!")
            self.redirect("/")
            return

        else:
            user_utils.get_user_from_rosefire_user(self.user())
            username = self.request.get('username', 'none')
            # if username == 'none':
            user_info = json.loads(self.session.get("user_info"))
            user = user_utils.get_user_from_username(user_info["username"])
            # is_self = True
            print("user info", user_info)

            #userResults = User.query(User.username == username).fetch(limit=1)
            #if len(userResults) == 0:
            #    user = User(parent=UNIVERSAL_PARENT, username=user_info.username,
            #                email=user_info.email, name=user_info.name)
            #else:
            #    user = userResults[0]
            #hackathon
            user.role = self.request.get('role')
            user.tsize = self.request.get('tsize')
            user.hacktype = self.request.get('hacktype')
            user.diet = self.request.get('diet')
            #Employment
            user.gradYear = self.request.get('gradYear')
            user.major = self.request.get('major')
            user.secondary = self.request.get('secondary')
            user.status = self.request.get('status')
            user.put()

            print("user", user)
            values = {"status": "success"}

            self.response.out.write(json.dumps(values))


config = {}
config['webapp2_extras.sessions'] = {
    # This key is used to encrypt your sessions
    'secret_key': '5LgLSINSUKGVbkwTw0ue',
}

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/img/([^/]+)?', handlers.BlobServer),
    # Auth
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    # Pages
    # ('/post-list', PostListHandler),
    # ('/view-post', ViewPostHandler),
    ('/profile', ViewProfileHandler),
    ('/register', RegisterHandler),
    # Actions
    # ('/post', PostAction),
    # ('/insert-reply', InsertReplyAction),
    ('/update-profile', UpdateProfileAction),
    ('/update-resume', UpdateResume),
    ('/update-registration', UpdateRegistration)
], config=config, debug=True)
