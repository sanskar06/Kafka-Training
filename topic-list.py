from kafka import KafkaAdminClient
client = KafkaAdminClient(bootstrap_servers='localhost:9092')
topics = client.list_topics()
for topic in topics:
    print(topic)

client = KafkaAdminClient(bootstrap_servers='localhost:9092')
topic1 = client.describe_topics(['my-topic'])
print(topic1)
# topic1 will return the list of dict having error code , topic name and partition etc info 