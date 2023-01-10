from kafka import KafkaAdminClient
client = KafkaAdminClient(bootstrap_servers='localhost:9092')
topics = client.list_topics()
for topic in topics:
    print(topic)

client = KafkaAdminClient(bootstrap_servers='localhost:9092')
topic1 = client.describe_topics(['my-topic'])
print(topic1)
<<<<<<< HEAD:topic-list.py
# topic1 will return the list of dict having error code , topic name and partition etc info 
=======
# topic1 will return the list of dict having error code , topic name and partition info 
>>>>>>> 5708bc94867103659fa54a2d52de4da0b976c70b:topics/topic-list.py
