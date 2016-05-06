import asyncio
import aioamqp

@asyncio.coroutine
def callback(channel, body, envelope, properties):
    print(body)

@asyncio.coroutine
def connect():
    try:
        transport, protocol = yield from aioamqp.connect()
        channel = yield from protocol.channel()
    except aioamqp.AmqpClosedConnection:
        print("closed connections")
        return

    yield from channel.exchange("mnemosyne", "traces", durable=True)

    yield from channel.queue(queue_name="mnemosyne-server", durable=True)

    yield from channel.queue_bind(exchange_name="mnemosyne", queue_name="hello", routing_key="#")

    print(' [*] Waiting for logs. To exit press CTRL+C')

    yield from channel.basic_consume(callback, queue_name="mnemosyne-server", no_ack=True)
    
    # close using the `AMQP` protocol
    #yield from protocol.close()
    # ensure the socket is closed.
    #transport.close()

event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(connect())
event_loop.run_forever()
