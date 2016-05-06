import asyncio
import aioamqp
import aiopg
import json

from datetime import datetime


async def callback(channel, body, envelope, properties):
    decoded_blob = json.loads(body.decode("utf-8"))
    trace_uuid = decoded_blob["uuid"]
    transaction_uuid = decoded_blob["transaction"]
    origin_uuid = None if not decoded_blob["origin"] else decoded_blob["origin"]
    start_time = datetime.fromtimestamp(decoded_blob["start"] / 1e9)
    end_time = datetime.fromtimestamp(decoded_blob["stop"] / 1e9)
    meta = json.dumps(decoded_blob["meta"])
    trace_name = decoded_blob["name"]

    dsn = 'dbname=mnemosynetest1'

    async with aiopg.create_pool(dsn) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("INSERT INTO traces (trace_uuid, transaction_uuid, origin_uuid, start_time, end_time, meta, trace_name) VALUES (%s, %s, %s, %s, %s, %s, %s)", (trace_uuid, transaction_uuid, origin_uuid, start_time, end_time, meta, trace_name))

    print(decoded_blob)

async def connect():
    try:
        transport, protocol = await aioamqp.connect()
        channel = await protocol.channel()
    except aioamqp.AmqpClosedConnection:
        print("closed connections")
        return

    await channel.exchange("mnemosyne", "topic", durable=True)

    await channel.queue(queue_name="mnemosyne-server", durable=True)

    await channel.queue_bind(exchange_name="mnemosyne", queue_name="mnemosyne-server", routing_key="#")

    print(' [*] Waiting for traces. To exit press CTRL+C')

    await channel.basic_consume(callback, queue_name="mnemosyne-server", no_ack=True)
    
    # close using the `AMQP` protocol
    #yield from protocol.close()
    # ensure the socket is closed.
    #transport.close()

event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(connect())
event_loop.run_forever()
