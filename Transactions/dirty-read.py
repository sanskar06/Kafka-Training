from confluent_kafka import Consumer,DeserializingConsumer
from confluent_kafka.serialization import StringDeserializer




conf = {'bootstrap.servers': 'localhost:9092',
        'group.id': "sanskar-id-1",
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': False,}


# without isolation level
def dirty_read():
    conf['key.deserializer'] = StringDeserializer()
    conf["value.deserializer"] = StringDeserializer()
    conf["isolation.level"]="read_uncommitted"
    consumer = DeserializingConsumer(conf)
    consumer.subscribe(['my-topic'])
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        print(f'Received message: {msg.value()} in dirty read')


dirty_read()