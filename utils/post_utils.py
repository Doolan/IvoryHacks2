# from models import Post, Reply
# from google.appengine.ext import ndb
#
# UNIVERSAL_PARENT = ndb.Key("Entity",'DARTH_VADER')
#
# def get_query_for_all_posts():
#     """ Returns a query for all OBJECTS for this user. """
#     return Post.query(ancestor=UNIVERSAL_PARENT).order(Post.time)
#
#
# def get_query_for_all_posts_by_user(user):
#     """ Returns a query for all OBJECTS for this user. """
#     return Post.query(ancestor=UNIVERSAL_PARENT).filter(Post.author == user.key).order(Post.time)
#
#
# def get_query_for_all_nonanonymous_posts_by_user(user):
#     """ Returns a query for all OBJECTS for this user. """
#     return Post.query(ancestor=UNIVERSAL_PARENT).filter(Post.author == user.key, Post.is_anonymous == False).order(Post.time)
#
#
# def get_post_by_id(post_id):
#     """ Returns a query for all OBJECTS for this user. """
#     #return Post.get_by_id(int(post_id))
# #    return Post.query(ancestor=UNIVERSAL_PARENT).fetch(limit=1)[0]
#     return ndb.Key("Post", post_id, parent=UNIVERSAL_PARENT).get()
#     #return Post.query(ancestor=UNIVERSAL_PARENT).get_by_id
#     #return Post.query(ancestor=UNIVERSAL_PARENT).filter(Post.ID==post_id)
#
#
# def get_replies_for_post_by_id(post_id):
#     """ Returns a query for all OBJECTS for this user. """
#     #return Reply.query(ancestor = ndb.Key('Post', post_id))
#     return Reply.query(Reply.parent == ndb.Key('Post', post_id, parent=UNIVERSAL_PARENT))
