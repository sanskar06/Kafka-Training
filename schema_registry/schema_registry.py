from confluent_kafka import SerializingProducer
import json
from confluent_kafka.schema_registry.schema_registry_client import SchemaRegistryClient 
from confluent_kafka.schema_registry.avro import AvroSerializer

schema_registry = SchemaRegistryClient({'url': "http://localhost:8085"})


schema = '{"type": "record", "name": "User", "fields": [{"name": "name", "type": "string"}, {"name": "age", "type": "int"}]}'

avro_serializer = AvroSerializer(schema_registry_client=schema_registry,schema_str=str(schema))

conf={'bootstrap.servers':"localhost:9092",'value.serializer': avro_serializer}

producer = SerializingProducer(conf)
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

producer.produce(topic='my-topic-value', value={'name': 'sanskar', 'age': 21}, on_delivery=delivery_report)
producer.flush()
producer.poll(1)
