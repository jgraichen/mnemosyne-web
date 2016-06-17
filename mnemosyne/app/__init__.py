import aiohttp
import aiohttp.web

from mnemosyne.app import by_time, by_uuid

application = aiohttp.web.Application()

# by_uuid API
# app.router.add_route('GET', '/applications', mnemosyne.applications.index)
application.router.add_route('GET', '/trace/{traceUuid}', by_uuid.getTrace)
application.router.add_route('GET', '/transaction/{transactionUuid}', by_uuid.getTransaction)
application.router.add_route('GET', '/application/{applicationUuid}', by_uuid.getApplication)

# by_time API
application.router.add_route('GET', '/traces/frontend/age/{ageInMin}', by_time.getFrontendTraces)
