from application import models  # noqa: F401
from application.app import app, db  # noqa: F401
from application.views import book, video, views  # noqa: F401


try:
    # Create tables if they don't exist
    db.create_all()
except Exception:
    pass
