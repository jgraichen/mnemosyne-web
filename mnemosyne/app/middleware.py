import asyncio
import aiopg

_lock = asyncio.Lock()
_db_pool = False

async def _acquire_pool():
    global _db_pool

    if _db_pool:
        return _db_pool

    async with _lock:
        if not _db_pool:
            _db_pool = await aiopg.create_pool('dbname=mnemosyne_development', maxsize=50)

    return _db_pool


async def DatabaseMiddleware(app, handler):
    db = await _acquire_pool()

    async def middleware_handler(request):
        request.db = db

        return await handler(request)

    return middleware_handler
