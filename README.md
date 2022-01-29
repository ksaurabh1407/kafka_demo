# Start zookeeper service
bin/zookeeper-server-start.sh config/zookeeper.properties
# Start kafka broker service
bin/kafka-server-start.sh config/server.properties
# Create a topic named 'items'
bin/kafka-topics.sh --create --topic items --bootstrap-server localhost:9092