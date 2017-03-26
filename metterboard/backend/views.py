from flask import Blueprint, Response

backend = Blueprint('backend', __name__, url_prefix='/backend')


@backend.route('/tracking/<hashtag>', methods=['GET'])
def track(hashtag):
    return Response('tracking ' + str(hashtag))
