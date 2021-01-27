from config import db

class URL(db.Model):
    """URL model for DB"""

    id = db.Column(db.Integer, primary_key = True)
    key = db.Column(db.String(7), nullable = False, unique = True)
    url = db.Column(db.String(), nullable = False)

    def __init__(self, key, url):
        self.key = key
        self.url = url

    def __repr__(self):
        return f'URL({self.key}, {self.url})'
