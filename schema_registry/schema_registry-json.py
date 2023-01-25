from confluent_kafka import SerializingProducer
import os
from confluent_kafka.schema_registry.schema_registry_client import SchemaRegistryClient 
from confluent_kafka.schema_registry.json_schema import JSONSerializer

schema_registry = SchemaRegistryClient({'url': "http://localhost:8085"})
def func(a,b):
    return "my-topic-new_schema"

schema_str = """{"type":"object","title":"new_schema","properties":{"f1":{"type":"int"}}}"""
json_serializer = JSONSerializer(schema_registry_client =schema_registry,schema_str=str(schema_str))
conf={'bootstrap.servers':os.environ.get('KAFKA_BROKER'),'value.serializer': json_serializer}
producer = SerializingProducer(conf)
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

producer.produce(topic='schema-value', value={"f1": 5} ,on_delivery=delivery_report)
producer.flush()