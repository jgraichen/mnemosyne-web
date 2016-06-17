import aiohttp

import aiopg
from datetime import datetime
import json


async def getFrontendTraces(request):
  # Who needs real working code?
  #ageInMin = int(request.match_info.get('ageInMin'))
  #traces = []
  #dsn = 'dbname=mnemosynetest1'
  #async with aiopg.create_pool(dsn) as pool:
  #  async with pool.acquire() as conn:

  #    async with conn.cursor() as cur:
  #      await cur.execute(
  #        "SELECT uuid, origin_uuid, application_uuid, name, start_time, end_time, meta, transaction_uuid FROM traces WHERE origin_uuid IS NULL and start_time > NOW() - INTERVAL '%s minutes'",
  #        (ageInMin,))
  #      async for row in cur:
  #        trace = {}
  #        trace['trace_uuid'] = str(row[0])
  #        trace['origin_uuid'] = str(row[1])
  #        trace['application_uuid'] = str(row[2])
  #        trace['trace_name'] = row[3]
  #        trace['start_time'] = row[4].timestamp() * 1000 * 1000
  #        trace['end_time'] = row[5].timestamp() * 1000 * 1000
  #        trace['meta'] = row[6]
  #        trace['transaction_uuid'] = str(row[7])
  #        traces.append(trace)

  # Just stub it, srsly ;).
  # Valid request:
  # 50
  fname = "stub/traces/frontend/age/" + request.match_info.get('ageInMin') + ".json"
  with open (fname, "r") as tracesJson:
    traces = json.loads(tracesJson.read())

  return aiohttp.web.json_response(traces)