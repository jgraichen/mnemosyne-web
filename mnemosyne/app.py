import aiohttp
import aiohttp.web

import asyncio

from mnemosyne.app import by_time, by_uuid

app = aiohttp.web.Application()

# by_uuid API
# app.router.add_route('GET', '/applications', mnemosyne.applications.index)
app.router.add_route('GET', '/trace/{traceUuid}', by_uuid.getTrace)
app.router.add_route('GET', '/transaction/{transactionUuid}', by_uuid.getTransaction)
app.router.add_route('GET', '/application/{applicationUuid}', by_uuid.getApplication)

# by_time API
app.router.add_route('GET', '/traces/frontend/age/{ageInMin}', by_time.getFrontendTraces)
