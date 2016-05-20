import aiohttp
import aiohttp.web

import asyncio
import aiopg
from datetime import datetime
import json

async def index(request):
  with open ("static/index.html", "r") as indexHtml:
    data = indexHtml.read()
  return aiohttp.web.Response(text=data, content_type='text/html')

async def getTrace(request):
  # Who needs real working code?
  #traceUuid = request.match_info.get('traceUuid')
  #trace = {'trace_uuid': traceUuid, 'spans': []}
  #dsn = 'dbname=mnemosynetest1'
  #async with aiopg.create_pool(dsn) as pool:
  #  async with pool.acquire() as conn:

  #    async with conn.cursor() as cur:
  #      await cur.execute(
  #        "SELECT transaction_uuid, origin_uuid, application_uuid, name, start_time, end_time, meta FROM traces WHERE uuid=%s",
  #        (traceUuid,))
  #      async for row in cur:
  #        trace['transaction_uuid'] = str(row[0])
  #        trace['origin_uuid'] = str(row[1])
  #        trace['application_uuid'] = str(row[2])
  #        trace['trace_name'] = row[3]
  #        trace['start_time'] = row[4].timestamp() * 1000 * 1000
  #        trace['end_time'] = row[5].timestamp() * 1000 * 1000
  #        trace['meta'] = row[6]

  #    async with conn.cursor() as cur:
  #      await cur.execute(
  #        "SELECT uuid, name, start_time, end_time, meta FROM spans WHERE trace_uuid=%s",
  #        (traceUuid,))
  #      async for row in cur:
  #        span = {}
  #        span['span_uuid'] = str(row[0])
  #        span['span_name'] = str(row[1])
  #        span['start_time'] = row[2].timestamp() * 1000 * 1000
  #        span['end_time'] = row[3].timestamp() * 1000 * 1000
  #        span['meta'] = row[4]
  #        trace['spans'].append(span)

  # Just stub it, srsly ;).
  with open ("stub/95fabf78-96cc-4e8d-87c5-715fd5400936.json", "r") as traceJson:
    trace = json.loads(traceJson.read())

  return aiohttp.web.json_response(trace)

app = aiohttp.web.Application()
app.router.add_route('GET', '/', index)
app.router.add_route('GET', '/trace/{traceUuid}', getTrace)

if __name__ == "__main__":
  aiohttp.web.run_app(app)
