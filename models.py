from app import db


class Image(db.Model):
    __tablename__ = 'files'

    id = db.Column('id', db.Integer, primary_key=True)
    file = db.Column('file', db.BLOB)

    def __repr__(self):
        return '<file %r>' % self.id

