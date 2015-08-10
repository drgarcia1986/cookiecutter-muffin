import asyncio

import muffin

from .. import app
from ..common.handlers import FormHandler
from ..common.exceptions import ValidationError, ProcessError
from .models import User


@app.register('/users/home/')
@app.ps.session.user_pass()
def home(request):
    return app.ps.jinja2.render('home.html')


@app.register('/users/logout/')
@app.ps.session.user_pass()
def logout(request):
    yield from app.ps.session.logout(request)
    return muffin.HTTPFound('/')


@app.register('/users/signup/')
class UserSignup(FormHandler):

    template = 'signup.html'
    success_redirect = '/users/home/'

    @asyncio.coroutine
    def validate(self, request):
        errors = []
        form_data = yield from request.post()

        try:
            email = form_data.get('email')
            user = User.get(User.email == email)
            if user:
                errors.append('User {} already exists'.format(email))
        except User.DoesNotExist:
            pass

        if len(errors) > 0:
            raise ValidationError(errors)

    @asyncio.coroutine
    def process(self, request):
        form_data = yield from request.post()
        password = User.generate_password(form_data.get('password'))
        user = User.create(
            email=form_data.get('email'),
            name=form_data.get('name'),
            password=password
        )
        yield from app.ps.session.login(request, user.email)


@app.register('/users/signin/')
class UserSignin(FormHandler):

    template = 'signin.html'
    success_redirect = '/users/home/'

    @asyncio.coroutine
    def process(self, request):
        errors = []
        form_data = yield from request.post()
        try:
            email = form_data.get('email')
            user = User.get(User.email == email)
            if not user.check_password(form_data.get('password')):
                errors.append('Invalid password')
        except User.DoesNotExist:
            errors.append('User {} not found'.format(email))

        if len(errors) > 0:
            raise ProcessError(errors)

        yield from app.ps.session.login(request, user.email)
