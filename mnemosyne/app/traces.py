from aiohttp import web
from mnemosyne import json
from mnemosyne.resources import Trace, Span

async def index(request):
    traces = []

    async with request.db.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT id, name FROM traces LIMIT 20")

            async for row in cur:
                traces.append(Trace(*row))

    return web.json_response(traces, dumps=json.dumps)


async def show(request):
    uuid = request.match_info['uuid']
    trace = await _trace(request, uuid)
    spans = []

    async with request.db.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("""
                SELECT id, name, start, stop, meta
                FROM spans
                WHERE trace_id = %s
                ORDER BY start ASC
            """, (uuid,))

            async for row in cur:
                spans.append(Span(*row))

    trace.spans = spans

    return web.json_response(trace, dumps=json.dumps)

async def _trace(request, uuid):
    async with request.db.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("""
                SELECT id, name, start, stop, meta
                FROM traces
                WHERE id = %s
            """, (uuid,))

            async for row in cur:
                return Trace(*row)
