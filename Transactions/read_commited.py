from confluent_kafka import Consumer,DeserializingConsumer
from confluent_kafka.serialization import StringDeserializer



conf = {'bootstrap.servers': 'localhost:9092',
        'group.id': "sanskar-id-2",
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': False,}

def readcommited():
    conf['key.deserializer'] = StringDeserializer()
    conf["value.deserializer"] = StringDeserializer()
    conf["isolation.level"]="read_committed"
    consumer = DeserializingConsumer(conf)
    consumer.subscribe(['my-topic'])
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
        print(f'Received message: {msg.value()} in read committed')
    
readcommited()