from kafka import KafkaConsumer

def consumer_func():
    consumer1 = KafkaConsumer('my-topic',bootstrap_servers=['localhost:9092'],auto_offset_reset='earliest')

    for msg in consumer1:
        print()
        print(msg.value)
        print(type(msg))
    
consumer_func()