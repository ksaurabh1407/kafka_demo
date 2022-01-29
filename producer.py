from kafka import KafkaProducer
import json

def orders(order_message):
  TOPIC_NAME = 'items'
  KAFKA_SERVER = 'localhost:9092'
  kafka_msg = json.dumps(order_message).encode()
  producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
  producer.send(TOPIC_NAME,kafka_msg)
  producer.flush()
  return (order_message)