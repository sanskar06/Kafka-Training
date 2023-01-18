from confluent_kafka import Producer,SerializingProducer
from confluent_kafka.serialization import StringSerializer
import socket
import json

# conf = {'bootstrap.servers': "localhost:9092",
#         'client.id': socket.gethostname(),
#         'key.serializer': str.encode,
#         'value.serializer': str.encode
#         }
#cimpl.KafkaException: KafkaError{code=_INVALID_ARG,val=-186,str="No such configuration property: "key.serializer""}
conf = {'bootstrap.servers': "localhost:9092",
         'client.id': socket.gethostname()} 
producer = Producer(conf)

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

def serialize(message):
    return json.dumps(message).encode()

def producer_with_key_callback():
    producer.produce('my-topic', key="key", value="msg from confluent kafka", callback=acked)
    producer.flush()
    producer.poll(1)

def producer_with_manual_partition():
    producer.produce('my_topic',value="partition value",partition=2)
    producer.flush()

def producer_serializer():
    conf={'bootstrap.servers': 'localhost:9092'}
    producer=SerializingProducer(conf=conf)
    producer.produce('my-topic',key="serialized_key",value=serialize("serialized_value_message1"))
    producer.flush()

producer_serializer()



