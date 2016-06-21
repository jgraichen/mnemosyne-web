
import os
import aiohttp
import aiohttp.web

from mnemosyne.app import by_time, by_uuid
from mnemosyne.app import applications, middleware, traces, transactions

application = aiohttp.web.Application(middlewares=[
    middleware.DatabaseMiddleware
])

#
# API
#
application.router.add_route('GET', '/api/applications', applications.index)
application.router.add_route('GET', '/api/transactions', transactions.index)
application.router.add_route('GET', '/api/transactions/{uuid}', transactions.show)
application.router.add_route('GET', '/api/traces', traces.index)

#
# by_uuid API
#
application.router.add_route('GET', '/trace/{traceUuid}', by_uuid.getTrace)
application.router.add_route(
    'GET', '/transaction/{transactionUuid}', by_uuid.getTransaction)
application.router.add_route(
    'GET', '/application/{applicationUuid}', by_uuid.getApplication)

#
# by_time API
#
application.router.add_route(
    'GET', '/traces/frontend/age/{ageInMin}', by_time.getFrontendTraces)


#
# Server static files
#
class DirectoryIndex(aiohttp.web.StaticRoute):
    def handle(self, request):
        filename = request.match_info['filename']

        if not filename:
            filename = 'index.html'
        elif filename.endswith('/'):
            filename += 'index.html'

        request.match_info['filename'] = filename

        return super().handle(request)

public_dir = os.path.abspath(os.path.join(__file__, '../../../public'))

application.router.register_route(DirectoryIndex(None, '/', public_dir))
