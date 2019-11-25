from application.app import db


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class Bookmark(Base):
    __tablename__ = 'bookmark'

    read_status = db.Column(db.Boolean, default=False)
    read_date = db.Column(db.DateTime)
    header = db.Column(db.String(50))
    comment = db.Column(db.String(1024))

    __mapper_args__ = {
        'polymorphic_identity': 'bookmark'
    }


class Book(Bookmark):
    __tablename__ = 'book'

    id = db.Column(db.Integer, db.ForeignKey('bookmark.id'), primary_key=True)
    ISBN = db.Column(db.String(17))
    writer = db.Column(db.String(250))

    __mapper_args__ = {
        'polymorphic_identity': 'book',
    }


class Blog(Bookmark):
    __tablename__ = 'blog'

    id = db.Column(db.Integer, db.ForeignKey('bookmark.id'), primary_key=True)
    URL = db.Column(db.String(250))
    writer = db.Column(db.String(250))

    __mapper_args__ = {
        'polymorphic_identity': 'blog',
    }


class Podcast(Bookmark):
    __tablename__ = 'podcast'

    id = db.Column(db.Integer, db.ForeignKey('bookmark.id'), primary_key=True)
    name = db.Column(db.String(250))
    description = db.Column(db.String(1024))
    author = db.Column(db.String(250))

    __mapper_args__ = {
        'polymorphic_identity': 'podcast',
    }


class Video(Bookmark):
    __tablename__ = 'video'

    id = db.Column(db.Integer, db.ForeignKey('bookmark.id'), primary_key=True)
    URL = db.Column(db.String(250))

    __mapper_args__ = {
        'polymorphic_identity': 'video',
    }
