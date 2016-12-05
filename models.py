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
    #Hackathon
    role = ndb.StringProperty()
    tsize = ndb.StringProperty()
    hacktype = ndb.StringProperty()
    diet = ndb.StringProperty()

    #Employment
    gradYear = ndb.StringProperty()
    major = ndb.StringProperty()
    secondary = ndb.StringProperty()
    status = ndb.StringProperty()

    resume_blob_key = ndb.BlobKeyProperty()
