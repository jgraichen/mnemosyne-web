import aiopg

async def DatabaseMiddleware(app, handler):
    db = await aiopg.create_pool('dbname=mnemosyne_development')

    async def middleware_handler(request):
        request.db = db

        print(request)

        return await handler(request)

    return middleware_handler
