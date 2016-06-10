import aiohttp
import aiohttp.web

import asyncio

import by_uuid

app = aiohttp.web.Application()

# by_uuid API
app.router.add_route('GET', '/trace/{traceUuid}', by_uuid.getTrace)
app.router.add_route('GET', '/transaction/{transactionUuid}', by_uuid.getTransaction)
app.router.add_route('GET', '/application/{applicationUuid}', by_uuid.getApplication)

if __name__ == "__main__":
  aiohttp.web.run_app(app)
