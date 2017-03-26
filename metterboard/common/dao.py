import sqlite3
from flask import g


DATABASE = 'sqlite:////tmp/metterboard.db'

class SqlDao(object):

    MAX_RESULTS_SIZE = 500

    def __init__(self, conn=None):
        self._conn = conn

    def get_db():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
        return db

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()
