from .. import app


@app.manage.command
def create_db():
    """
    Create all tables in configured database
    """
    from ..users.models import User  # noqa
    app.ps.peewee.database.create_table(User)
