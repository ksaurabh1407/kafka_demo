# Kafka Demo
This is a small python application to demonstrate Topics and events in Kafka
The entire application conists of three python files:
1. app.py - This is a flask application that exposes REST API with PUT action and passes the JSON message to producer.py
2. producer.py - contains a function to recieve JSON message and store it as an event under Kafka Topic
3. consumer.py - contains a function to retrieve all events stored within a specified Kafka Topic
## Install Kafka (refer link below)
https://kafka.apache.org/quickstart
## Start zookeeper service
bin/zookeeper-server-start.sh config/zookeeper.properties
## Start kafka broker service
bin/kafka-server-start.sh config/server.properties
## Create a topic named 'items'
bin/kafka-topics.sh --create --topic items --bootstrap-server localhost:9092
## Read the events in Kafka Topic named 'items'
bin/kafka-console-consumer.sh --topic items --from-beginning --bootstrap-server localhost:9092
## Run application and pass JSON object through postman
python3 app.py
## Run application to view messages added in the topic
pyhton3 consumer.py