from aiohttp import web
from mnemosyne import json
from mnemosyne.resources import Application

async def index(request):
    applications = []

    async with request.db.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT id, name, original_name FROM applications")

            async for row in cur:
                applications.append(Application(*row))

    return web.json_response(applications, dumps=json.dumps)
