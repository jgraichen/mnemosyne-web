from aiohttp import web
from mnemosyne import json
from mnemosyne.resources import Transaction

async def index(request):
    transactions = []

    async with request.db.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("""
                SELECT DISTINCT transaction_id, name, meta
                FROM traces
                WHERE origin_id IS NULL
                LIMIT 20
            """)

            async for row in cur:
                transactions.append(Transaction(*row))

    return web.json_response(transactions, dumps=json.dumps)
