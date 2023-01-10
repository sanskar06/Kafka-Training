from kafka import  KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

producer.send('my-topic', key=b'key1', value=b'value1')

producer.send('my-topic', key=b'key2', value=b'value2')

producer.flush()
