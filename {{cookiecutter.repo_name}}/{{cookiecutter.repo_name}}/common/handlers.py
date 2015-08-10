import asyncio

import muffin

from .. import app
from .exceptions import ValidationError, ProcessError


class FormHandler(muffin.Handler):
    """ generic Form handler """

    template = None
    success_redirect = None

    @asyncio.coroutine
    def validate(self, request):
        """ Validate form content (before process)"""

    @asyncio.coroutine
    def process(self, request):
        """ Process form content (after validation) """

    def get(self, request):
        return app.ps.jinja2.render(self.template)

    def post(self, request):
        try:
            yield from self.validate(request)
            yield from self.process(request)
        except (ValidationError, ProcessError) as e:
            return app.ps.jinja2.render(self.template, errors=e.errors)

        return muffin.HTTPFound(self.success_redirect)
