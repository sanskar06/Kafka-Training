from confluent_kafka import Producer,StringSerializer
import socket

conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}
producer = Producer(conf)

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))
def producer_with_key_callback():
    producer.produce('my-topic', key="key", value="msg from confluent kafka", callback=acked)
    producer.flush()
    producer.poll(1)
def producer_with_serializer():
    producer.set_key_serializer(StringSerializer())
    producer.set_value_serializer(StringSerializer())
    producer.produce('my_topic', key='serialized_key', value='serialized_value')
    producer.flush()
def producer_with_manual_partition():
    producer.produce('my_topic',value="partition value",partition=2)
    producer.flush()