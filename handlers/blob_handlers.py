from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

# Straight from https://cloud.google.com/appengine/docs/python/blobstore/
class BlobServer(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, blob_key):
        if not blobstore.get(blob_key):
            self.error(404)
        else:
            self.send_blob(blob_key)