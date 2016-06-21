import asyncio
from aiohttp import web
from mnemosyne import json
from mnemosyne.resources import Transaction, Trace

async def index(request):
    transactions = []

    async with request.db.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("""
                SELECT DISTINCT transaction_id, start, stop, meta
                FROM traces
                WHERE origin_id IS NULL
                ORDER BY start ASC
                LIMIT 2000
            """)

            async for row in cur:
                transactions.append(_load(conn, row))

    transactions = await asyncio.gather(*transactions)

    return web.json_response(transactions, dumps=json.dumps)


async def _load(conn, row):
    async with conn.cursor() as cur:
        return Transaction(*row)


async def show(request):
    uuid = request.match_info['uuid']
    transaction = await _transaction(request, uuid)
    traces = []

    async with request.db.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("""
                SELECT id, name, start, stop, meta
                FROM traces
                WHERE transaction_id = %s
                ORDER BY start ASC
            """, (uuid,))

            async for row in cur:
                traces.append(Trace(*row))

    transaction.traces = traces

    return web.json_response(transaction, dumps=json.dumps)


async def _transaction(request, uuid):
    async with request.db.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("""
                SELECT transaction_id, start, stop, meta
                FROM traces
                WHERE transaction_id = %s
                ORDER BY start ASC
                LIMIT 1
            """, (uuid,))

            async for row in cur:
                return Transaction(*row)

