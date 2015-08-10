import asyncio


import muffin


@asyncio.coroutine
def middleware_current_user(app, handler):
    """ set current_user in muffin locals """
    @asyncio.coroutine
    def middleware(request):
        local = muffin.local(app.loop)

        user = yield from app.ps.session.load_user(request)
        local.current_user = user

        response = yield from handler(request)

        local.current_user = None

        return response
    return middleware
