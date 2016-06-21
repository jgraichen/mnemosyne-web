from aiohttp import web
from mnemosyne import json
from mnemosyne.resources import Trace

async def index(request):
    traces = []

    async with request.db.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT id, name FROM traces LIMIT 20")

            async for row in cur:
                traces.append(Trace(*row))

    return web.json_response(traces, dumps=json.dumps)
