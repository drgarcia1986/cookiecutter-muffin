from .. import app


@app.register('/', methods=['GET'])
def index(request):
    return app.ps.jinja2.render('index.html')
