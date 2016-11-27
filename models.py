'''
Created on Oct 24, 2016

@author: nygrendr
'''

from google.appengine.ext import ndb
from google.appengine.api import blobstore
from google.appengine.api.blobstore.blobstore import BlobKey
from google.appengine.ext.webapp import blobstore_handlers


class User(ndb.Model):
    # internal
    ID = ndb.StringProperty()
    # Rose Fire
    username = ndb.StringProperty()
    email = ndb.StringProperty()
    name = ndb.StringProperty()
    # questions

    gradyear = ndb.IntegerProperty()
    primary_major = ndb.IntegerProperty()
    secondary_major_or_minor = ndb.IntegerProperty()
    full_time = ndb.BooleanProperty()
    has_job = ndb.BooleanProperty()

    tshirt_size = ndb.StringProperty()
    dietary_restrictions = ndb.StringProperty()

    resume_blob_key = ndb.BlobKeyProperty()
