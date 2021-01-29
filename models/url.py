from config import db, engine
from random import choices
from sqlalchemy.sql import text

class URL(db.Model):
    """URL model for DB"""

    id = db.Column(db.Integer, primary_key = True)
    key = db.Column(db.String(4), nullable = False, unique = True)
    url = db.Column(db.String(), nullable = False)

    def __init__(self, key, url):
        self.key = key
        self.url = url

    def __repr__(self):
        return f'URL({self.key}, {self.url})'

    @staticmethod
    def GenerateKey():
        vals = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        while True:
            key = "".join(choices(vals, k = 4))
            with engine.connect() as con:
                try:
                    sql = text("SELECT COUNT(1) FROM url WHERE key = :key")
                    res = con.execute(sql, key = key).scalar()
                except:
                    pass

            if not res > 0:
                return key