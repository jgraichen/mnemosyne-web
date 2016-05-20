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
  # Valid requests:
  # 3ddb5d78-9356-4946-b5ab-895a658e018f (belongs to available stub transaction 953bdffe-94bc-419c-9749-8c4d88d0e38f) (with cool external references to other traces in spans)
  # 95fabf78-96cc-4e8d-87c5-715fd5400936 (more spans, some with the same name, currently displayed in index.html)
  fname = "stub/trace/" + request.match_info.get('traceUuid') + ".json"
  with open (fname, "r") as traceJson:
    trace = json.loads(traceJson.read())

  return aiohttp.web.json_response(trace)

async def getTransaction(request):
  # Who needs real working code?
  #transactionUuid = request.match_info.get('transactionUuid')
  #transaction = {'transaction_uuid': transactionUuid, 'traces': []}
  #dsn = 'dbname=mnemosynetest1'
  #async with aiopg.create_pool(dsn) as pool:
  #  async with pool.acquire() as conn:

  #    async with conn.cursor() as cur:
  #      await cur.execute(
  #        "SELECT uuid, origin_uuid, application_uuid, name, start_time, end_time, meta FROM traces WHERE transaction_uuid=%s",
  #        (transactionUuid,))
  #      async for row in cur:
  #        trace = {}
  #        trace['trace_uuid'] = str(row[0])
  #        trace['origin_uuid'] = str(row[1])
  #        trace['application_uuid'] = str(row[2])
  #        trace['trace_name'] = row[3]
  #        trace['start_time'] = row[4].timestamp() * 1000 * 1000
  #        trace['end_time'] = row[5].timestamp() * 1000 * 1000
  #        trace['meta'] = row[6]
  #        transaction['traces'].append(trace)

  # Just stub it, srsly ;).
  # Valid request:
  # 953bdffe-94bc-419c-9749-8c4d88d0e38f
  fname = "stub/transaction/" + request.match_info.get('transactionUuid') + ".json"
  with open (fname, "r") as traceJson:
    transaction = json.loads(traceJson.read())

  return aiohttp.web.json_response(transaction)

app = aiohttp.web.Application()
app.router.add_route('GET', '/', index)
app.router.add_route('GET', '/trace/{traceUuid}', getTrace)
app.router.add_route('GET', '/transaction/{transactionUuid}', getTransaction)

if __name__ == "__main__":
  aiohttp.web.run_app(app)
