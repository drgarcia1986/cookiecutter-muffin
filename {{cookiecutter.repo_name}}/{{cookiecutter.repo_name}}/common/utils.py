import muffin

from .. import app


@app.ps.jinja2.context_processor
def current_user_context():
    local = muffin.local(app.loop)
    current_user = getattr(local, 'current_user')
    return {'user': current_user}
