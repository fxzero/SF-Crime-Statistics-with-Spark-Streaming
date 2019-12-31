from kafka import KafkaConsumer

consumer = KafkaConsumer(
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id = "0")

consumer.subscribe(['org.udacity.service.calls'])

for message in consumer:
    print(message.value)
        